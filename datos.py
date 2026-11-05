codigos, nombres_alumnos, dnis, telefonos, niveles = [], [], [], [], []

def guardar_solicitud(nombres, dni, telefono, grado, codigo):
    print(f"Datos procesados para: {nombres}")

def guardar_en_archivo():
    if not codigos: return False, "No hay registros para guardar."
    try:
        with open("registros_matricula.txt", "w", encoding="utf-8") as f:
            f.write("=== REPORTE DE MATRÍCULAS ===\n\n")
            for i, c in enumerate(codigos):
                f.write(f"[{i+1}] Código: {c} | Estudiante: {nombres_alumnos[i]} | DNI: {dnis[i]} | Tel: {telefonos[i]} | Grado: {niveles[i]}\n")
        return True, "¡Guardado exitosamente en 'registros_matricula.txt'!"
    except Exception as e:
        return False, f"Error al guardar: {e}"