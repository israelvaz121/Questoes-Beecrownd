medidas = list(map(float,input().split()))
a,b,c = medidas
if a+b>c and b+c>a and c+a>b:
    perimetro = a+b+c
    print(f'Perimetro ={perimetro:.1f}')
else :
    calculo = (a+b)*c/2
    print(f'Area ={calculo:.1f}')