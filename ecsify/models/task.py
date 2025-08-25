"""
Task definition models
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ContainerSpec(BaseModel):
    """Container specification within a task definition"""

    model_config = ConfigDict(extra="forbid")

    name: str
    image: str
    port: int = 80
    cpu: int = Field(default=256, ge=128)
    memory: int = Field(default=512, ge=128)
    command: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None


class TaskDefinition(BaseModel):
    """ECS Task Definition configuration"""

    model_config = ConfigDict(extra="forbid")

    family: str = Field(..., min_length=1)
    container: ContainerSpec
    execution_role_arn: Optional[str] = None
    task_role_arn: Optional[str] = None
