import sys

INFINITO_NICO = float("inf")

def minimo_costo_nico(precio_cj, precio_jc, mural):
    con_c = con_j = None
    for pos, letra in enumerate(mural):
        nuevo_c = nuevo_j = INFINITO_NICO
        if pos == 0:
            if letra != "J": nuevo_c = 0
            if letra != "C": nuevo_j = 0
        else:
            if letra != "J": nuevo_c = min(con_c, con_j + precio_jc)
            if letra != "C": nuevo_j = min(con_j, con_c + precio_cj)
        con_c, con_j = nuevo_c, nuevo_j
    return min(con_c, con_j)

def lunas_nico():
    renglones = sys.stdin.read().split("\n")
    casos = int(renglones[0])
    for num in range(1, casos + 1):
        px, py, mural = renglones[num].split()
        print(f"Case #{num}: {minimo_costo_nico(int(px), int(py), mural)}")

lunas_nico()
