import click


@click.group()
def cli():
    pass


@cli.command(short_help="Cálcula la distribución posterior para el tamaño de la población inicial")
@click.option("--name", "-n", type=str, help="Nombre del recurso csv")
def main(**arguments):
    name = arguments["name"]
    print(f"Hello {name}")
