import sys

def escalera_nico():
    tokens = sys.stdin.read().split()
    casos, idx = int(tokens[0]), 1
    for num in range(1, casos + 1):
        cantidad = int(tokens[idx]); idx += 1
        dados_nico = sorted(map(int, tokens[idx:idx + cantidad])); idx += cantidad
        altura_nico = 0
        for lados in dados_nico:
            if lados > altura_nico:
                altura_nico += 1
        print(f"Case #{num}: {altura_nico}")

escalera_nico()
