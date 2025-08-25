"""
Service definition models
"""

from pydantic import BaseModel, Field


class ServiceDefinition(BaseModel):
    """ECS Service configuration"""

    name: str = Field(..., min_length=1)
    cluster: str = Field(..., min_length=1)
    replicas: int = Field(default=1, ge=1)
    task_family: str = Field(..., min_length=1)

    class Config:
        extra = "forbid"
