import sys

class Balde_nico:
    def __init__(self, maximo, ritmo):
        self.maximo, self.ritmo = maximo, ritmo
        self.disponibles, self.t_previo = maximo, 0

    def llenar_nico(self, ahora):
        self.disponibles = min(self.maximo, self.disponibles + self.ritmo * (ahora - self.t_previo))
        self.t_previo = ahora

    def cuanto_esperar_nico(self, pedido):
        faltan = pedido - self.disponibles
        if faltan <= 0:
            return 0
        return -(-faltan // self.ritmo)

def limitar_nico():
    peticiones_nico = Balde_nico(3, 1)
    fichas_nico = Balde_nico(100, 20)
    for renglon in sys.stdin.read().splitlines():
        trozos = renglon.split()
        if not trozos or trozos[0] != "REQUEST":
            continue
        instante, pedidos = int(trozos[1]), int(trozos[2])
        peticiones_nico.llenar_nico(instante)
        fichas_nico.llenar_nico(instante)
        if peticiones_nico.disponibles >= 1 and fichas_nico.disponibles >= pedidos:
            peticiones_nico.disponibles -= 1
            fichas_nico.disponibles -= pedidos
            print("ok")
        else:
            demora = max(peticiones_nico.cuanto_esperar_nico(1), fichas_nico.cuanto_esperar_nico(pedidos))
            print(f"429 retry-after={demora}")

limitar_nico()
