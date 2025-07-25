codigo,quantidade = map(int,input().split())
preços =  { 1: 4.00,
          2: 4.50,
          3: 5.00,
          4: 2.00,
          5: 1.50
          }
total = preços[codigo]*quantidade
print(f'TOTAL: R${total:.2f}')