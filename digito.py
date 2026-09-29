n = int(input())
digitos = input().split()

lousa = ""
for d in digitos:
    lousa += d

for tam in range(1, len(lousa) + 1):
    primeiro = int(lousa[:tam])
    num = primeiro
    teste = ""

    # Vai montando a sequência para testar
    while len(teste) < len(lousa):
        teste += str(num)
        num += 1

    if teste == lousa:
        print(primeiro)
        break