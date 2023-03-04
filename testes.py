from questoes import *
from faturamento import Faturamento


estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
    }


print(q1())

print("-"*40)

for n in range(0, 611):
    r = is_fibonacci(n)
    if r is True:
        print(n, r)

print("-"*40)


faturamento = Faturamento('dados.json')
print(faturamento.min())
print(faturamento.max())
print(faturamento.dias_alem_da_media())

print("-"*40)

print(calc_percentual_estados(estados))

print("-"*40)

print(inverte_string("ronaldo"))

