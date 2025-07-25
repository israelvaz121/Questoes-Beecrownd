valor = float(input())
if 0 <= valor<= 25.00:
    print('Intervalo [0,25]')
elif  25.00 < valor<= 50.00 :
    print('Intervalo [25,50]')
elif  50.00 < valor<=75.00 :
    print('Intervalo [50,75]')
elif  75.00 < valor<=100 :
    print('Intervalo [75,100]')
else:
    print('Fora de intervalo')
