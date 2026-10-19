
# =============================================================================
# PROYECTO Z - MENU PRINCIPAL E INTEGRACION
# Integrante: Sebastian
# =============================================================================

import validaciones

# Lista temporal para guardar los alumnos durante la ejecucion
alumnos = []


# -----------------------------------------------------------------------------
# MENU PRINCIPAL
# -----------------------------------------------------------------------------

def mostrar_menu():
    print("\n" + "=" * 40)
    print("       SISTEMA DE GESTION MAT-Z")
    print("=" * 40)
    print("1. Registrar nuevo alumno")
    print("2. Buscar alumno por DNI")
    print("3. Generar reportes / Listados")
    print("4. Otras opciones del sistema")
    print("5. Salir del programa")
    print("=" * 40)


# -----------------------------------------------------------------------------
# FUNCION AUXILIAR PARA SOLICITAR DATOS OBLIGATORIOS
# -----------------------------------------------------------------------------

def pedir_dato(mensaje, funcion_validacion):
    while True:
        valor = input(mensaje).strip()

        if not validaciones.campo_obligatorio(valor):
            print("Error: este campo es obligatorio.")
            continue

        if funcion_validacion(valor):
            return valor

        print("Dato no valido. Intente nuevamente.")


# -----------------------------------------------------------------------------
# REGISTRO DE ALUMNOS
# -----------------------------------------------------------------------------

def registrar_alumno():
    print("\n--- REGISTRO DE NUEVO ALUMNO ---")

    nombre = pedir_dato(
        "Ingrese nombres y apellidos: ",
        validaciones.validar_nombre
    )

    dni = pedir_dato(
        "Ingrese DNI (8 digitos): ",
        validaciones.validar_dni
    )

    telefono = pedir_dato(
        "Ingrese telefono (9 digitos, empieza con 9): ",
        validaciones.validar_telefono
    )

    while True:
        nivel = input("Nivel (Primaria/Secundaria): ").strip()
        nivel_normalizado = validaciones.normalizar_nivel(nivel)

        if nivel_normalizado is not None:
            nivel = nivel_normalizado
            break

        print("Error: escriba Primaria o Secundaria.")

    while True:
        grado = input("Grado: ").strip()

        if validaciones.validar_grado(grado, nivel):
            grado = int(grado)
            break

        print("Grado no valido para el nivel seleccionado.")

    seccion = pedir_dato(
        "Seccion (A, B o C): ",
        validaciones.validar_seccion
    ).upper()

    alumno = {
        "nombre": nombre.strip(),
        "dni": dni,
        "telefono": telefono,
        "nivel": nivel,
        "grado": grado,
        "seccion": seccion
    }

    # Evitar registrar dos veces el mismo DNI en esta ejecucion
    for existente in alumnos:
        if existente["dni"] == dni:
            print("Error: ya existe un alumno con ese DNI.")
            return

    alumnos.append(alumno)

    print("\nAlumno registrado correctamente.")
    print(f"Nombre: {alumno['nombre']}")
    print(f"DNI: {alumno['dni']}")
    print(f"Nivel: {alumno['nivel']}")
    print(f"Grado y seccion: {alumno['grado']} - {alumno['seccion']}")


# -----------------------------------------------------------------------------
# BUSQUEDA DE ALUMNOS
# -----------------------------------------------------------------------------

def buscar_alumno():
    print("\n--- BUSQUEDA DE ALUMNO ---")
    dni = input("Ingrese el DNI que desea buscar: ").strip()

    if not validaciones.validar_dni(dni):
        print("Error: el DNI debe tener exactamente 8 digitos.")
        return

    for alumno in alumnos:
        if alumno["dni"] == dni:
            print("\nAlumno encontrado:")
            print(f"Nombre: {alumno['nombre']}")
            print(f"DNI: {alumno['dni']}")
            print(f"Telefono: {alumno['telefono']}")
            print(f"Nivel: {alumno['nivel']}")
            print(f"Grado: {alumno['grado']}")
            print(f"Seccion: {alumno['seccion']}")
            return

    print("No se encontro un alumno con ese DNI.")


# -----------------------------------------------------------------------------
# LISTADO DE ALUMNOS
# -----------------------------------------------------------------------------

def mostrar_alumnos():
    print("\n--- LISTADO DE ALUMNOS ---")

    if not alumnos:
        print("Todavia no hay alumnos registrados.")
        return

    for numero, alumno in enumerate(alumnos, start=1):
        print(
            f"{numero}. {alumno['nombre']} | DNI: {alumno['dni']} | "
            f"{alumno['nivel']} | {alumno['grado']} - {alumno['seccion']}"
        )


# -----------------------------------------------------------------------------
# OPCIONES ADICIONALES
# -----------------------------------------------------------------------------

def otras_opciones():
    print("\n--- OTRAS OPCIONES ---")
    print("Este modulo esta pendiente de integracion.")


# -----------------------------------------------------------------------------
# EJECUCION DEL PROGRAMA
# -----------------------------------------------------------------------------

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion == "1":
            registrar_alumno()

        elif opcion == "2":
            buscar_alumno()

        elif opcion == "3":
            mostrar_alumnos()

        elif opcion == "4":
            otras_opciones()

        elif opcion == "5":
            print("\nGracias por usar el Sistema Proyecto Z.")
            print("Hasta pronto.")
            break

        else:
            print("Opcion no valida. Ingrese un numero del 1 al 5.")


if __name__ == "__main__":
    main()
