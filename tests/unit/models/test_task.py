"""
Unit tests for task definition models
"""

import pytest
from pydantic import ValidationError

from ecsify.models.task import ContainerSpec, TaskDefinition


class TestContainerSpecBehavior:
    """Test ContainerSpec behaviors"""

    class TestWhenCreatingWithValidData:
        """When the given container data is valid"""

        def test_it_should_succeed(self):
            """It should succeed"""
            valid_data = {
                "name": "web",
                "image": "nginx:latest",
                "port": 80,
                "cpu": 256,
                "memory": 512,
            }

            container = ContainerSpec(**valid_data)

            assert container.name == "web"
            assert container.image == "nginx:latest"
            assert container.cpu == 256

    class TestWhenMissingRequiredField:
        """When a required field (name) is missing"""

        def test_it_should_raise_validation_error(self):
            """It should raise ValidationError"""
            invalid_data = {
                # "name" is missing
                "image": "nginx:latest",
                "port": 80,
                "cpu": 256,
                "memory": 512,
            }

            with pytest.raises(ValidationError) as exc_info:
                ContainerSpec(**invalid_data)

            errors = exc_info.value.errors()

            assert any(
                error["loc"] == ("name",) and error["type"] == "missing"
                for error in errors
            )

    class TestWhenOmitingOptionalFields:
        """When optional fields are omitted"""

        def test_it_should_use_defaults(self):
            """It should use default values"""
            minimal_data = {
                "name": "web",
                "image": "nginx:latest",
            }

            container = ContainerSpec(**minimal_data)

            assert container.port == 80
            assert container.cpu == 256
            assert container.memory == 512
            assert container.command is None
            assert container.env is None

    class TestWhenCreatingWithIncorrectData:
        """When the given container data is invalid"""

        class TestWhenCPUIsBelowMinimum:
            """When CPU is below minimum"""

            def test_it_should_raise_validation_error(self):
                """It should raise ValidationError"""
                invalid_data = {
                    "name": "web",
                    "image": "nginx:latest",
                    "port": 80,
                    "cpu": 64,  # Invalid: less than minimum
                    "memory": 512,
                }

                with pytest.raises(ValidationError) as exc_info:
                    ContainerSpec(**invalid_data)

                errors = exc_info.value.errors()

                assert any(
                    error["loc"] == ("cpu",) and error["type"] == "greater_than_equal"
                    for error in errors
                )

        class TestWhenMemoryIsBelowMinimum:
            """When Memory is below minimum"""

            def test_it_should_raise_validation_error(self):
                """It should raise ValidationError"""
                invalid_data = {
                    "name": "web",
                    "image": "nginx:latest",
                    "port": 80,
                    "cpu": 256,
                    "memory": 64,  # Invalid: less than minimum
                }

                with pytest.raises(ValidationError) as exc_info:
                    ContainerSpec(**invalid_data)

                errors = exc_info.value.errors()

                assert any(
                    error["loc"] == ("memory",)
                    and error["type"] == "greater_than_equal"
                    for error in errors
                )


class TestTaskDefinitionBehavior:
    """Test TaskDefinition behaviors"""

    class TestWhenCreatingWithValidData:
        """When the given task definition data is valid"""

        def test_it_should_succeed(self):
            """It should succeed"""
            valid_data = {
                "family": "my-task-family",
                "container": {
                    "name": "web",
                    "image": "nginx:latest",
                    "port": 80,
                    "cpu": 256,
                    "memory": 512,
                },
                "execution_role_arn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
                "task_role_arn": "arn:aws:iam::123456789012:role/myTaskRole",
            }

            task_def = TaskDefinition(**valid_data)

            assert task_def.family == "my-task-family"
            assert task_def.container.name == "web"
            assert (
                task_def.execution_role_arn
                == "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
            )

    class TestWhenMissingRequiredField:
        """When a required field (family) is missing"""

        def test_it_should_raise_validation_error(self):
            """It should raise ValidationError"""
            invalid_data = {
                # "family" is missing
                "container": {
                    "name": "web",
                    "image": "nginx:latest",
                    "port": 80,
                    "cpu": 256,
                    "memory": 512,
                },
                "execution_role_arn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
            }

            with pytest.raises(ValidationError) as exc_info:
                TaskDefinition(**invalid_data)

            errors = exc_info.value.errors()

            assert any(
                error["loc"] == ("family",) and error["type"] == "missing"
                for error in errors
            )
