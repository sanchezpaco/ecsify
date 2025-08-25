"""
CLI entrypoint for ECSify
"""

import click
from rich.console import Console
from rich.panel import Panel

from ecsify.utils.logger import get_logger

console = Console()
logger = get_logger(__name__)


@click.group()
@click.version_option(version="0.1.0", prog_name="ecsify")
@click.pass_context
def main(ctx: click.Context) -> None:
    """
    ECSify - A CLI tool to simplify deployment of containers to AWS ECS

    ECSify abstracts ECS complexity while keeping the process GitOps-friendly,
    minimal, and practical.
    """
    ctx.ensure_object(dict)


@main.command()
@click.option("--dry-run", is_flag=True, help="Show deployment plan without executing")
@click.option("--env", help="Environment configuration to use (dev, staging, prod)")
@click.option("--service", help="Deploy only a specific service")
@click.option("--file", help="Custom configuration file to use")
@click.option("--json", is_flag=True, help="Output in JSON format for automation")
def apply(dry_run: bool, env: str, service: str, file: str, json: bool) -> None:
    """Deploy services to AWS ECS"""

    if json:
        result = {
            "status": "success",
            "message": "Hello from ECSify!",
            "dry_run": dry_run,
        }
        click.echo(str(result).replace("'", '"'))
        return

    console.print(
        Panel(
            "[bold green]🚀 ECSify Hello World![/bold green]\n\n"
            f"[cyan]Dry run:[/cyan] {dry_run}\n"
            f"[cyan]Environment:[/cyan] {env or 'default'}\n"
            f"[cyan]Service:[/cyan] {service or 'all'}\n"
            f"[cyan]File:[/cyan] {file or 'ecsify.yaml'}\n\n"
            "[yellow]This is a scaffolding version. "
            "Full implementation coming soon![/yellow]",
            title="ECSify Apply Command",
            border_style="green",
        )
    )

    logger.info("Apply command executed successfully")


@main.command()
def version() -> None:
    """Show ECSify version"""
    console.print("[bold blue]ECSify version 0.1.0[/bold blue]")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
