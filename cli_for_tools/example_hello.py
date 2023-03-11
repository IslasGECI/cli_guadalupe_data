import typer

app = typer.Typer(help="Awesome CLI user manager.")


@app.command()
def main(name: str):
    print(f"Hello {name}")

