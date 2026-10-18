
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

def validar_tipo_documento(tipo):
    """Comprueba que el tipo de trámite sea válido."""
    if not campo_obligatorio(tipo):
        return False

    tipos_validos = {
        "matrícula",
        "vacante",
        "certificado",
        "constancia"
    }

    return tipo.strip().casefold() in tipos_validos
