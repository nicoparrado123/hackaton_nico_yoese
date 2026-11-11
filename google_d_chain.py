import sys

def reacciones_nico():
    tokens = sys.stdin.read().split()
    casos, idx = int(tokens[0]), 1
    for num in range(1, casos + 1):
        cantidad = int(tokens[idx]); idx += 1
        diversion = [0] + [int(v) for v in tokens[idx:idx + cantidad]]; idx += cantidad
        destino = [0] + [int(v) for v in tokens[idx:idx + cantidad]]; idx += cantidad
        debajo_nico = [[] for _ in range(cantidad + 1)]
        for nodo in range(1, cantidad + 1):
            debajo_nico[destino[nodo]].append(nodo)
        mejor_nico = [0] * (cantidad + 1)
        suma_nico = 0
        for nodo in range(cantidad, 0, -1):
            if not debajo_nico[nodo]:
                mejor_nico[nodo] = diversion[nodo]
                continue
            valores = [mejor_nico[h] for h in debajo_nico[nodo]]
            menor = min(valores)
            suma_nico += sum(valores) - menor
            mejor_nico[nodo] = max(diversion[nodo], menor)
        suma_nico += sum(mejor_nico[h] for h in debajo_nico[0])
        print(f"Case #{num}: {suma_nico}")

reacciones_nico()
