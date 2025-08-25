"""
Configuration models for ECSify
"""

from typing import List
from pydantic import BaseModel

from ecsify.models.task import TaskDefinition
from ecsify.models.service import ServiceDefinition


class ECSifyConfig(BaseModel):
    """Root configuration model for ECSify YAML files"""

    tasks: List[TaskDefinition]
    services: List[ServiceDefinition]

    class Config:
        extra = "forbid"
