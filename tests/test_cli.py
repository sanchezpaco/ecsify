"""
Basic CLI tests
"""

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


def test_validate_command():
    """Test validate command functionality"""
    runner = CliRunner()
    result = runner.invoke(main, ["validate", "--help"])

    output = result.output.lower()

    assert result.exit_code == 0
    assert "ecsify" in output
    assert "version" in output
    assert "version" in output
