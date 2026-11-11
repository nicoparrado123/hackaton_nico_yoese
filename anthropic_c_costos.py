import sys, json

def a_dolares_nico(micros):
    return f"${micros // 1_000_000}.{micros % 1_000_000:06d}"

def calcular_costos_nico():
    gastado_nico = sin_cache_nico = hits_nico = cuenta_nico = 0
    for renglon in sys.stdin.read().splitlines():
        if not renglon.strip():
            continue
        uso = json.loads(renglon)
        entrada, escritura = uso["input_tokens"], uso["cache_creation_input_tokens"]
        lectura, salida = uso["cache_read_input_tokens"], uso["output_tokens"]
        precio = (entrada * 300 + escritura * 375 + lectura * 30 + salida * 1500) // 100
        precio_normal = (entrada + escritura + lectura) * 3 + salida * 15
        cuenta_nico += 1
        gastado_nico += precio
        sin_cache_nico += precio_normal
        if lectura > 0: hits_nico += 1
        print(f"solicitud {cuenta_nico}: {a_dolares_nico(precio)}")
    print(f"total: {a_dolares_nico(gastado_nico)}")
    print(f"sin_cache: {a_dolares_nico(sin_cache_nico)}")
    print(f"ahorro: {a_dolares_nico(sin_cache_nico - gastado_nico)}")
    print(f"aciertos_de_cache: {hits_nico}/{cuenta_nico}")

calcular_costos_nico()
