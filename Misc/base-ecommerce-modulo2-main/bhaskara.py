from math import sqrt
#      a*x^2 + b*x + c
def delta(a, b, c):
    return ((b * b) - (4 * a * c))

def raiz_delta(a, b, c):
    return sqrt(delta(a, b, c))

def xis_linha(a, b, raiz_delta):
    return (-b + raiz_delta) / (2 * a)

def xis_duas_linhas(a, b, raiz_delta):
    return (-b - raiz_delta) / (2 * a)

def bhaskara(a, b, c):
    # sqrt => squared root => raiz quadrada
    rd = raiz_delta(a, b, c)
    x1 = xis_linha(a, b, rd)
    x2 = xis_duas_linhas(a, b, rd)

    return x1, x2