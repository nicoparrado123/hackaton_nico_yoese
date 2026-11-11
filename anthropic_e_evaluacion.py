import sys, json, re, unicodedata

def limpiar_nico(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(ch for ch in texto if not unicodedata.combining(ch)).lower()
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()

def evaluar_nico():
    por_categoria_nico = {}
    buenas_nico = cuenta_nico = 0
    for renglon in sys.stdin.read().splitlines():
        if not renglon.strip():
            continue
        fila = json.loads(renglon)
        acerto = f" {limpiar_nico(fila['esperado'])} " in f" {limpiar_nico(fila['respuesta'])} "
        grupo = fila["categoria"]
        bien, todos = por_categoria_nico.get(grupo, (0, 0))
        por_categoria_nico[grupo] = (bien + acerto, todos + 1)
        buenas_nico += acerto
        cuenta_nico += 1
    for grupo in sorted(por_categoria_nico):
        bien, todos = por_categoria_nico[grupo]
        print(f"{grupo}: {bien}/{todos}")
    print(f"total: {buenas_nico}/{cuenta_nico} ({100 * buenas_nico / cuenta_nico:.1f}%)")

evaluar_nico()
