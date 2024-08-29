import click
from wqp import __version__

print(f"Version imported is : {__version__}")

@click.group()
#@click.version_option(version='1.0.0')  # Adds the --version option to the CLI
@click.version_option(__version__)  # Adds the --version option to the CLI
def cli():
    """The main CLI group."""
    pass

@cli.group()
def data():
    """Subcommand group for data operations."""
    pass


@data.command()
@click.option('--data-path', type=click.Path(exists=True), required=True, help='Path to the data file.')
def cli_command(data_path):
    """Print the value of the provided data path."""
    click.echo(f"Data path is: {data_path}")

if __name__ == '__main__':
    cli()

