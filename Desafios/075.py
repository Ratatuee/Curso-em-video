numeros = (int(input('Digite um número- ')),
           int(input('Digite outro número- ')),
           int(input('Digite mais um número- ')),
           int(input('Digite o ultimo número- ')))

print('=' * 30)
print(f'Qunatas vezes foi digitado o nove: {numeros.count(9)}')
print('-' * 30)

if 3 in numeros:
    print(f'Posição do número três: {numeros.index(3) + 1}°')
else:
    print('Número Três não foi encontrado.')

print('-' * 30)
print('Os números pares digitados são: ', end='')

for n in numeros:
    print(n , end=' ')
print('                                ')