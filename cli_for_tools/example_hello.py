import typer

app = typer.Typer(help="Awesome CLI user manager.")


@app.command()
def main(name: str):
    print(f"Hello {name}")


@app.command()
def good_bye(name: str = "Chato"):
    print(f"adios {name}")
