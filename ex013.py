def paresmatriz(matriz):
    return [x for linha in matriz for x in linha if x % 2 == 0]