from random import randint
numeros = (randint(1, 100000), randint(1, 100000), randint(1, 100000),
           randint(1, 100000), randint(1, 100000), )

print('Numeros sorteados:')
for n in numeros:
    print(f'{n}')

print(f'Menor número: {min(numeros)}')
print(f'Maior número: {max(numeros)}')
print(f'Soma entre eles: {sum(numeros)}')
print('=' * 30)
# ultilizando lista agora

numeros1 = []
contador = 0

while contador < 5:
    contador += 1
    ran = randint(1, 10000)
    numeros1.append(ran)

print('Numeros sorteados:')

for n1 in numeros1:
    print(n1)

print(f'Menor valor: {min(numeros1)}')
print(f'Maior valor: {max(numeros1)}')
print(f'Soma dos valores: {sum(numeros1)}')
