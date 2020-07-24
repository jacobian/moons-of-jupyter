import click
import os
import subprocess
import sys


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

class ProcessHopesShattered(Exception):
    pass


def optimistic_run(description, arguments):
    result = subprocess.run(arguments, capture_output=True, text=True)
    if result.returncode != 0:
        raise ProcessHopesShattered(description, result)


@cli.command()
@click.argument(
    "environment",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, allow_dash=False),
)
@click.option("-n", "--name", help="Human-readable name for this environment")
# This option should not really be needed, but it is useful when debugging.
@click.option("-j", "--jupyter", help="Which Jupyter installation to add to")
def add(environment, name, jupyter):
    """
    Add a Python environment, which can be a virtualenv, Pipenv/Poetry directory,
    or python interpreter
    """
    if name is None:
        name = os.path.basename(environment)
        if name == "": # Allow trailing / because of shell completion
            name = os.path.basename(os.path.dirname(environment))
    if jupyter is None:
        jupyter = "jupyter"
    venv_python = os.path.join(environment, "bin", "python")
    try:
        optimistic_run("install ipykernel",
                       [venv_python, "-m", "pip", "install", "ipykernel"])
        logical_name = f"{name}-venv"
        optimistic_run("create ipykernel description",
                       [venv_python, "-m", "ipykernel", "install",
                                     "--name", logical_name,
                                     "--display-name", name,
                                     "--prefix", environment])
        description = os.path.join(environment, "share", "jupyter", "kernels",
                                   logical_name)
        optimistic_run("add ipykernel description to jupyter",
                       [jupyter, "kernelspec", "install", description,
                        "--sys-prefix",])
    except ProcessHopesShattered as exc:
        stage, details = exc.args
        print("Commands to f{stage} failed:")
        print("Output:")
        sys.stdout.write(details.stdout)
        print("Error:")
        sys.stdout.write(details.stderr)
    print(f"✅ added {environment} as {name} to {jupyter}")


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
