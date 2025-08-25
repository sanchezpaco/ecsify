"""
Custom exception classes for ECSify
"""


class ECSifyError(Exception):
    """Base exception for all ECSify errors"""


class ValidationError(ECSifyError):
    """YAML validation or configuration error"""


class AWSError(ECSifyError):
    """AWS API or authentication error"""


class DeploymentError(ECSifyError):
    """Deployment process failure"""


class DeploymentTimeoutError(ECSifyError):
    """Deployment timeout"""
