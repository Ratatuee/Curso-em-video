tabela_de_preços = ('Lápis', 1.49, 'Borracha', 0.49, 'Caderno', 10.99, 'Estojo', 13.90,
                    'Mochila', 119.99, 'Tesoura', 2.99, 'Caneta', 2.99, 'Fichario', 39.99,
                    'Cola', 4.99, 'Canetinha', 49.99)
print('=' * 30)
print(f'{"Tabela de preços" :^30}')
print('=' * 30)

for pos in range(0, len(tabela_de_preços)):
    if pos % 2 == 0:
        print(f'{tabela_de_preços[pos]:.<30}', end='R$ ')
    else:
        print(tabela_de_preços[pos])
print('=' * 40)
