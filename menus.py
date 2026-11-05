from datos import codigos, nombres_alumnos, guardar_en_archivo
from operaciones import registrar_alumno, buscar_registro, borrar_registro

def menu_registros():
    while True:
        print("\n--- MENÚ DE REGISTROS ---")
        if not codigos: print("No hay registros almacenados.")
        else:
            for i, c in enumerate(codigos): print(f"{i+1}. {c} - {nombres_alumnos[i]}")
        print("-------------------------")
        print("1. Volver al menú principal\n2. Buscar / Gestionar registro\n3. Borrar registro")
        op = input("Opción (1-3): ").strip()
        if op == "1": break
        elif op == "2": buscar_registro(); input("\nPresione Enter...")
        elif op == "3": borrar_registro(); input("\nPresione Enter...")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE MATRÍCULA ===")
        print("1. Crear registro\n2. Ver / Buscar registros\n3. Guardar en Bloc de Notas\n4. Salir")
        op = input("Seleccione opción (1-4): ").strip()
        if op == "1": registrar_alumno(); input("\nPresione Enter...")
        elif op == "2": menu_registros()
        elif op == "3": 
            _, msg = guardar_en_archivo()
            print(msg)
            input("\nPresione Enter...")
        elif op == "4": print("Saliendo del sistema..."); break