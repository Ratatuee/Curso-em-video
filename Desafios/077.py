palavras = ('Prograamador', 'Python', 'Janela', 'oito', 'Teclado', 'Pendrive', 'Pomada', 'Copo', 'Computador',
            'Mouse', 'Biblia', 'Mesa', 'Caderno', 'Mousepad', 'Celular')

print('=' * 35)
for item in palavras:
    print(f'\n{f"{item}:" :<15}Vogais: ', end=' ')

    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
print('\n')
print('=' * 35)