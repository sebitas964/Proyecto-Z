import almacenamiento
import busqueda
import codigos
import ingreso


def mostrar_menu():
    print("\nMESA DE PARTES DIGITAL - MAT-Z")
    print("1. Registrar solicitud")
    print("2. Buscar expediente por código")
    print("3. Mostrar expedientes ordenados por código")
    print("4. Mostrar todos los expedientes")
    print("5. Salir")


def registrar_solicitud():
    print("\nREGISTRO DE SOLICITUD")

    registro = ingreso.pedir_datos()

    registro["codigo"] = codigos.generar_codigo(
        almacenamiento.leer_registros()
    )

    if almacenamiento.guardar_registro(registro):
        print("\nSolicitud registrada correctamente.")
        busqueda.mostrar_resultado(registro)
    else:
        print("\nNo se pudo registrar la solicitud.")


def mostrar_solicitudes(registros):
    if not registros:
        print("\nNo hay expedientes registrados.")
        return

    print(
        f"\n{'CÓDIGO':<11}{'APELLIDOS':<22}{'NOMBRES':<22}"
        f"{'DNI':<10}{'TELÉFONO':<12}{'DOCUMENTO':<13}{'GRADO'}"
    )

    for registro in registros:
        grado = (
            f"{registro['nivel']} "
            f"{registro['grado']}-{registro['seccion']}"
        )

        print(
            f"{registro['codigo']:<11}"
            f"{registro['apellidos']:<22}"
            f"{registro['nombres']:<22}"
            f"{registro['dni']:<10}"
            f"{registro['telefono']:<12}"
            f"{registro['tipo_documento']:<13}"
            f"{grado}"
        )


def main():
    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == "1":
            registrar_solicitud()

        elif opcion == "2":
            codigo = input(
                "\nCódigo del expediente (ejemplo MAT-00001): "
            ).strip()

            registro = busqueda.buscar_por_codigo(
                almacenamiento.leer_registros(),
                codigo
            )

            print()
            busqueda.mostrar_resultado(registro)

        elif opcion == "3":
            registros = almacenamiento.leer_registros()
            registros_ordenados = codigos.ordenar_registros(registros)
            mostrar_solicitudes(registros_ordenados)

        elif opcion == "4":
            registros = almacenamiento.leer_registros()
            mostrar_solicitudes(registros)

        elif opcion == "5":
            print("\nHasta pronto.")
            break

        else:
            print("\nOpción no válida. Ingrese un número del 1 al 5.")


if __name__ == "__main__":
    main()
