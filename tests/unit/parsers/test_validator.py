"""
Unit tests for config validator
"""

import pytest

from ecsify.parsers.validator import ECSifyConfig
from ecsify.utils.exceptions import ValidationError


class TestECSifyConfigValidation:
    """Test ECSifyConfig Validation behaviors"""

    class TestWhenGivenValidConfig:
        """When the given config is valid"""

        def test_it_should_succeed(self):
            """It should succeed"""

            valid_config = {
                "tasks": [
                    {
                        "family": "web-task",
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
                ],
                "services": [
                    {
                        "name": "web",
                        "cluster": "default",
                        "replicas": 2,
                        "task_family": "web-task",
                    }
                ],
            }

            config = ECSifyConfig.model_validate(valid_config)

            assert len(config.tasks) == 1
            assert config.tasks[0].family == "web-task"
            assert len(config.services) == 1
            assert config.services[0].name == "web"

    class TestWhenGivenInvalidConfig:
        """When the given config is invalid"""

        def test_it_should_fail(self):
            """It should fail"""

            valid_config = {
                "tasks": [
                    {
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
                ],
                "services": [
                    {
                        "name": "web",
                        "cluster": "default",
                        "replicas": 2,
                        "task_family": "web-task",
                    }
                ],
            }

            with pytest.raises(ValidationError) as exc_info:
                ECSifyConfig.model_validate(valid_config)

            errors = exc_info.value.errors()

            assert any(
                error["loc"] == ("tasks", 0, "family") and error["type"] == "missing"
                for error in errors
            )
