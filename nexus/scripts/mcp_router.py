# -*- coding: utf-8 -*-
# SAÃDA OBRIGATÃ“RIA: PORTUGUÃŠS BRASILEIRO FORMAL
# Toda resposta ao usuÃ¡rio DEVE ser em portuguÃªs do Brasil formal.
# Contexto em chinÃªs para eficiÃªncia de tokens (densidade +40%%).
# Modelo: big-pickle (OpenCode Zen, 200K ctx, 128K out, gratuito)

#!/usr/bin/env python3
"""
MCP Router: Intelligent routing of tasks to Model Context Protocol servers.

Routes tasks based on:
- Required capabilities (filesystem, web, database, etc.)
- Agent specialization and current load
- MCP availability and performance metrics
- Granular synchronization barriers
"""

import json
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import hashlib
from datetime import datetime, timezone


class MCPCapability(Enum):
    """Available MCP capabilities."""
    FILESYSTEM = "filesystem"
    WEB_SEARCH = "web_search"
    DATABASE = "database"
    CODE_EXECUTION = "code_execution"
    LLM_INFERENCE = "llm_inference"
    MEMORY = "memory"
    NOTIFICATION = "notification"
    CUSTOM = "custom"


class AgentSpecialization(Enum):
    """Agent specializations aligned with TMA phases."""
    EMBEDDING = "A1"  # Context mapping
    ATTENTION = "A2"  # Impact analysis
    CONSENSUS = "A3"  # Mediation
    FEED_FORWARD = "A4"  # Execution
    ARCHITECTURE = "A5"  # Validation
    QA = "A6"  # Quality assurance
    INTEGRATION = "A7"  # Deployment
    EVOLUTION = "A8"  # Optimization


@dataclass
class MCPServer:
    """Model Context Protocol server descriptor."""
    id: str
    name: str
    capabilities: List[MCPCapability]
    endpoint: str
    max_concurrent_tasks: int
    current_load: int = 0
    health_score: float = 1.0  # 0.0 to 1.0
    last_heartbeat: str = ""
    
    def is_available(self) -> bool:
        """Check if MCP server is available and healthy."""
        return (
            self.health_score > 0.5 and
            self.current_load < self.max_concurrent_tasks
        )
    
    def can_handle(self, capabilities: List[MCPCapability]) -> bool:
        """Check if server can handle required capabilities."""
        return all(cap in self.capabilities for cap in capabilities)


@dataclass
class TaskDescriptor:
    """Task descriptor with requirements and context."""
    id: str
    agent_id: str
    phase: str
    required_capabilities: List[MCPCapability]
    priority: int = 1  # 1 (low) to 5 (critical)
    estimated_duration_ms: int = 0
    dependencies: List[str] = None
    context: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.context is None:
            self.context = {}


@dataclass
class RoutingDecision:
    """Routing decision with rationale."""
    task_id: str
    mcp_server_id: str
    agent_id: str
    confidence: float  # 0.0 to 1.0
    rationale: str
    alternative_servers: List[str]
    sync_barrier_required: bool
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()


class MCPRouter:
    """Intelligent router for MCP task distribution."""
    
    def __init__(self):
        self.mcp_servers: Dict[str, MCPServer] = {}
        self.routing_history: List[RoutingDecision] = []
        self.agent_specializations = {spec.value: spec.name for spec in AgentSpecialization}
    
    def register_mcp(self, server: MCPServer) -> None:
        """Register a new MCP server."""
        self.mcp_servers[server.id] = server
    
    def route_task(self, task: TaskDescriptor) -> RoutingDecision:
        """
        Route a task to the most suitable MCP server.
        
        Routing strategy:
        1. Filter servers by capability match
        2. Score by: availability, load, specialization alignment, health
        3. Select highest-scoring server
        4. Determine if sync barrier is needed
        """
        # Find capable servers
        capable_servers = [
            server for server in self.mcp_servers.values()
            if server.can_handle(task.required_capabilities) and server.is_available()
        ]
        
        if not capable_servers:
            raise RuntimeError(
                f"No available MCP servers for task {task.id} "
                f"requiring {[c.value for c in task.required_capabilities]}"
            )
        
        # Score each server
        scores = []
        for server in capable_servers:
            score = self._score_server(server, task)
            scores.append((server, score))
        
        # Sort by score (descending)
        scores.sort(key=lambda x: x[1], reverse=True)
        best_server = scores[0][0]
        confidence = scores[0][1]
        
        # Determine if sync barrier is needed
        sync_barrier_needed = self._needs_sync_barrier(task, best_server)
        
        # Build decision
        alternative_servers = [s[0].id for s in scores[1:3]]  # Top 2 alternatives
        decision = RoutingDecision(
            task_id=task.id,
            mcp_server_id=best_server.id,
            agent_id=task.agent_id,
            confidence=confidence,
            rationale=self._build_rationale(task, best_server, scores),
            alternative_servers=alternative_servers,
            sync_barrier_required=sync_barrier_needed
        )
        
        self.routing_history.append(decision)
        return decision
    
    def _score_server(self, server: MCPServer, task: TaskDescriptor) -> float:
        """
        Score a server for a given task.
        
        Factors:
        - Health score (40%)
        - Load factor (30%)
        - Specialization alignment (20%)
        - Priority boost (10%)
        """
        health_score = server.health_score * 0.4
        
        load_factor = (1.0 - (server.current_load / server.max_concurrent_tasks)) * 0.3
        
        # Specialization alignment
        agent_spec = self.agent_specializations.get(task.agent_id, "")
        spec_match = 0.2 if agent_spec in server.name.lower() else 0.1
        
        # Priority boost
        priority_boost = (task.priority / 5.0) * 0.1
        
        return health_score + load_factor + spec_match + priority_boost
    
    def _needs_sync_barrier(self, task: TaskDescriptor, server: MCPServer) -> bool:
        """
        Determine if a sync barrier is needed for this task.
        
        Sync barriers are needed for:
        - Critical tasks (priority >= 4)
        - Tasks with dependencies
        - Cross-phase transitions
        - Database/state-changing operations
        """
        has_dependencies = len(task.dependencies) > 0
        is_critical = task.priority >= 4
        is_state_changing = MCPCapability.DATABASE in task.required_capabilities
        
        return has_dependencies or is_critical or is_state_changing
    
    def _build_rationale(
        self,
        task: TaskDescriptor,
        selected_server: MCPServer,
        all_scores: List[Tuple[MCPServer, float]]
    ) -> str:
        """Build human-readable rationale for routing decision."""
        top_score = all_scores[0][1]
        second_score = all_scores[1][1] if len(all_scores) > 1 else 0
        
        return (
            f"Selected {selected_server.name} (score: {top_score:.2f}) for {task.phase} phase. "
            f"Health: {selected_server.health_score:.1%}, Load: {selected_server.current_load}/"
            f"{selected_server.max_concurrent_tasks}. "
            f"Margin over next option: {(top_score - second_score):.2f}. "
            f"Requires sync barrier: {self._needs_sync_barrier(task, selected_server)}"
        )
    
    def update_server_load(self, server_id: str, delta: int) -> None:
        """Update server load (positive for increment, negative for decrement)."""
        if server_id in self.mcp_servers:
            self.mcp_servers[server_id].current_load = max(
                0,
                self.mcp_servers[server_id].current_load + delta
            )
    
    def update_server_health(self, server_id: str, health_score: float) -> None:
        """Update server health score."""
        if server_id in self.mcp_servers:
            self.mcp_servers[server_id].health_score = max(0.0, min(1.0, health_score))
    
    def get_routing_report(self) -> Dict[str, Any]:
        """Generate routing statistics and performance report."""
        if not self.routing_history:
            return {"total_routes": 0, "servers": {}}
        
        server_stats = {}
        for server in self.mcp_servers.values():
            routed_tasks = [r for r in self.routing_history if r.mcp_server_id == server.id]
            server_stats[server.id] = {
                "name": server.name,
                "tasks_routed": len(routed_tasks),
                "current_load": server.current_load,
                "health_score": server.health_score,
                "avg_confidence": (
                    sum(r.confidence for r in routed_tasks) / len(routed_tasks)
                    if routed_tasks else 0.0
                )
            }
        
        return {
            "total_routes": len(self.routing_history),
            "servers": server_stats,
            "avg_confidence": sum(r.confidence for r in self.routing_history) / len(self.routing_history)
        }
    
    def export_routing_log(self, filepath: str) -> None:
        """Export routing history to JSON."""
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "total_routes": len(self.routing_history),
            "routes": [asdict(r) for r in self.routing_history],
            "servers": {
                sid: asdict(server) for sid, server in self.mcp_servers.items()
            }
        }
        with open(filepath, "w") as f:
            json.dump(log_data, f, indent=2)


# Example usage
if __name__ == "__main__":
    router = MCPRouter()
    
    # Register MCP servers
    router.register_mcp(MCPServer(
        id="mcp-fs-1",
        name="Filesystem MCP A1",
        capabilities=[MCPCapability.FILESYSTEM, MCPCapability.CODE_EXECUTION],
        endpoint="http://localhost:8001",
        max_concurrent_tasks=5
    ))
    
    router.register_mcp(MCPServer(
        id="mcp-db-1",
        name="Database MCP A4",
        capabilities=[MCPCapability.DATABASE, MCPCapability.MEMORY],
        endpoint="http://localhost:8002",
        max_concurrent_tasks=10
    ))
    
    # Route a task
    task = TaskDescriptor(
        id="task-001",
        agent_id="A1",
        phase="Embedding",
        required_capabilities=[MCPCapability.FILESYSTEM],
        priority=3
    )
    
    decision = router.route_task(task)
    print(f"Routed to: {decision.mcp_server_id}")
    print(f"Confidence: {decision.confidence:.2%}")
    print(f"Rationale: {decision.rationale}")
    print(f"Sync barrier required: {decision.sync_barrier_required}")
