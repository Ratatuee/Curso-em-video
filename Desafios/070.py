from time import sleep
menor = 0
opçao2 = -1
nomemenor = ''
total = 0
coun = 0
print('=' * 30)
print('         Python store')
print('=' * 30)
count = 0
while True:
    while True:
        nome = str(input('Nome do produto- ')).strip().title()
        if nome.isnumeric():
            print('\033[31mSomente letras!\033[m')
        if nome.isalpha():
            break

    preço = float(input('Preço R$ '))
    if preço >= 1000:
        coun +=1
    count += 1
    if count == 1:
        menor = preço
        nomemenor = nome
    if preço < menor:
        menor = preço
        nomemenor = nome

    total += preço
    print('-' * 20)
    while True:
        print('[1]Próximo produto. \n[2]Finalizar compras.')
        opçao = int(input('Sua opção é- '))
        if opçao == 1:
            break
        if opçao == 2:
            print('-' * 20)
            sleep(0.2)
        print(f'Preço final: R${total}')
        sleep(0.3)
        print(f'Produtos de mil reais ou mais: {coun}')
        sleep(0.3)
        print(f'Produto mais barato: {nomemenor}')
        sleep(0.3)
        print('-' * 30)
        print('[1]Comprar mais \n[0]Sair.')
        opçao2 = int(input('Sua opção é- '))
        if opçao2 == 1:
            break
        if opçao2 == 0:
            break
    if opçao2 == 0:
        break

print('Finalizando...')
sleep(2)
print('Finalizado!')