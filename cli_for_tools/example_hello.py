import os
import typer

app = typer.Typer(help="Awesome CLI user manager.")


def clean_data_when_use_yolo():
    os.system("sudo chown --recursive $USER:$USER .")
    os.system("rm --force --recursive raw")
    os.system("rm --force --recursive resized")


@app.command()
def say_hi(name: str):
    print(f"Hello {name}")


@app.command()
def good_bye(name: str = "Chato"):
    print(f"Good bye {name}")
