from datetime import date

TIPOS_DOCUMENTO = {
    "matricula": "Matrícula",
    "vacante": "Vacante",
    "certificado": "Certificado",
    "constancia": "Constancia",
}


def campo_obligatorio(valor):
    return valor is not None and bool(str(valor).strip())


def validar_nombre(nombre):
    if not campo_obligatorio(nombre):
        return False

    palabras = str(nombre).strip().split()

    return all(palabra.isalpha() for palabra in palabras)


def validar_dni(dni):
    if not campo_obligatorio(dni):
        return False

    dni = str(dni).strip()

    return (
        len(dni) == 8
        and dni.isascii()
        and dni.isdigit()
    )


def validar_telefono(telefono):
    if not campo_obligatorio(telefono):
        return False

    telefono = str(telefono).strip()

    return (
        len(telefono) == 9
        and telefono.isascii()
        and telefono.isdigit()
        and telefono.startswith("9")
    )


def normalizar_tipo_documento(tipo):
    if not campo_obligatorio(tipo):
        return None

    clave = str(tipo).strip().casefold().replace("í", "i")

    return TIPOS_DOCUMENTO.get(clave)


def validar_tipo_documento(tipo):
    return normalizar_tipo_documento(tipo) is not None


def normalizar_nivel(nivel):
    if not campo_obligatorio(nivel):
        return None

    niveles = {
        "primaria": "Primaria",
        "secundaria": "Secundaria",
    }

    return niveles.get(str(nivel).strip().casefold())


def validar_grado(grado, nivel):
    nivel = normalizar_nivel(nivel)

    if nivel is None or not campo_obligatorio(grado):
        return False

    grado = str(grado).strip()

    if not (grado.isascii() and grado.isdigit()):
        return False

    grado = int(grado)

    if nivel == "Primaria":
        return 1 <= grado <= 6

    return 1 <= grado <= 5


def validar_seccion(seccion):
    if not campo_obligatorio(seccion):
        return False

    return str(seccion).strip().upper() in ("A", "B", "C")


def validar_anio_escolar(anio):
    if not campo_obligatorio(anio):
        return False

    anio = str(anio).strip()

    if not (anio.isascii() and anio.isdigit()):
        return False

    anio = int(anio)
    anio_actual = date.today().year

    return anio_actual <= anio <= anio_actual + 1