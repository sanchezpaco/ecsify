"""
Basic CLI tests
"""

from unittest.mock import patch

from click.testing import CliRunner

from ecsify.cli import main


def test_cli_import():
    """Test that CLI module can be imported"""

    assert main is not None


def test_version_command():
    """Test version command functionality"""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])

    output = result.output.lower()

    assert result.exit_code == 0
    assert "ecsify" in output
    assert "version" in output
    assert "version" in output


class TestValidateCommandBehavior:
    """Test validate command behaviour"""

    class TestWhenYamlIsValid:
        """When the given YAML file is valid"""

        @patch("ecsify.cli.validate_config")
        @patch("ecsify.cli.load_yaml_file")
        def test_it_should_pass_validation(self, mock_yaml_parser, validator_mock):
            """It should pass validation"""
            mock_yaml_parser.return_value = {"services": {}}
            validator_mock.return_value = True

            runner = CliRunner()
            result = runner.invoke(main, ["validate"])

            output = result.output.lower()

            assert result.exit_code == 0
            assert "configuration is valid" in output

    class TestWhenYamlDoesNotExist:
        """When the given YAML file does not exist"""

        def test_it_should_return_file_not_found_error(self):
            """It should return file not found error and exit with code 1"""

            runner = CliRunner()
            result = runner.invoke(main, ["validate", "-f", "nonexistent.yaml"])

            output = result.output.lower()

            assert result.exit_code != 0
            assert "file not found" in output

    class TestWhenYamlIsInvalid:
        """When the given YAML file is invalid"""

        @patch("ecsify.cli.load_yaml_file")
        def test_it_should_return_validation_error(self, mock_yaml_parser):
            """It should return validation error"""
            mock_yaml_parser.return_value = {"services": {}}

            runner = CliRunner()
            result = runner.invoke(main, ["validate"])

            output = result.output.lower()

            assert result.exit_code != 0
            assert "validation failed" in output
