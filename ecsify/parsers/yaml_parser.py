"""
YAML file parsing utilities
"""

from pathlib import Path
from typing import Dict, Any
import yaml

from ecsify.utils.exceptions import ValidationError
from ecsify.utils.logger import get_logger

logger = get_logger(__name__)


def load_yaml_file(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a YAML file

    Args:
        file_path: Path to the YAML file

    Returns:
        Parsed YAML content as dictionary

    Raises:
        ValidationError: If file not found or YAML syntax error
    """
    path = Path(file_path)

    if not path.exists():
        raise ValidationError(f"Configuration file not found: {file_path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = yaml.safe_load(file)
            logger.info(f"Successfully loaded YAML file: {file_path}")
            return content or {}
    except yaml.YAMLError as e:
        raise ValidationError(f"YAML syntax error in {file_path}: {e}")
    except Exception as e:
        raise ValidationError(f"Error reading file {file_path}: {e}")
