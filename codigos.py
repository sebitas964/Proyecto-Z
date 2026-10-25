
# codigos.py
# Generación de códigos, validación, almacenamiento y ordenamiento.

import os
import re

ARCHIVO = "registros.txt"
PREFIJO = "MAT-"

CAMPOS = [
    "codigo", "nombres", "apellidos", "dni",
    "telefono", "nivel", "grado", "seccion"
]


def validar_texto(valor, campo):
    """Permite letras, tildes, ñ y espacios."""
    valor = valor.strip()

    if not valor:
        raise ValueError(f"El campo {campo} es obligatorio.")

    if not all(c.isalpha() or c.isspace() for c in valor):
        raise ValueError(
            f"{campo} solo admite letras y espacios."
        )

    return " ".join(valor.split())


def validar_registro(registro):
    """Valida los datos antes de guardar un registro."""

    registro["nombres"] = validar_texto(
        registro["nombres"], "nombres"
    )
    registro["apellidos"] = validar_texto(
        registro["apellidos"], "apellidos"
    )

    dni = registro["dni"].strip()
    if not re.fullmatch(r"\d{8}", dni):
        raise ValueError("El DNI debe contener exactamente 8 dígitos.")
    registro["dni"] = dni

    telefono = registro["telefono"].strip()
    if not re.fullmatch(r"9\d{8}", telefono):
        raise ValueError(
            "El teléfono debe tener 9 dígitos y comenzar con 9."
        )
    registro["telefono"] = telefono

    nivel = registro["nivel"].strip().capitalize()
    if nivel not in ("Primaria", "Secundaria"):
        raise ValueError(
            "El nivel debe ser Primaria o Secundaria."
        )
    registro["nivel"] = nivel

    grado = str(registro["grado"]).strip()
    limite = 6 if nivel == "Primaria" else 5

    if not re.fullmatch(r"\d+", grado):
        raise ValueError("El grado debe ser un número entero.")

    if not 1 <= int(grado) <= limite:
        raise ValueError(
            f"El grado de {nivel} debe estar entre 1 y {limite}."
        )
    registro["grado"] = str(int(grado))

    seccion = registro["seccion"].strip().upper()
    if seccion not in ("A", "B", "C"):
        raise ValueError("La sección debe ser A, B o C.")
    registro["seccion"] = seccion

    # Evita campos vacíos y el separador del archivo.
    for campo in CAMPOS[1:]:
        valor = str(registro[campo])
        if not valor.strip() or "|" in valor:
            raise ValueError(f"El campo {campo} no es válido.")

    return registro


def cargar_registros():
    """Lee los registros guardados en el archivo TXT."""
    registros = []

    if not os.path.exists(ARCHIVO):
        return registros

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            linea = linea.rstrip("\n")

            if not linea:
                continue

            campos = linea.split("|")

            if len(campos) != len(CAMPOS):
                raise ValueError(
                    f"Formato incorrecto en la línea {numero}."
                )

            registro = dict(zip(CAMPOS, campos))
            validar_registro(registro)

            if not re.fullmatch(
                r"MAT-\d{5,}", registro["codigo"]
            ):
                raise ValueError(
                    f"Código incorrecto en la línea {numero}."
                )

            if any(
                r["codigo"] == registro["codigo"]
                for r in registros
            ):
                raise ValueError(
                    f"Código duplicado: {registro['codigo']}"
                )

            registros.append(registro)

    return registros


def generar_codigo(registros=None):
    """
    Genera el siguiente código disponible.
    Consulta el archivo para conservar la secuencia
    incluso después de cerrar y volver a abrir el programa.
    """
    if registros is None:
        registros = cargar_registros()

    mayor = 0

    for registro in registros:
        coincidencia = re.fullmatch(
            r"MAT-(\d{5,})", registro["codigo"]
        )
        if coincidencia:
            mayor = max(mayor, int(coincidencia.group(1)))

    return f"{PREFIJO}{mayor + 1:05d}"


def guardar_registro(registro):
    """Valida y guarda un registro sin duplicar códigos."""
    registros = cargar_registros()

    validar_registro(registro)

    if any(r["codigo"] == registro.get("codigo")
           for r in registros):
        raise ValueError("El código ya existe.")

    if not registro.get("codigo"):
        registro["codigo"] = generar_codigo(registros)

    # Comprueba nuevamente el código asignado.
    if any(r["codigo"] == registro["codigo"]
           for r in registros):
        raise ValueError("El código ya existe.")

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        linea = "|".join(registro[c] for c in CAMPOS)
        archivo.write(linea + "\n")

    return registro["codigo"]


def ordenar_registros(registros, criterio="apellidos"):
    """
    Ordena los registros por apellido, nombres, DNI,
    código, nivel, grado o sección.
    """
    criterios_validos = {
        "codigo", "nombres", "apellidos", "dni",
        "nivel", "grado", "seccion"
    }

    if criterio not in criterios_validos:
        raise ValueError(
            f"Criterio inválido. Use: {criterios_validos}"
        )

    if criterio == "grado":
        return sorted(
            registros,
            key=lambda r: (
                r["nivel"],
                int(r["grado"]),
                r["seccion"],
                r["apellidos"].casefold(),
                r["nombres"].casefold()
            )
        )

    return sorted(
        registros,
        key=lambda r: r[criterio].casefold()
    )


if __name__ == "__main__":
    print("SISTEMA DE REGISTRO DE MATRÍCULA")

    try:
        nuevo = {
            "codigo": "",
            "nombres": input("Nombres: "),
            "apellidos": input("Apellidos: "),
            "dni": input("DNI: "),
            "telefono": input("Teléfono: "),
            "nivel": input("Nivel (Primaria/Secundaria): "),
            "grado": input("Grado: "),
            "seccion": input("Sección (A/B/C): ")
        }

        codigo = guardar_registro(nuevo)
        print(f"\nRegistro guardado correctamente: {codigo}")

        print("\nREGISTROS ORDENADOS POR APELLIDOS")
        for registro in ordenar_registros(
            cargar_registros(), "apellidos"
        ):
            print(
                registro["codigo"],
                registro["apellidos"],
                registro["nombres"]
            )

    except (ValueError, KeyError) as error:
        print(f"Error: {error}")
