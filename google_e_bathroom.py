import sys

def ultimo_en_entrar_nico(total, persona):
    tramos_nico = {total: 1}
    while True:
        largo = max(tramos_nico)
        veces = tramos_nico.pop(largo)
        if persona <= veces:
            return largo // 2, (largo - 1) // 2
        persona -= veces
        for mitad in (largo // 2, (largo - 1) // 2):
            tramos_nico[mitad] = tramos_nico.get(mitad, 0) + veces

def banos_nico():
    renglones = sys.stdin.read().split("\n")
    casos = int(renglones[0])
    for num in range(1, casos + 1):
        total, persona = map(int, renglones[num].split())
        grande, chico = ultimo_en_entrar_nico(total, persona)
        print(f"Case #{num}: {grande} {chico}")

banos_nico()
