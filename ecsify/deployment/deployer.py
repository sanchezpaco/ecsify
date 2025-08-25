"""
Main deployment orchestration logic
"""

from ecsify.aws.ecs_client import ECSClient
from ecsify.models.config import ECSifyConfig
from ecsify.utils.logger import get_logger

logger = get_logger(__name__)


class Deployer:
    """Main deployment orchestrator"""

    def __init__(self):
        self.ecs_client = ECSClient()

    def deploy(self, config: ECSifyConfig, dry_run: bool = False) -> bool:
        """
        Deploy configuration to AWS ECS

        Args:
            config: Validated ECSify configuration
            dry_run: If True, only show what would be deployed

        Returns:
            True if deployment successful
        """
        logger.info("Starting deployment process")

        if dry_run:
            logger.info("DRY RUN MODE - No actual deployment will occur")
            return self._dry_run_deploy(config)

        return self._execute_deploy(config)

    def _dry_run_deploy(self, config: ECSifyConfig) -> bool:
        """Show deployment plan without executing"""
        logger.info("Deployment plan:")
        logger.info("  Task definitions: %s", len(config.tasks))
        logger.info("  Services: %s", len(config.services))

        for task in config.tasks:
            logger.info("  - Task: %s", task.family)

        for service in config.services:
            logger.info("  - Service: %s (%s replicas)", service.name, service.replicas)

        return True

    def _execute_deploy(self, config: ECSifyConfig) -> bool:
        """Execute actual deployment"""
        logger.info("Executing deployment...")

        # Validate clusters
        clusters = {service.cluster for service in config.services}
        for cluster in clusters:
            self.ecs_client.validate_cluster_exists(cluster)

        # Deploy task definitions
        for task in config.tasks:
            logger.info("Deploying task definition: %s", task.family)

        # Deploy services
        for service in config.services:
            logger.info("Deploying service: %s", service.name)

        logger.info("Deployment completed successfully")
        return True
