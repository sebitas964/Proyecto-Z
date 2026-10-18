
from datetime import date

def campo_obligatorio(valor):
    """Comprueba que un campo no esté vacío."""
    return valor is not None and bool(str(valor).strip())

def validar_nombre(nombre):
    """Acepta letras, tildes, ñ y espacios."""
    if not campo_obligatorio(nombre):
        return False

    palabras = nombre.strip().split()
    return all(palabra.isalpha() for palabra in palabras)


def validar_dni(dni):
    """Comprueba que el DNI tenga exactamente 8 dígitos."""
    dni = str(dni).strip()
    return len(dni) == 8 and dni.isdigit()


def validar_telefono(telefono):
    """Comprueba que tenga 9 dígitos y comience con 9."""
    telefono = str(telefono).strip()
    return (
        len(telefono) == 9
        and telefono.isdigit()
        and telefono.startswith("9")
    )


def normalizar_nivel(nivel):
    """Devuelve el nivel con escritura uniforme o None si no es válido."""
    if not campo_obligatorio(nivel):
        return None

    niveles = {
        "primaria": "Primaria",
        "secundaria": "Secundaria"
    }

    return niveles.get(str(nivel).strip().casefold())


def validar_grado(grado, nivel):
    """Comprueba que el grado corresponda al nivel educativo."""
    nivel_normalizado = normalizar_nivel(nivel)

    if nivel_normalizado is None:
        return False

    try:
        grado = int(grado)
    except (ValueError, TypeError):
        return False

    if nivel_normalizado == "Primaria":
        return 1 <= grado <= 6

    return 1 <= grado <= 5


def validar_seccion(seccion):
    """Acepta las secciones A, B y C, sin distinguir mayúsculas."""
    if not campo_obligatorio(seccion):
        return False

    return str(seccion).strip().upper() in ("A", "B", "C")


def validar_anio_escolar(anio):
    """Acepta el año actual o el siguiente."""
    try:
        anio = int(anio)
    except (ValueError, TypeError):
        return False

    anio_actual = date.today().year
    return anio in (anio_actual, anio_actual + 1)
