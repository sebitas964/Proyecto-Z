ARCHIVO = "registros.txt"
SEPARADOR = "|"

CAMPOS = [
    "codigo",
    "nombres",
    "apellidos",
    "dni",
    "telefono",
    "tipo_documento",
    "nivel",
    "grado",
    "seccion",
]


def convertir_registro(linea):
    valores = linea.strip().split(SEPARADOR)

    if len(valores) != len(CAMPOS):
        return None

    if not all(valor.strip() for valor in valores):
        return None

    return dict(zip(CAMPOS, valores))


def guardar_registro(registro):
    if not isinstance(registro, dict):
        print("Error: el registro debe ser un diccionario.")
        return False

    if not all(campo in registro for campo in CAMPOS):
        print("Error: el registro no contiene todos los campos.")
        return False

    valores = []

    for campo in CAMPOS:
        valor = registro[campo]

        if not isinstance(valor, str) or not valor.strip():
            print("Error: los campos deben contener texto y no estar vacíos.")
            return False

        if SEPARADOR in valor or "\n" in valor or "\r" in valor:
            print("Error: los datos contienen caracteres no permitidos.")
            return False

        valores.append(valor.strip())

    linea = SEPARADOR.join(valores)

    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(linea + "\n")

        return True

    except OSError as error:
        print(f"Error al guardar: {error}")
        return False


def leer_registros():
    registros = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):

                if not linea.strip():
                    continue

                registro = convertir_registro(linea)

                if registro is None:
                    print(
                        f"Línea {numero} ignorada: formato incorrecto."
                    )
                else:
                    registros.append(registro)

    except FileNotFoundError:
        pass

    except OSError as error:
        print(f"Error al leer: {error}")

    return registros
