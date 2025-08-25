"""
Unit tests for service models
"""

import pytest
from pydantic import ValidationError

from ecsify.models.service import ServiceDefinition


class TestServiceDefinitionBehavior:
    """Test ServiceDefinition behaviors"""

    class TestWhenCreatingWithValidData:
        """When the given service data is valid"""

        def test_it_should_succeed(self):
            """It should succeed"""
            valid_data = {
                "name": "my-service",
                "cluster": "my-cluster",
                "replicas": 2,
                "task_family": "my-task-family",
            }

            service = ServiceDefinition(**valid_data)

            assert service.name == "my-service"
            assert service.cluster == "my-cluster"
            assert service.replicas == 2
            assert service.task_family == "my-task-family"

    class TestWhenMissingRequiredField:
        """When a required field (name) is missing"""

        def test_it_should_raise_validation_error(self):
            """It should raise ValidationError"""
            invalid_data = {
                # "name" is missing
                "cluster": "my-cluster",
                "replicas": 2,
                "task_family": "my-task-family",
            }

            with pytest.raises(ValidationError) as exc_info:
                ServiceDefinition(**invalid_data)

            errors = exc_info.value.errors()

            assert any(
                error["loc"] == ("name",) and error["type"] == "missing"
                for error in errors
            )

    class TestWhenReplicasIsBelowMinimum:
        """When replicas is set below the minimum of 1"""

        def test_it_should_raise_validation_error(self):
            """It should raise ValidationError"""
            invalid_data = {
                "name": "my-service",
                "cluster": "my-cluster",
                "replicas": 0,  # Invalid, should be at least 1
                "task_family": "my-task-family",
            }

            with pytest.raises(ValidationError) as exc_info:
                ServiceDefinition(**invalid_data)

            errors = exc_info.value.errors()

            assert any(
                error["loc"] == ("replicas",) and error["type"] == "greater_than_equal"
                for error in errors
            )
