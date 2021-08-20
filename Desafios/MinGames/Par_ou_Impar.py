from random import randint
print('=' * 30)
print('      Jogo Par ou Impar')
print('=' * 30)
coun = 0
while True:
    a1 = randint(1, 10)
    while True:
        n1 = str(input('Impar ou par:[i/P] ')).upper()
        if n1 == 'I':
            print('PAR!')
            break
        if n1 == 'P':
            print('IMPAR!')
            break
    while True:
        n2 = int(input('Qual sua jogada? '))
        if n2 > 10:
            print(f'Você tem {n2} dedos?')
        if n2 <= 10:
            break

    print(f'Minha jogada é {a1}')
    s1 = a1 + n2
    s2 = s1 % 2
    print('Deu Par!'if s2 == 0 else 'Deu Impar!')
    if n1 == 'P' and s2 == 0:
        print('Você venceu!!! \nTente de novo!')
        print('-' * 30)
        coun += 1
    if n1 == 'I' and s2 == 1:
        print('Você venceu!!! \nTente de novo!')
        print('-' * 30)
        coun += 1
    if n1 == 'I' and s2 == 0:
        print('=' * 30)
        print(f'Você perdeu! \nTeve {coun} Vitórias.')
        break
    if n1 == 'P' and s2 == 1:
        print('=' * 30)
        print(f'Você perdeu. \nTeve {coun} vitórias.')
        break