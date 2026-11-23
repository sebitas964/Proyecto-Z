import validaciones


def pedir_dato(mensaje, validar, error):
    while True:
        valor = input(mensaje).strip()

        if validar(valor):
            return valor

        print(error)


def pedir_datos():
    nombres = pedir_dato(
        "Nombres: ",
        validaciones.validar_nombre,
        "Error: solo se permiten letras y espacios."
    )

    apellidos = pedir_dato(
        "Apellidos: ",
        validaciones.validar_nombre,
        "Error: solo se permiten letras y espacios."
    )

    dni = pedir_dato(
        "DNI (8 dígitos): ",
        validaciones.validar_dni,
        "Error: el DNI debe tener exactamente 8 dígitos."
    )

    telefono = pedir_dato(
        "Teléfono (9 dígitos, empieza con 9): ",
        validaciones.validar_telefono,
        "Error: el teléfono debe tener 9 dígitos y empezar con 9."
    )

    documento = pedir_dato(
        "Documento (Matrícula/Vacante/Certificado/Constancia): ",
        validaciones.validar_tipo_documento,
        "Error: tipo de documento no válido."
    )

    nivel = pedir_dato(
        "Nivel (Primaria/Secundaria): ",
        lambda n: validaciones.normalizar_nivel(n) is not None,
        "Error: escriba Primaria o Secundaria."
    )

    nivel = validaciones.normalizar_nivel(nivel)

    grado = pedir_dato(
        "Grado: ",
        lambda g: validaciones.validar_grado(g, nivel),
        "Error: grado no válido para ese nivel."
    )

    seccion = pedir_dato(
        "Sección (A/B/C): ",
        validaciones.validar_seccion,
        "Error: la sección debe ser A, B o C."
    )

    return {
        "nombres": " ".join(nombres.split()),
        "apellidos": " ".join(apellidos.split()),
        "dni": dni,
        "telefono": telefono,
        "tipo_documento": validaciones.normalizar_tipo_documento(
            documento
        ),
        "nivel": nivel,
        "grado": str(int(grado)),
        "seccion": seccion.upper(),
    }