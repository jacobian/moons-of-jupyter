import click


@click.group()
@click.version_option()
def cli():
    """Manage a Moons of Jupyter installation."""


@cli.command()
def start():
    """Start Jupyter"""
    print("✨ running on http://notreally/")


@cli.command()
def stop():
    """Stop Jupyter"""
    print("🔥 server stopped")


@cli.command()
@click.argument(
    "environment",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, allow_dash=False),
)
@click.option("-n", "--name", help="Human-readable name for this environment")
def add(environment, name):
    """
    Add a Python environment, which can be a virtualenv, Pipenv/Poetry directory,
    or python interpreter
    """
    print(f"✅ added {environment}")


@cli.command()
@click.argument("environment_or_name")
def remove(environment_or_name):
    """Remove an environment (by path or name)"""
    print(f"🔥 removed {environment_or_name}")


@cli.command()
@click.argument("onoff", default="on", type=click.Choice(["on", "off"]))
def autostart(onoff):
    """Turn on/off automatically running at startup."""
    if onoff == "on":
        print(f"✅ moj will run on startup")
    else:
        print(f"🔥 moj will no longer start automatically")
