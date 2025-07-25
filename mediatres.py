notas = list(map(float, input().split()))
media = (notas[0]*2 + notas[1]*3 + notas[2]*4 + notas[3]*1) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
else:
    print('Aluno reprovado.')