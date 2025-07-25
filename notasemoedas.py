n = float(input())
print('NOTAS:')
print(n)
for nota in[100,50,20,10,5,2]:
    quantidades = n // nota
    print(f'{quantidades} nota(s) de R${nota},00')

print('MOEDAS:')
for moeda in[1, 0.50, 0.25, 0.10, 0.05,0.01]:
    quantidadedois = n // moeda
    print(f'{quantidadedois:.0f} moeda(s) de R${moeda}')
    n = n % moeda
    n = n % nota
#incompleto
