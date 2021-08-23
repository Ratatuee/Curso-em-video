tabela = ('Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'Flamengo',
          'Bragantino', 'Corintias', 'Atlético-GO', 'Ceará-SC', 'Athetico-PR',
          'Internacional', 'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia',
          'Fluminance', 'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')
# posição da chapecoense
chap = tabela.index('Chapecoense')
# titulo
print('=' * 19)
print('{:^19}'.format('Tabela normal'))
print('=' * 19)
# exibição da tabela
posicao = 0
for time in tabela:
    posicao += 1
    # pintando 4 primeiros times
    if posicao <= 4:
        print(f'{posicao}-\033[32m{time}\033[m')

    # deixando em branco os times da posição 5 á 16
    if 4 < posicao <= 16:
        print(f'{posicao}-{time}')

    # pintando os 4 ultimos times
    if posicao >= 17:
        print(f'{posicao}-\033[31m{time}\033[m')
# Tabela em ordem alfabética
print('=' * 40)
print('{:^40}'.format('Tabela em ordem alfabética'))
print('=' * 40)

for time in sorted(tabela):
    print(time)

# posição da chapecoense
print('=' * 33)
print('{:^33}'.format('Posição da chapecoense'))
print('=' * 33)

print(f'{chap +1}-Chapesoense')