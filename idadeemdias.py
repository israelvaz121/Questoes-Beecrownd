dias = int(input())
ano = dias//365
mes = (dias%365)/30
dias = (dias%365)%30
print(f'{ano:.0f} anos(s)')
print(f'{mes:.0f} mes(es)')
print(f'{dias:.0f} dia(s)')