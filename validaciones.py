from datetime import date

def campo_obligatorio(valor):
    """Comprueba que el campo no esté vacío."""
    return valor is not None and bool(str(valor).strip())

def validar_nombre(nombre):
    """Acepta letras, tildes, ñ y espacios."""
    if not campo_obligatorio(nombre):
        return False

    palabras = nombre.strip().split()
    return all(palabra.isalpha() for palabra in palabras)

def validar_dni(dni):
    """Comprueba que el DNI tenga exactamente ocho dígitos."""
    dni = str(dni).strip()
    return len(dni) == 8 and dni.isdigit()

def validar_telefono(telefono):
    """Comprueba que tenga nueve dígitos y comience con 9."""
    telefono = str(telefono).strip()
    return (
        len(telefono) == 9
        and telefono.isdigit()
        and telefono.startswith("9")
    )

def normalizar_nivel(nivel):
    """Acepta Primaria o Secundaria sin distinguir mayúsculas."""
    if not campo_obligatorio(nivel):
        return None

    niveles = {
        "primaria": "Primaria",
        "secundaria": "Secundaria"
    }

    return niveles.get(str(nivel).strip().casefold())

def validar_grado(grado, nivel):
    """Valida el grado según el nivel educativo."""
    nivel = normalizar_nivel(nivel)

    if nivel is None:
        return False

    try:
        grado = int(grado)
    except (ValueError, TypeError):
        return False

    if nivel == "Primaria":
        return 1 <= grado <= 6

    return 1 <= grado <= 5

def validar_seccion(seccion):
    """Acepta únicamente las secciones A, B y C."""
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

def validar_tipo_documento(tipo):
    """Acepta los tipos de trámite acordados."""
    if not campo_obligatorio(tipo):
        return False

    tipos_validos = {
        "matrícula",
        "matricula",
        "vacante",
        "certificado",
        "constancia"
    }

    tipo_normalizado = str(tipo).strip().casefold()
    return tipo_normalizado in tipos_validos