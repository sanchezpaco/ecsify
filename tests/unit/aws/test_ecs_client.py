"""
Unit tests for ECS client
"""

import os
from typing import Iterator

import pytest
from moto import mock_aws

from ecsify.aws.ecs_client import AWSError, ECSClient


class TestECSClient:
    """Test ECSClient behaviors"""

    @pytest.fixture(scope="module", autouse=True)
    def aws_credentials(self) -> None:
        """Mocked AWS Credentials for moto."""
        os.environ["AWS_ACCESS_KEY_ID"] = "testing"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
        os.environ["AWS_SECURITY_TOKEN"] = "testing"
        os.environ["AWS_SESSION_TOKEN"] = "testing"
        os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

    @pytest.fixture(scope="function", autouse=True)
    def mocked_aws(self) -> Iterator[None]:
        """
        Mock all AWS interactions
        Requires you to create your own boto3 clients
        """
        with mock_aws():
            yield

    @pytest.fixture(scope="function")
    def ecs_client(self) -> ECSClient:
        """Create ECSClient instance within mock context"""
        return ECSClient()

    class TestValidateClusterExists:
        """When validating an ECS cluster"""

        @pytest.fixture(scope="function")
        def mock_ecs_cluster(self, ecs_client):
            """Create a mock ECS cluster for testing"""

            ecs_client.ecs.create_cluster(clusterName="a-cluster")
            return ecs_client

        class TestWhenClusterExists:
            """When the cluster exists"""

            def test_it_should_succeed_for_existing_cluster(
                self, ecs_client, mock_ecs_cluster
            ):
                """It should succeed for existing cluster"""

                result = ecs_client.validate_cluster_exists("a-cluster")

                assert result is True

        class TestWhenClusterDoesNotExist:
            """When the cluster does not exist"""

            def test_it_should_fail_for_nonexistent_cluster(self, ecs_client):
                """It should fail for nonexistent cluster"""

                result = ecs_client.validate_cluster_exists("a-non-existent-cluster")

                assert result is False
