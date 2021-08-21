from time import sleep
print('_=_' * 8)
print('     Banco Python')
print('_=_' * 8)
print('Seja bem-vindo.')
while True:
    n1 = int(input('Valor do saque: R$'))
    if n1 >= 100000000:
        print('Calculando...')
    # sistema de contagem de cedulas
    total = n1
    cedulas50 = 0
    cedulas20 = 0
    cedulas10 = 0
    cedulas1 = 0
    ced = 50
    ced20 = 20
    ced10 = 10
    ced1 = 1
    while True:
        if total >= ced:
            total -= ced
            cedulas50 += 1
        if total < ced:
            if total >= ced20:
                total -= 20
                cedulas20 += 1
            if total < ced20:
                if total >= ced10:
                    total -= ced10
                    cedulas10 += 1
                if total < ced10:
                    if total >= ced1:
                        total -= ced1
                        cedulas1 += 1
                    if total == 0:
                        break
    # Finalização
    print(f'->{cedulas50} Cedulas de R$50,00')
    print('                                  ')
    sleep(0.3)
    print(f'->{cedulas20} Cedulas de R$20,00')
    print('                                  ')
    sleep(0.3)
    print(f'->{cedulas10} Cedulas de 10,00')
    print('                                 ')
    sleep(0.3)
    print(f'->{cedulas1} Moedas de R$1,00')
    print('                                ')
    sleep(0.3)
    print('[1]Sacar novamente. \n[0]Sair')
    opçao = int(input('Sua opção é- '))
    if opçao == 0:
        break
print('Finalizando...')
sleep(2)
print('Até mais, tchau')