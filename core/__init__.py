"""
core/__init__.py (refatorado) - Core Runtime com DI.
Inicializacao explicita via initialize_core().
"""

from __future__ import annotations
import logging
from pathlib import Path
from typing import Any
from core.config import settings, OpenCodeSettings
from core.container import Container
from core.state import SQLiteStateManager
from core.events import AsyncEventBus
from core.interfaces import IStateManager, IEventBus

logger = logging.getLogger(__name__)

# API Publica
settings: OpenCodeSettings = settings


def initialize_core(db_path: str | Path = '') -> None:
    """Inicializa o core com injecao de dependencia explicita."""
    if Container.instance().is_registered('state_manager'):
        logger.warning('Core already initialized - skipping')
        return

    path = Path(db_path) if db_path else settings.state_db_path()
    sm = SQLiteStateManager(path)
    eb = AsyncEventBus()

    container = Container.instance()
    container.register('state_manager', sm)
    container.register('event_bus', eb)

    import asyncio
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(eb.publish('core.initialized', {'db_path': str(path)}))
    except RuntimeError:
        logger.debug('No running event loop - deferring core.initialized event')

    logger.info('Core initialized - db_path=%s', path)


def reset_for_testing() -> None:
    """Reseta o container - USO APENAS EM TESTES."""
    Container.instance().reset()
    logger.warning('Core reset for testing - all services cleared')


__all__ = [
    'settings',
    'initialize_core',
    'reset_for_testing',
    'Container',
    'IStateManager',
    'IEventBus',
]
