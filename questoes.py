def q1():  # questao 1
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k = k+1
        soma = soma+k

    return soma


def is_fibonacci(num, a=0, b=1):  # questao 2
    if a < num:
        return is_fibonacci(num, b, a+b)
    else:
        if a == num:
            return True
        else:
            return False


def calc_percentual_estados(dados):  # questao 4
    total = sum(dados.values())
    percentual = {}
    for e in dados.keys():
        percentual[e] = (dados[e]/total) * 100
    return percentual


def inverte_string(string):  # questao 5
    invertido = ""
    for n in range(len(string)-1, -1, -1):
        invertido = invertido + string[n]

    return invertido
