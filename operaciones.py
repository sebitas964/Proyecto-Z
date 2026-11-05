import random
from datos import codigos, nombres_alumnos, dnis, telefonos, niveles, guardar_solicitud

def registrar_alumno():
    print("\n--- NUEVO REGISTRO ---")
    nom, dni, tel = input("Nombre Completo: ").strip(), input("DNI (8 dígitos): ").strip(), input("Teléfono (9 dígitos): ").strip()
    grados = {"1": "Inicial", "2": "Primaria", "3": "Secundaria"}
    grado = grados.get(input("Grado:\n1. Inicial\n2. Primaria\n3. Secundaria\nSeleccione opción (1-3): ").strip(), "")
    
    if not all([nom, dni, tel, grado]) or len(dni)!=8 or not dni.isdigit() or len(tel)!=9 or not tel.isdigit():
        print("Error: Datos incompletos o formatos inválidos.")
    elif dni in dnis:
        print("Error: El DNI ya está registrado.")
    else:
        while True:
            code = f"MAT-{random.randint(10000, 99999)}"
            if code not in codigos: break
        codigos.append(code); nombres_alumnos.append(nom); dnis.append(dni); telefonos.append(tel); niveles.append(grado)
        guardar_solicitud(nom, dni, tel, grado, code)
        print(f"¡Registrado! Código: {code}")

def gestionar_acciones(idx):
    while True:
        print(f"\n[Registro] \nCódigo: {codigos[idx]} \nEstudiante: {nombres_alumnos[idx]} \nDNI: {dnis[idx]} \nTel: {telefonos[idx]} \nGrado: {niveles[idx]}")
        op = input("1. Cambiar Nombre\n2. Cambiar DNI\n3. Cambiar Teléfono\n4. Cambiar Grado\n5. Eliminar\n6. Volver\nOpción: ").strip()
        if op == "1":
            v = input("Nuevo nombre: ").strip()
            if v: nombres_alumnos[idx] = v; print("¡Actualizado!")
        elif op == "2":
            v = input("Nuevo DNI (8 dígitos): ").strip()
            if len(v)==8 and v.isdigit() and (v not in dnis or v == dnis[idx]): dnis[idx] = v; print("¡Actualizado!")
            else: print("DNI inválido o repetido.")
        elif op == "3":
            v = input("Nuevo teléfono (9 dígitos): ").strip()
            if len(v)==9 and v.isdigit(): telefonos[idx] = v; print("¡Actualizado!")
            else: print("Teléfono inválido.")
        elif op == "4":
            g = {"1": "Inicial", "2": "Primaria", "3": "Secundaria"}.get(input("1. Inicial\n2. Primaria\n3. Secundaria\nSeleccione opción (1-3): ").strip())
            if g: niveles[idx] = g; print("¡Actualizado!")
        elif op == "5":
            n = nombres_alumnos.pop(idx); codigos.pop(idx); dnis.pop(idx); telefonos.pop(idx); niveles.pop(idx)
            print(f"Eliminado: {n}"); break
        elif op == "6": break
        input("\nPresione Enter...")

def buscar_registro():
    busq = input("Ingrese código completo o parcial: ").strip().upper()
    if busq in codigos:
        gestionar_acciones(codigos.index(busq))
    else:
        matches = [i for i, c in enumerate(codigos) if busq in c]
        if len(matches) == 1: gestionar_acciones(matches[0])
        elif len(matches) > 1:
            for i, m in enumerate(matches, 1): print(f"{i}. {codigos[m]} - {nombres_alumnos[m]}")
            sel = input("Seleccione número: ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(matches): gestionar_acciones(matches[int(sel)-1])
        else: print("No se encontró coincidencia.")

def borrar_registro():
    busq = input("Ingrese código exacto a borrar: ").strip().upper()
    if busq in codigos:
        i = codigos.index(busq)
        print(f"Eliminado: {nombres_alumnos.pop(i)}")
        codigos.pop(i); dnis.pop(i); telefonos.pop(i); niveles.pop(i)
    else: print("Código no encontrado.")