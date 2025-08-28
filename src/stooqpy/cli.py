"""Console script for stooqpy."""

import typer
from rich.console import Console

from . import config

# from stooqpy import utils

app = typer.Typer()
console = Console()


@app.command(help="Inicjuje pliki konfiguracyjne w Dokumentach")
def init_config():
    config.initialize_config()


if __name__ == "__main__":
    app()

    # console.print("Replace this message by putting your code into "
    #            "stooqpy.cli.main")
    # console.print("See Typer documentation at https://typer.tiangolo.com/")
    # # utils.do_something_useful()
