from time import sleep
#Numeros
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    # introdução com o usuario
    while True:
        n1 = int(input('Digíte um número[0 á 20]- '))
        if n1 > 20:
            print('\033[31mErro\033[m \nDigite um número abaixo de 20')

        # Resolução do programa
        if n1 <= 20:
            print('=' * 30)
            print('{:^30}'.format(numeros[n1]))
            print('=' * 30)
            break

    # opção de interação com o usuario
    print('[1]Digitar mais. \n[0]Sair.')
    opcao = int(input('Sua opção é- '))

    # Finalização
    if opcao == 0:
        break
    print('=' * 30)
print('Finalizando...')
sleep(2)
print('Até mais. Tchau!')