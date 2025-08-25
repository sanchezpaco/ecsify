"""
Dry-run plan generation
"""

from ecsify.models.config import ECSifyConfig
from ecsify.utils.logger import get_logger

logger = get_logger(__name__)


def generate_deployment_plan(config: ECSifyConfig) -> dict:
    """
    Generate deployment plan for dry-run

    Args:
        config: ECSify configuration

    Returns:
        Deployment plan dictionary
    """
    plan = {
        "task_definitions": [
            {
                "family": task.family,
                "image": task.container.image,
                "cpu": task.container.cpu,
                "memory": task.container.memory,
                "action": "register",
            }
            for task in config.tasks
        ],
        "services": [
            {
                "name": service.name,
                "cluster": service.cluster,
                "replicas": service.replicas,
                "task_family": service.task_family,
                "action": "create_or_update",
            }
            for service in config.services
        ],
    }

    logger.info("Deployment plan generated successfully")
    return plan
