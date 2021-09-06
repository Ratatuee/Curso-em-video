# variaveis que seram usadas para indicar o maior e o menor valor digitado
men = 0
mai = 0

# perguntado os números digitados e os colocando na lista
numeros = []
for c in range(0, 5):
    n1 = int(input(f'Digite o {c + 1}° valor- '))
    numeros.append(n1)

# definindo o maior e o menor valor
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]

        if numeros[c] < men:
            men = numeros[c]
# dando ao usuario as informações do maior valor e qual posição ele esta.
print(f'O maior valor é {mai} eles são os: ', end=' ')

for chave, valor in enumerate(numeros):
    if numeros[chave] == mai:
        print(chave + 1, end='°- ')
print('Valores')

# dando ao usuario as informações do menor valor e qual posição ele esta.
print(f'\nO menor valor é {men} eles são os: ', end=' ')

for chave2, valor2 in enumerate(numeros):
    if numeros[chave2] == men:
        print(chave2 + 1, end='°- ')
print('Valores')
