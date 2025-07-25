x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
distancia = ((x2-x1)**2)+((y2-y1)**2)
resultado = distancia**0.5
print(f'{resultado:.4f}')