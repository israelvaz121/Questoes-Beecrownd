# Lendo a entrada do exercício
A, B = map(float,input().split())

c = (A + B) / 2
# Seu código vai aqui
print(c)
if c >= 7 :
    print("Aprovado")

elif c < 7 and c > 4:
    print("Recuperacao")

else :
    print("Reprovado")