# =============================================================================
# PROYECTO Z - MENÚ PRINCIPAL E INTEGRACIÓN
# Integrante: Sebastián
# =============================================================================

import re

# --- FUNCIONES DE VALIDACIÓN (RESTRICCIONES) ---
def validar_obligatorio(texto):
    return len(texto.strip()) > 0

def validar_nombre(texto):
    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    return bool(re.match(patron, texto)) and validar_obligatorio(texto)

def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 9 and telefono.startswith("9")

def validar_nivel_y_grado(nivel, grado):
    if nivel not in ["Primaria", "Secundaria"]:
        return False
    if not grado.isdigit():
        return False
    num_grado = int(grado)
    if nivel == "Primaria" and (1 <= num_grado <= 6):
        return True
    if nivel == "Secundaria" and (1 <= num_grado <= 5):
        return True
    return False

def validar_seccion(seccion):
    seccion_mayus = seccion.upper().strip()
    if seccion_mayus in ["A", "B", "C"]:
        return seccion_mayus
    return None

# --- MENÚ PRINCIPAL ---
def mostrar_menu():
    print("\n" + "="*35)
    print("      SISTEMA DE GESTIÓN MAT-Z      ")
    print("="*35)
    print("1. Registrar nuevo alumno")
    print("2. Buscar alumno por DNI")
    print("3. Generar reportes / Listados")
    print("4. Otras opciones del sistema")
    print("5. Salir del programa")
    print("="*35)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n[Módulo de Registro - En construcción por tu compañero]")
        elif opcion == "2":
            print("\n[Módulo de Búsqueda - En construcción por tu compañero]")
        elif opcion == "3":
            print("\n[Módulo de Reportes - En construcción por tu compañero]")
        elif opcion == "4":
            print("\n[Módulo Adicional - En construcción por tu compañero]")
        elif opcion == "5":
            print("\n¡Gracias por usar el Sistema Proyecto Z! Saliendo...")
            break
        else:
            print("\n❌ Opción no válida. Por favor, digite un número entre 1 y 5.")

if __name__ == "__main__":
    main()
