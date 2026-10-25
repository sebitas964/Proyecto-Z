import random

def guardar_solicitud(nombres, dni, telefono, datos_matricula, codigo):
    print(f"Datos procesados para: {nombres}")

def sistema_matricula():
    codigos = []
    nombres_alumnos = []
    dnis = []
    telefonos = []
    niveles = []
    
    while True:
        print("\n" * 2)
        print("========================================")
        print("    SISTEMA DE SOLICITUD DE MATRÍCULA   ")
        print("========================================")
        print("1. Crear registro")
        print("2. Ver registros")
        print("3. Guardar registros en Bloc de Notas")
        print("4. Salir")
        
        seleccion = input("Seleccione una opción (1-4): ").strip()
        
        if seleccion == "1":
            print("\n--- NUEVO REGISTRO DE MATRÍCULA ---")
            nombres = input("Ingrese nombres y apellidos: ").strip()
            dni = input("Ingrese DNI: ").strip()
            telefono = input("Ingrese teléfono: ").strip()
            
            print("Seleccione el Nivel / Grado de Matrícula:")
            print("1. Inicial")
            print("2. Primaria")
            print("3. Secundaria")
            opcion_matricula = input("Elija opción (1-3): ").strip()
            
            if opcion_matricula == "1":
                datos_matricula = "Inicial"
            elif opcion_matricula == "2":
                datos_matricula = "Primaria"
            elif opcion_matricula == "3":
                datos_matricula = "Secundaria"
            else:
                datos_matricula = ""
                
            if not nombres or not dni or not telefono or not datos_matricula:
                print("Error: Debe completar todos los campos correctamente.")
            elif len(dni) != 8 or not dni.isdigit():
                print("Error: DNI inválido (debe tener exactamente 8 dígitos numéricos).")
            elif dni in dnis:
                print("Error: El DNI del estudiante es idéntico al de otro estudiante.")
            elif len(telefono) != 9 or not telefono.isdigit():
                print("Error: Teléfono inválido (debe tener exactamente 9 dígitos numéricos).")
            else:
                while True:
                    numero_azar = random.randint(10000, 99999)
                    codigo_nuevo = f"MAT-{numero_azar}"
                    
                    if codigo_nuevo not in codigos:
                        break
                
                codigos.append(codigo_nuevo)
                nombres_alumnos.append(nombres)
                dnis.append(dni)
                telefonos.append(telefono)
                niveles.append(datos_matricula)
                
                guardar_solicitud(nombres, dni, telefono, datos_matricula, codigo_nuevo)
                
                print("----------------------------------------")
                print("Solicitud registrada correctamente.")
                print(f"Nivel seleccionado: {datos_matricula}")
                print(f"Código asignado   : {codigo_nuevo}")
                print("----------------------------------------")
            
            input("\nPresione Enter para continuar...")
                
        elif seleccion == "2":
            while True:
                print("\n" * 2)
                print("========================================")
                print("         MENÚ DE REGISTROS              ")
                print("========================================")
                
                if len(codigos) == 0:
                    print("No hay registros almacenados actualmente.")
                else:
                    for i in range(len(codigos)):
                        print(f"{i + 1}. Código: {codigos[i]} | Estudiante: {nombres_alumnos[i]}")
                
                print("----------------------------------------")
                print("1. Volver al menú principal")
                print("2. Buscar un registro por código")
                print("3. Borrar un registro por código")
                print("========================================")
                
                sub_seleccion = input("Seleccione una opción (1-3): ").strip()
                
                if sub_seleccion == "1":
                    break
                
                elif sub_seleccion == "2":
                    print("\n" * 2)
                    print("========================================")
                    print("           BUSCAR REGISTRO              ")
                    print("========================================")
                    busqueda = input("Ingrese el código completo o parcial (ej. MAT-12345 o 67): ").strip().upper()
                    
                    print("----------------------------------------")
                    # 1. Si encuentra una coincidencia exacta de inmediato, entra directo al menú de acciones
                    if busqueda in codigos:
                        indice = codigos.index(busqueda)
                        while True:
                            print("\n========================================")
                            print("          ACCIONES DEL REGISTRO          ")
                            print("========================================")
                            print(f"Código    : {codigos[indice]}")
                            print(f"Estudiante: {nombres_alumnos[indice]}")
                            print(f"DNI       : {dnis[indice]}")
                            print(f"Teléfono  : {telefonos[indice]}")
                            print(f"Grado     : {niveles[indice]}")
                            print("----------------------------------------")
                            print("1. Cambiar nombre")
                            print("2. Cambiar DNI")
                            print("3. Cambiar teléfono")
                            print("4. Cambiar de grado")
                            print("5. Eliminar el registro")
                            print("6. Volver al menú de registros")
                            print("========================================")
                            
                            opcion_accion = input("Seleccione una opción (1-6): ").strip()
                            
                            if opcion_accion == "1":
                                nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ").strip()
                                if nuevo_nombre:
                                    nombres_alumnos[indice] = nuevo_nombre
                                    print("¡Nombre actualizado correctamente!")
                                else:
                                    print("Error: El nombre no puede estar vacío.")
                                input("\nPresione Enter para continuar...")
                                
                            elif opcion_accion == "2":
                                nuevo_dni = input("Ingrese el nuevo DNI (8 dígitos): ").strip()
                                if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
                                    if nuevo_dni in dnis and nuevo_dni != dnis[indice]:
                                        print("Error: El DNI del estudiante es idéntico al de otro estudiante.")
                                    else:
                                        dnis[indice] = nuevo_dni
                                        print("¡DNI actualizado correctamente!")
                                else:
                                    print("Error: DNI inválido (debe tener exactamente 8 dígitos numéricos).")
                                input("\nPresione Enter para continuar...")
                                
                            elif opcion_accion == "3":
                                nuevo_tel = input("Ingrese el nuevo teléfono (9 dígitos): ").strip()
                                if len(nuevo_tel) == 9 and nuevo_tel.isdigit():
                                    telefonos[indice] = nuevo_tel
                                    print("¡Teléfono actualizado correctamente!")
                                else:
                                    print("Error: Teléfono inválido (debe tener exactamente 9 dígitos numéricos).")
                                input("\nPresione Enter para continuar...")
                                
                            elif opcion_accion == "4":
                                print("Seleccione el nuevo Nivel / Grado de Matrícula:")
                                print("1. Inicial")
                                print("2. Primaria")
                                print("3. Secundaria")
                                op_niv = input("Elija opción (1-3): ").strip()
                                if op_niv == "1":
                                    niveles[indice] = "Inicial"
                                    print("¡Grado actualizado a Inicial!")
                                elif op_niv == "2":
                                    niveles[indice] = "Primaria"
                                    print("¡Grado actualizado a Primaria!")
                                elif op_niv == "3":
                                    niveles[indice] = "Secundaria"
                                    print("¡Grado actualizado a Secundaria!")
                                else:
                                    print("Error: Opción de grado no válida.")
                                input("\nPresione Enter para continuar...")
                                
                            elif opcion_accion == "5":
                                eliminado_nombre = nombres_alumnos.pop(indice)
                                codigos.pop(indice)
                                dnis.pop(indice)
                                telefonos.pop(indice)
                                niveles.pop(indice)
                                print(f"Registro de '{eliminado_nombre}' eliminado exitosamente.")
                                input("\nPresione Enter para continuar...")
                                break
                                
                            elif opcion_accion == "6":
                                break
                            else:
                                print("Opción no válida.")
                                input("\nPresione Enter para continuar...")
                    else:
                        # 2. Si no es exacto, busca coincidencias parciales
                        coincidencias = []
                        for idx, c in enumerate(codigos):
                            if busqueda in c:
                                coincidencias.append(idx)
                        
                        if len(coincidencias) == 1:
                            indice = coincidencias[0]
                            while True:
                                print("\n========================================")
                                print("          ACCIONES DEL REGISTRO          ")
                                print("========================================")
                                print(f"Código    : {codigos[indice]}")
                                print(f"Estudiante: {nombres_alumnos[indice]}")
                                print(f"DNI       : {dnis[indice]}")
                                print(f"Teléfono  : {telefonos[indice]}")
                                print(f"Grado     : {niveles[indice]}")
                                print("----------------------------------------")
                                print("1. Cambiar nombre")
                                print("2. Cambiar DNI")
                                print("3. Cambiar teléfono")
                                print("4. Cambiar de grado")
                                print("5. Eliminar el registro")
                                print("6. Volver al menú de registros")
                                print("========================================")
                                
                                opcion_accion = input("Seleccione una opción (1-6): ").strip()
                                
                                if opcion_accion == "1":
                                    nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ").strip()
                                    if nuevo_nombre:
                                        nombres_alumnos[indice] = nuevo_nombre
                                        print("¡Nombre actualizado correctamente!")
                                    else:
                                        print("Error: El nombre no puede estar vacío.")
                                    input("\nPresione Enter para continuar...")
                                    
                                elif opcion_accion == "2":
                                    nuevo_dni = input("Ingrese el nuevo DNI (8 dígitos): ").strip()
                                    if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
                                        if nuevo_dni in dnis and nuevo_dni != dnis[indice]:
                                            print("Error: El DNI del estudiante es idéntico al de otro estudiante.")
                                        else:
                                            dnis[indice] = nuevo_dni
                                            print("¡DNI actualizado correctamente!")
                                    else:
                                        print("Error: DNI inválido (debe tener exactamente 8 dígitos numéricos).")
                                    input("\nPresione Enter para continuar...")
                                    
                                elif opcion_accion == "3":
                                    nuevo_tel = input("Ingrese el nuevo teléfono (9 dígitos): ").strip()
                                    if len(nuevo_tel) == 9 and nuevo_tel.isdigit():
                                        telefonos[indice] = nuevo_tel
                                        print("¡Teléfono actualizado correctamente!")
                                    else:
                                        print("Error: Teléfono inválido (debe tener exactamente 9 dígitos numéricos).")
                                    input("\nPresione Enter para continuar...")
                                    
                                elif opcion_accion == "4":
                                    print("Seleccione el nuevo Nivel / Grado de Matrícula:")
                                    print("1. Inicial")
                                    print("2. Primaria")
                                    print("3. Secundaria")
                                    op_niv = input("Elija opción (1-3): ").strip()
                                    if op_niv == "1":
                                        niveles[indice] = "Inicial"
                                        print("¡Grado actualizado a Inicial!")
                                    elif op_niv == "2":
                                        niveles[indice] = "Primaria"
                                        print("¡Grado actualizado a Primaria!")
                                    elif op_niv == "3":
                                        niveles[indice] = "Secundaria"
                                        print("¡Grado actualizado a Secundaria!")
                                    else:
                                        print("Error: Opción de grado no válida.")
                                    input("\nPresione Enter para continuar...")
                                    
                                elif opcion_accion == "5":
                                    eliminado_nombre = nombres_alumnos.pop(indice)
                                    codigos.pop(indice)
                                    dnis.pop(indice)
                                    telefonos.pop(indice)
                                    niveles.pop(indice)
                                    print(f"Registro de '{eliminado_nombre}' eliminado exitosamente.")
                                    input("\nPresione Enter para continuar...")
                                    break
                                    
                                elif opcion_accion == "6":
                                    break
                                else:
                                    print("Opción no válida.")
                                    input("\nPresione Enter para continuar...")
                                    
                        elif len(coincidencias) > 1:
                            print("--- RESULTADOS SIMILARES ---")
                            for idx, real_idx in enumerate(coincidencias):
                                print(f"{idx + 1}. Código: {codigos[real_idx]} | Estudiante: {nombres_alumnos[real_idx]}")
                            print("----------------------------------------")
                            elegir_simil = input("Ingrese el número del registro que desea seleccionar (o presione Enter para volver): ").strip()
                            
                            if elegir_simil.isdigit():
                                num_elegido = int(elegir_simil)
                                if 1 <= num_elegido <= len(coincidencias):
                                    indice = coincidencias[num_elegido - 1]
                                    while True:
                                        print("\n========================================")
                                        print("          ACCIONES DEL REGISTRO          ")
                                        print("========================================")
                                        print(f"Código    : {codigos[indice]}")
                                        print(f"Estudiante: {nombres_alumnos[indice]}")
                                        print(f"DNI       : {dnis[indice]}")
                                        print(f"Teléfono  : {telefonos[indice]}")
                                        print(f"Grado     : {niveles[indice]}")
                                        print("----------------------------------------")
                                        print("1. Cambiar nombre")
                                        print("2. Cambiar DNI")
                                        print("3. Cambiar teléfono")
                                        print("4. Cambiar de grado")
                                        print("5. Eliminar el registro")
                                        print("6. Volver al menú de registros")
                                        print("========================================")
                                        
                                        opcion_accion = input("Seleccione una opción (1-6): ").strip()
                                        
                                        if opcion_accion == "1":
                                            nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ").strip()
                                            if nuevo_nombre:
                                                nombres_alumnos[indice] = nuevo_nombre
                                                print("¡Nombre actualizado correctamente!")
                                            else:
                                                print("Error: El nombre no puede estar vacío.")
                                            input("\nPresione Enter para continuar...")
                                            
                                        elif opcion_accion == "2":
                                            nuevo_dni = input("Ingrese el nuevo DNI (8 dígitos): ").strip()
                                            if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
                                                if nuevo_dni in dnis and nuevo_dni != dnis[indice]:
                                                    print("Error: El DNI del estudiante es idéntico al de otro estudiante.")
                                                else:
                                                    dnis[indice] = nuevo_dni
                                                    print("¡DNI actualizado correctamente!")
                                            else:
                                                print("Error: DNI inválido (debe tener exactamente 8 dígitos numéricos).")
                                            input("\nPresione Enter para continuar...")
                                            
                                        elif opcion_accion == "3":
                                            nuevo_tel = input("Ingrese el nuevo teléfono (9 dígitos): ").strip()
                                            if len(nuevo_tel) == 9 and nuevo_tel.isdigit():
                                                telefonos[indice] = nuevo_tel
                                                print("¡Teléfono actualizado correctamente!")
                                            else:
                                                print("Error: Teléfono inválido (debe tener exactamente 9 dígitos numéricos).")
                                            input("\nPresione Enter para continuar...")
                                            
                                        elif opcion_accion == "4":
                                            print("Seleccione el nuevo Nivel / Grado de Matrícula:")
                                            print("1. Inicial")
                                            print("2. Primaria")
                                            print("3. Secundaria")
                                            op_niv = input("Elija opción (1-3): ").strip()
                                            if op_niv == "1":
                                                niveles[indice] = "Inicial"
                                                print("¡Grado actualizado a Inicial!")
                                            elif op_niv == "2":
                                                niveles[indice] = "Primaria"
                                                print("¡Grado actualizado a Primaria!")
                                            elif op_niv == "3":
                                                niveles[indice] = "Secundaria"
                                                print("¡Grado actualizado a Secundaria!")
                                            else:
                                                print("Error: Opción de grado no válida.")
                                            input("\nPresione Enter para continuar...")
                                            
                                        elif opcion_accion == "5":
                                            eliminado_nombre = nombres_alumnos.pop(indice)
                                            codigos.pop(indice)
                                            dnis.pop(indice)
                                            telefonos.pop(indice)
                                            niveles.pop(indice)
                                            print(f"Registro de '{eliminado_nombre}' eliminado exitosamente.")
                                            input("\nPresione Enter para continuar...")
                                            break
                                            
                                        elif opcion_accion == "6":
                                            break
                                        else:
                                            print("Opción no válida.")
                                            input("\nPresione Enter para continuar...")
                        else:
                            print(f"Error: No se encontró ningún registro similar a '{busqueda}'.")
                    print("----------------------------------------")
                    
                    input("\nPresione Enter para regresar al menú de registros...")
                    
                elif sub_seleccion == "3":
                    print("\n" * 2)
                    print("========================================")
                    print("           BORRAR REGISTRO              ")
                    print("========================================")
                    busqueda = input("Ingrese el código completo o parcial a borrar (ej. 67): ").strip().upper()
                    
                    print("----------------------------------------")
                    if busqueda in codigos:
                        indice = codigos.index(busqueda)
                        eliminado = nombres_alumnos.pop(indice)
                        codigos.pop(indice)
                        dnis.pop(indice)
                        telefonos.pop(indice)
                        niveles.pop(indice)
                        print(f"¡Éxito! El registro de '{eliminado}' fue eliminado.")
                    else:
                        coincidencias = []
                        for idx, c in enumerate(codigos):
                            if busqueda in c:
                                coincidencias.append(idx)
                                
                        if len(coincidencias) == 1:
                            indice = coincidencias[0]
                            eliminado = nombres_alumnos.pop(indice)
                            codigos.pop(indice)
                            dnis.pop(indice)
                            telefonos.pop(indice)
                            niveles.pop(indice)
                            print(f"¡Éxito! El registro de '{eliminado}' fue eliminado.")
                        elif len(coincidencias) > 1:
                            print("--- RESULTADOS SIMILARES PARA BORRAR ---")
                            for idx, real_idx in enumerate(coincidencias):
                                print(f"{idx + 1}. Código: {codigos[real_idx]} | Estudiante: {nombres_alumnos[real_idx]}")
                            print("----------------------------------------")
                            elegir_simil = input("Ingrese el número del registro que desea eliminar: ").strip()
                            
                            if elegir_simil.isdigit():
                                num_elegido = int(elegir_simil)
                                if 1 <= num_elegido <= len(coincidencias):
                                    indice = coincidencias[num_elegido - 1]
                                    eliminado = nombres_alumnos.pop(indice)
                                    codigos.pop(indice)
                                    dnis.pop(indice)
                                    telefonos.pop(indice)
                                    niveles.pop(indice)
                                    print(f"¡Éxito! El registro de '{eliminado}' fue eliminado.")
                                else:
                                    print("Error: Número de selección inválido.")
                            else:
                                print("Error: Entrada no válida.")
                        else:
                            print(f"Error: No se encontró ningún registro similar a '{busqueda}'.")
                    print("----------------------------------------")
                    
                    input("\nPresione Enter para regresar al menú de registros...")
                else:
                    print("Opción no válida. Intente nuevamente.")
                    input("\nPresione Enter para continuar...")
                    
        elif seleccion == "3":
            # Opción para guardar en un bloc de notas (archivo .txt)
            print("\n--- GUARDAR REGISTROS EN BLOC DE NOTAS ---")
            if len(codigos) == 0:
                print("No hay registros para guardar.")
            else:
                try:
                    with open("registros_matricula.txt", "w", encoding="utf-8") as archivo:
                        archivo.write("========================================\n")
                        archivo.write("    REPORTE DE REGISTROS DE MATRÍCULA   \n")
                        archivo.write("========================================\n\n")
                        for i in range(len(codigos)):
                            archivo.write(f"Registro {i + 1}\n")
                            archivo.write(f"Código    : {codigos[i]}\n")
                            archivo.write(f"Estudiante: {nombres_alumnos[i]}\n")
                            archivo.write(f"DNI       : {dnis[i]}\n")
                            archivo.write(f"Teléfono  : {telefonos[i]}\n")
                            archivo.write(f"Grado     : {niveles[i]}\n")
                            archivo.write("----------------------------------------\n")
                    print("¡Registros guardados exitosamente en el archivo 'registros_matricula.txt'!")
                except Exception as e:
                    print(f"Error al guardar el archivo: {e}")
            input("\nPresione Enter para continuar...")

        elif seleccion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    sistema_matricula()