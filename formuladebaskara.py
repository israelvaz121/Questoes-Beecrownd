a,b,c = map(float,input().split())
delta = (b**2)-(4*a*c)
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
        bhaskara = (-b + (delta**0.5)) / (a*2)
        bhaskara_dois = (-b - (delta**0.5)) / (a*2)

        print(f'R1 = {bhaskara:.5f}')
        print(f'R2 = {bhaskara_dois:.5f}')