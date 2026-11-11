import sys

def repartir_nico():
    tokens = sys.stdin.read().split()
    casos, idx = int(tokens[0]), 1
    for num in range(1, casos + 1):
        cantidad = int(tokens[idx]); idx += 1
        tareas_nico = []
        for orden in range(cantidad):
            ini, fin = int(tokens[idx]), int(tokens[idx + 1]); idx += 2
            tareas_nico.append((ini, fin, orden))
        tareas_nico.sort()
        letras_nico = [""] * cantidad
        libre_c = libre_j = 0
        se_puede = True
        for ini, fin, orden in tareas_nico:
            if libre_c <= ini:
                letras_nico[orden] = "C"; libre_c = fin
            elif libre_j <= ini:
                letras_nico[orden] = "J"; libre_j = fin
            else:
                se_puede = False
                break
        print(f"Case #{num}: {''.join(letras_nico) if se_puede else 'IMPOSSIBLE'}")

repartir_nico()
