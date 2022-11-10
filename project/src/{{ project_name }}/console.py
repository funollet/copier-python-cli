import click
from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The project that does nothing (useful)"""
    click.echo("Nothing done.")
