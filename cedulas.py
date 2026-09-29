n = int(input())
print(n)
for nota in[100,50,20,10,5,2,1]:
    quantidades = n // nota
    print(f'{quantidades} nota(s) de R${nota},00')



    n = n % nota




