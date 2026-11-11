import sys, json

TEMPERATURAS_NICO = {"Bogotá": 14, "Medellín": 24, "Cali": 26}

def calcular_nico(datos):
    oper, x, y = datos.get("operacion"), datos.get("a"), datos.get("b")
    if oper == "sumar": return str(x + y)
    if oper == "restar": return str(x - y)
    if oper == "multiplicar": return str(x * y)
    if oper == "dividir":
        if y == 0: return "error: división por cero"
        cociente = abs(x) // abs(y)
        return str(cociente if (x >= 0) == (y > 0) else -cociente)
    return f"error: operación desconocida: {oper}"

def usar_herramienta_nico(herramienta, datos):
    if herramienta == "calculadora": return calcular_nico(datos)
    if herramienta == "clima":
        lugar = datos.get("ciudad")
        if lugar in TEMPERATURAS_NICO:
            return f"{TEMPERATURAS_NICO[lugar]} °C"
        return f"error: ciudad desconocida: {lugar}"
    return f"error: herramienta desconocida: {herramienta}"

def procesar_respuestas_nico():
    sys.stdout.reconfigure(encoding="utf-8")
    usos_nico = fallos_nico = 0
    for renglon in sys.stdin.read().splitlines():
        if not renglon.strip():
            continue
        mensaje = json.loads(renglon)
        if mensaje["stop_reason"] == "tool_use":
            for bloque in mensaje["content"]:
                if bloque["type"] == "tool_use":
                    salida = usar_herramienta_nico(bloque["name"], bloque["input"])
                    usos_nico += 1
                    if salida.startswith("error:"): fallos_nico += 1
                    print(f"tool_result {bloque['id']} {salida}")
        elif mensaje["stop_reason"] == "end_turn":
            final = "".join(bl["text"] for bl in mensaje["content"] if bl["type"] == "text")
            print(f"final: {final}")
    print(f"resumen: {usos_nico} llamadas, {fallos_nico} errores")

procesar_respuestas_nico()
