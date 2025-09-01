"""
Unit tests for Yaml parser
"""

import pytest

from ecsify.parsers.yaml_parser import load_yaml_file
from ecsify.utils.exceptions import ValidationError


class TestLoadYAMLFile:
    """Test Yaml Parser behaviors"""

    class TestWhenFileExistsAndIsValid:
        """When the given file exists and is valid"""

        def test_it_should_succeed(self, tmp_path):
            """It should succeed"""
            valid_yaml_content = """
            tasks:
              - family: web-task
                container:
                  name: web
                  image: nginx:latest
                  port: 80
                  cpu: 256
                  memory: 512
                execution_role_arn: arn:aws:iam::123456789012:role/ecsTaskExecutionRole
                task_role_arn: arn:aws:iam::123456789012:role/myTaskRole
            services:
              - name: web
                cluster: default
                replicas: 2
                task_family: web-task
            """

            yaml_file = tmp_path / "config.yaml"
            yaml_file.write_text(valid_yaml_content)

            result = load_yaml_file(str(yaml_file))

            assert "tasks" in result
            assert len(result["tasks"]) == 1

    class TestWhenFileDoesNotExist:
        """When the given file does not exist"""

        def test_it_should_raise_file_not_found_error(self):
            """It should raise ValidationError"""
            non_existent_file = "non_existent.yaml"

            with pytest.raises(FileNotFoundError) as exc_info:
                load_yaml_file(non_existent_file)

            assert (
                str(exc_info.value) == "Configuration file not found: non_existent.yaml"
            )

    class TestWhenFileIsInvalidYAML:
        """When the given file contains invalid YAML"""

        def test_it_should_raise_yaml_syntax_error(self, tmp_path):
            """It should raise ValidationError"""
            invalid_yaml_content = """
            tasks:
              - family: web-task
                container
                  name: web
                  image: nginx:latest
                  port: 80
                  cpu: 256
                  memory: 512
                execution_role_arn: arn:aws:iam::123456789012:role/ecsTaskExecutionRole
                task_role_arn: arn:aws:iam::123456789012:role/myTaskRole
            services:
              - name: web
                cluster: default
                replicas: 2
                task_family: web-task
            """

            yaml_file = tmp_path / "config.yaml"
            yaml_file.write_text(invalid_yaml_content)

            with pytest.raises(ValidationError) as exc_info:
                load_yaml_file(yaml_file)

            assert "YAML syntax error in" in str(exc_info.value)
