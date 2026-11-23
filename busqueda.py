def buscar_por_codigo(registros, codigo):
    if not isinstance(codigo, str):
        return None

    codigo = codigo.strip().upper()

    for registro in registros:
        if str(registro.get("codigo", "")).strip().upper() == codigo:
            return registro

    return None


def mostrar_resultado(registro):
    if registro is None:
        print("No se encontró el expediente.")
        return

    print(f"Código:    {registro.get('codigo', '')}")
    print(
        f"Nombres:   {registro.get('nombres', '')} "
        f"{registro.get('apellidos', '')}"
    )
    print(f"DNI:       {registro.get('dni', '')}")
    print(f"Teléfono:  {registro.get('telefono', '')}")
    print(f"Documento: {registro.get('tipo_documento', '')}")

    print(
        f"Nivel:     {registro.get('nivel', '')} "
        f"{registro.get('grado', '')}-"
        f"{registro.get('seccion', '')}"
    )