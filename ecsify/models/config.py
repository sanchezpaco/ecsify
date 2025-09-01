"""
Configuration models for ECSify
"""

from typing import List

from pydantic import BaseModel, ConfigDict

from ecsify.models.service import ServiceDefinition
from ecsify.models.task import TaskDefinition


class ECSifyConfig(BaseModel):
    """Root configuration model for ECSify YAML files"""

    model_config = ConfigDict(extra="forbid")

    tasks: List[TaskDefinition]
    services: List[ServiceDefinition]
