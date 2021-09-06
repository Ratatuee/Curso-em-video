# perguntado os números e os coloocando nas listas
numeros = []
repetidos = []
c = 0
while c < 5:
    while True:
        n1 = int(input(f'Digíte o {c + 1}° número-  '))
        if n1 in numeros:
            print('Numero duplicado, não sera inserido')
            repetidos.append(n1)
            break

        if n1 not in numeros:
            numeros.append(n1)
        c += 1

        if c == 5:
            break
    if c == 5:
        break

# colocando as listas em ordem crecente
numeros.sort()
repetidos.sort()

# informando os números digitados
print(f'->Os números digitados foi:', end=' ')
for numero in numeros:
    print(numero, end=' ')

# informando os números que se repetiram
print('\n')
if len(repetidos) == 0:
    print('\n->Não ouve números repetidos.')
else:
    print('->Os números repetidos foram: ', end=' ')
    for pos, numero in enumerate(repetidos):
        if pos % 2 == 0:
            print(numero, end=' ' )
print('\n')