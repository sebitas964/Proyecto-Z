
# almacenamiento.py

ARCHIVO = "registros.txt"


def guardar_registro(registro, archivo=ARCHIVO):
    """Guarda un registro sin borrar los anteriores."""
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(registro + "\n")
        return True
    except OSError as error:
        print(f"Error al guardar: {error}")
        return False


def leer_registros(archivo=ARCHIVO):
    """Lee los registros guardados."""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [linea.rstrip("\n") for linea in f if linea.strip()]
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"Error al leer: {error}")
        return []


if __name__ == "__main__":
    guardar_registro("001,Juan,20")
    guardar_registro("002,Ana,22")

    print("Registros guardados:")
    for registro in leer_registros():
        print(registro)
