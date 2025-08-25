"""
Configuration validation using Pydantic models
"""

from typing import Dict, Any

from ecsify.models.config import ECSifyConfig
from ecsify.utils.exceptions import ValidationError
from ecsify.utils.logger import get_logger

logger = get_logger(__name__)


def validate_config(config_data: Dict[str, Any]) -> ECSifyConfig:
    """
    Validate configuration data against Pydantic models

    Args:
        config_data: Raw configuration dictionary

    Returns:
        Validated ECSifyConfig instance

    Raises:
        ValidationError: If validation fails
    """
    try:
        config = ECSifyConfig.model_validate(config_data)
        logger.info("Configuration validation passed")
        return config
    except Exception as e:
        raise ValidationError(f"Configuration validation failed: {e}") from e
