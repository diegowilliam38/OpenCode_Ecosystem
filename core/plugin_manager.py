"""
core/plugin_manager.py — Gerenciamento de Plugins.

Descoberta, carregamento, registro e ciclo de vida de plugins.
Suporta plugins Python (.py) instalados via pip ou locais.

Uso:
    mgr = PluginManager()
    mgr.discover(["plugins/"])
    mgr.load_all()
    plugin = mgr.get_plugin("meu-plugin")
    result = await plugin.execute_hook("on_start", {})
"""

from __future__ import annotations

import importlib
import inspect
import logging
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Protocol

from core.errors import PluginError, NotFoundError

logger = logging.getLogger(__name__)


# ── Protocolo Base para Plugins ────────────────────────────────────


class Plugin(Protocol):
    """Protocolo que todos os plugins podem implementar."""

    name: str

    async def on_load(self, config: dict[str, Any]) -> None:
        """Chamado quando o plugin é carregado."""
        ...

    async def on_unload(self) -> None:
        """Chamado quando o plugin é descarregado."""
        ...

    async def execute_hook(self, hook: str, context: dict[str, Any]) -> Any:
        """Executa um hook específico."""
        ...


# ── Metadados ──────────────────────────────────────────────────────


@dataclass
class PluginMeta:
    """Metadados de um plugin."""
    name: str
    version: str = "1.0.0"
    description: str = ""
    author: str = ""
    hooks: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)


@dataclass
class PluginInstance:
    """Instância carregada de um plugin."""
    meta: PluginMeta
    module: Any = None
    instance: Any = None
    loaded_at: float = field(default_factory=time.time)
    enabled: bool = True


# ── PluginManager ──────────────────────────────────────────────────


class PluginManager:
    """Gerenciador de plugins com descoberta automática.

    Args:
        auto_enable: Se True, plugins são ativados automaticamente após load.
    """

    def __init__(self, auto_enable: bool = True) -> None:
        self._plugins: dict[str, PluginInstance] = {}
        self._search_dirs: list[Path] = []
        self._auto_enable = auto_enable

    # ── Descoberta ─────────────────────────────────────────────────

    def add_search_dir(self, directory: str | Path) -> None:
        """Adiciona diretório para busca de plugins."""
        path = Path(directory)
        if path.exists() and path.is_dir():
            self._search_dirs.append(path.resolve())
            logger.debug("Added plugin search dir: %s", path)

    def discover(self, directories: Optional[list[str | Path]] = None) -> list[str]:
        """Descobre plugins disponíveis nos diretórios de busca.

        Args:
            directories: Lista opcional de diretórios (adiciona aos existentes).

        Returns:
            Lista de nomes de plugins encontrados.
        """
        if directories:
            for d in directories:
                self.add_search_dir(d)

        found: list[str] = []
        for search_dir in self._search_dirs:
            for path in search_dir.glob("*.py"):
                if path.stem.startswith("_"):
                    continue
                if path.stem not in self._plugins:
                    self._plugins[path.stem] = PluginInstance(
                        meta=PluginMeta(
                            name=path.stem,
                            description=f"Plugin from {path.name}",
                        )
                    )
                    found.append(path.stem)
            # Também busca subdiretórios com __init__.py (pacotes)
            for path in search_dir.iterdir():
                if path.is_dir() and (path / "__init__.py").exists():
                    if path.name not in self._plugins:
                        self._plugins[path.name] = PluginInstance(
                            meta=PluginMeta(
                                name=path.name,
                                description=f"Plugin package from {path.name}/",

                            )
                        )
                        found.append(path.name)

        if found:
            logger.info("Discovered %d plugins: %s", len(found), found)
        return found

    # ── Carregamento ───────────────────────────────────────────────

    def load(self, name: str) -> bool:
        """Carrega um plugin específico.

        Args:
            name: Nome do plugin.

        Returns:
            True se carregado com sucesso.

        Raises:
            NotFoundError: Se o plugin não for encontrado.
            PluginError: Se o carregamento falhar.
        """
        plugin = self._plugins.get(name)
        if plugin is None:
            raise NotFoundError(f"Plugin '{name}' not found")

        try:
            module = importlib.import_module(name)
            plugin.module = module

            # Procura instância da classe Plugin
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, "execute_hook") and obj is not type:
                    plugin.instance = obj()
                    break

            plugin.loaded_at = time.time()
            logger.info("Loaded plugin '%s' (v%s)", name, plugin.meta.version)

            if self._auto_enable and plugin.instance:
                import asyncio
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(plugin.instance.on_load({}))
                except RuntimeError:
                    pass

            return True

        except ImportError as e:
            raise PluginError(f"Failed to import plugin '{name}': {e}") from e
        except Exception as e:
            raise PluginError(f"Failed to load plugin '{name}': {e}") from e

    def load_all(self) -> int:
        """Carrega todos os plugins descobertos."""
        count = 0
        for name in list(self._plugins.keys()):
            try:
                if self.load(name):
                    count += 1
            except (PluginError, NotFoundError) as e:
                logger.warning("Skipping plugin '%s': %s", name, e)
        logger.info("Loaded %d/%d plugins", count, len(self._plugins))
        return count

    def unload(self, name: str) -> bool:
        """Descarrega um plugin."""
        plugin = self._plugins.get(name)
        if plugin is None:
            return False

        if plugin.instance:
            try:
                import asyncio
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(plugin.instance.on_unload())
                except RuntimeError:
                    pass
            except Exception as e:
                logger.warning("Error unloading plugin '%s': %s", name, e)

        plugin.instance = None
        plugin.module = None
        plugin.enabled = False
        logger.info("Unloaded plugin '%s'", name)
        return True

    # ── Consultas ──────────────────────────────────────────────────

    def get_plugin(self, name: str) -> Optional[PluginInstance]:
        """Retorna um plugin pelo nome."""
        return self._plugins.get(name)

    def list_plugins(self, loaded_only: bool = False) -> list[PluginInstance]:
        """Lista plugins, opcionalmente apenas os carregados."""
        result = list(self._plugins.values())
        if loaded_only:
            result = [p for p in result if p.module is not None]
        return result

    def get_plugin_names(self) -> list[str]:
        return sorted(self._plugins.keys())

    @property
    def count(self) -> int:
        return len(self._plugins)

    @property
    def loaded_count(self) -> int:
        return sum(1 for p in self._plugins.values() if p.module is not None)

    def __repr__(self) -> str:
        return f"PluginManager(plugins={self.count}, loaded={self.loaded_count})"
