import os
import typer

app = typer.Typer(help="Awesome CLI user manager.")


def clean_data_when_use_yolo():
    os.system("sudo chown --recursive $USER:$USER .")
    os.system("rm --force --recursive raw")
    os.system("rm --force --recursive resized")


def clean_data_when_after_made_little_map():
    os.system("sudo chown --recursive $USER:$USER .")
    os.system("echo ¿Qué borraremos?")


def analyze_photo():
    command = "docker run -itv $PWD:/workdir/data/raw/photos -v $PWD:/workdir/data islasgeci/cat_recognition:latest make detection_with_yolo"
    os.system(command)


def make_data_map_of_traps_jpg():
    command = "docker run -v $PWD:/workdir/data islasgeci/ig_position_traps_map make data/map_of_traps.jpg"
    os.system(command)


@app.command()
def say_hi(name: str):
    print(f"Hello {name}")


@app.command()
def good_bye(name: str = "Chato"):
    print(f"Good bye {name}")


@app.command()
def haz_mapa():
    '''
    Hace un esbozo del mapa de Isla Guadalupe con las trampas activas e inactivas. \n
    Requerimiento: En la carpeta de trabajo debe estar: \n
    - IG_POSICION_{fecha}.txt         : Archivo que obtenemos de mapsource \n
    - IG_POSICION_TRAMPAS_{fecha}.xlsx: Archivos con los esfuerzos de la semana \n
    Al final generará el archivo `map_of_traps.jpg`.
    '''
    make_data_map_of_traps_jpg()
    clean_data_when_after_made_little_map()


@app.command()
def clasifica_fotos():
    '''
    Clasifica las fotos que vienen de las trampas cámara. \n
    Requerimiento: En la carpeta de trabajo debe estar una carpeta (varias carpetas) con las fotos. \n
    Al final generará una carpeta con las fotos en las que detectó gato.
    '''
    analyze_photo()
    clean_data_when_use_yolo()


if __name__ == "__main__":
    app()
