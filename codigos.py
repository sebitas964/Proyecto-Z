
# codigos.py
# Generación de códigos, validación, almacenamiento y ordenamiento.

PREFIJO = "MAT-"


def numero_codigo(codigo):
    if not isinstance(codigo, str):
        return 0

    if not codigo.startswith(PREFIJO):
        return 0

    numero = codigo[len(PREFIJO):]

    if numero.isascii() and numero.isdigit():
        return int(numero)

    return 0


def generar_codigo(registros):
    mayor = 0

    for registro in registros:
        numero = numero_codigo(registro.get("codigo", ""))
        mayor = max(mayor, numero)

    return f"{PREFIJO}{mayor + 1:05d}"


def ordenar_registros(registros):
    lista = registros[:]

    for i in range(len(lista) - 1):
        menor = i

        for j in range(i + 1, len(lista)):
            codigo_actual = numero_codigo(
                lista[j].get("codigo", "")
            )

            codigo_menor = numero_codigo(
                lista[menor].get("codigo", "")
            )

            if codigo_actual < codigo_menor:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista