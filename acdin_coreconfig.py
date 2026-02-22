"""
Configuration management for ACDIN with rigorous validation and environment handling.
Uses Pydantic for robust type validation and environment variable parsing.
"""

import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from enum import Enum

from pydantic import Field, validator, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl, SecretStr

# Initialize logging early for configuration debugging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Environment(str, Enum):
    """Environment types for different deployment contexts"""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class ACDINConfig(BaseSettings):
    """
    Central configuration for ACDIN with comprehensive validation.
    All environment variables use ACDIN_ prefix for isolation.
    """
    
    model_config = SettingsConfigDict(
        env_prefix="ACDIN_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"  # Ignore extra env vars to prevent injection attacks
    )
    
    # Core Settings
    environment: Environment = Field(
        default=Environment.DEVELOPMENT,
        description="Runtime environment"
    )
    node_id: str = Field(
        default_factory=lambda: f"node_{os.urandom(4).hex()}",
        description="Unique identifier for this ACDIN node"
    )
    
    # Firebase Configuration (CRITICAL - per mission constraints)
    firebase_project_id: str = Field(
        ...,  # Required field
        description="Firebase project ID for Firestore/Realtime DB"
    )
    firebase_credentials_path: Optional[Path] = Field(
        None,
        description="Path to Firebase service account JSON file"
    )
    firestore_collection_prefix: str = Field(
        default="acdin_",
        description="Prefix for Firestore collections"
    )
    
    # Network & Communication
    api_host: str = Field(
        default="0.0.0.0",
        description="Host for API server"
    )
    api_port: int = Field(
        default=8000,
        ge=1024,  # Must be >= 1024 (non-privileged ports)
        le=65535,  # Must be <= 65535
        description="Port for API server"
    )
    
    # Module Discovery
    discovery_poll_interval_seconds: int = Field(
        default=30,
        ge=5,  # Minimum 5 seconds for rate limiting
        description="Interval for module discovery polling"
    )
    heartbeat_timeout_seconds: int = Field(
        default=120,
        ge=30,
        description="Timeout for module heartbeat detection"
    )
    
    # Emergent Synthesis