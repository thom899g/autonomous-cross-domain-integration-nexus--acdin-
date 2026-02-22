"""
ACDIN Core Package - Autonomous Cross-Domain Integration Nexus

Provides the foundational systems for emergent collective intelligence
across diverse AI modules.
"""

__version__ = "0.1.0"
__author__ = "ACDIN Collective"
__license__ = "Proprietary"

from .config import ACDINConfig, get_config
from .module import AIModule, ModuleCapability, ModuleStatus
from .registry import ModuleRegistry
from .communication import MessageBroker, Message, MessageType
from .emergent_synthesizer import EmergentCapabilitySynthesizer
from .meta_reasoning import MetaReasoningEngine
from .memory import CollectiveMemorySystem
from .skill_composition import DynamicSkillComposer
from .logging import ACDINLogger

__all__ = [
    "ACDINConfig",
    "get_config",
    "AIModule",
    "ModuleCapability",
    "ModuleStatus",
    "ModuleRegistry",
    "MessageBroker",
    "Message",
    "MessageType",
    "EmergentCapabilitySynthesizer",
    "MetaReasoningEngine",
    "CollectiveMemorySystem",
    "DynamicSkillComposer",
    "ACDINLogger",
]