"""
AWS authentication and credentials handling
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

from ecsify.utils.exceptions import AWSError
from ecsify.utils.logger import get_logger

logger = get_logger(__name__)


def get_aws_session() -> boto3.Session:
    """
    Get AWS session with current credentials

    Returns:
        Boto3 session instance

    Raises:
        AWSError: If credentials not found or invalid
    """
    try:
        session = boto3.Session()
        # Test credentials by making a simple call
        sts = session.client("sts")
        identity = sts.get_caller_identity()
        logger.info("AWS credentials verified successfully")
        logger.debug("AWS Account: %s", identity.get("Account"))
        return session
    except NoCredentialsError as e:
        raise AWSError("AWS credentials not found") from e
    except ClientError as e:
        raise AWSError(f"AWS authentication failed: {e}") from e
