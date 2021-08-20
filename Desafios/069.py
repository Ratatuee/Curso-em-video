from datetime import date
from emoji import emojize
from time import sleep
# descobrindo nomes
maior_idade = 0
menor_idade = 0
nome_maior = ''
nome_menor = ''
# Listas
nomes = []  # linha (16)
idades = []  # Linha (33)
sexos = []  # linha (36)
tudo = [nomes, idades, sexos]
atual = date.today().year  # ano atual
coun_mulher = 0  # mulher com menos de 20 anos Linha (44)
coun_homen = 0  # Homens ao total Linha (46)
coun_maioridade = 0  # pessoas maores de idade linha (48)
coun = 0 # contador do (for)
while True:
    while True:
        # inicio do cadastro ou perguntas, final na linha(32)
        nome = str(input(emojize(':black_circle:Informe seu primeiro nome- ', use_aliases=True))).title().strip()
        coun += 1
        nomes.append(nome)
        if nome.isalpha():
            break
        if nome.isnumeric():
            print('\033[31mNome invalido.\033[m \nPor favor digite somente letras')
            print('_' * 30)
    print('                                         ')
    while True:
        nascimento = int(input(emojize(f':black_circle:{nome} em que ano você nasceu- ', use_aliases=True)))
        if atual < nascimento:
            print('\033[31mData invalida!\033[m \nPor favor insira uma data válida.')
        if nascimento < 1911:
            print('\033[31mData invalida!\033[m \nPorfavor insira uma data válida')
        if 1911 < nascimento < atual:
            break
    print('                                         ')
    idade = atual - nascimento
    idades.append(idade)
    # descobrindo nome e idade (maior idade)
    if coun == 1:
        maior_idade = idade
        nome_maior = nome
    if idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    # descobrindo nome e idade(menor idade)
    if coun == 1:
        menor_idade = idade
        nome_menor = nome
    if idade < menor_idade:
        menor_idade = idade
        nome_menor = nome
    while True:
        sexo = str(input(emojize(f':black_circle:{nome} informe seu sexo [M/F]- ', use_aliases=True))).upper().strip()[
            0]
        sexos.append(sexo)
        if sexo in 'MF':
            break
        if sexo not in 'MF':
            print('\033[31mSexo invalido.\033[m \nInsira uma letra válida.')
    # filtros para contagem dos dados final na linha(40)
    if sexo == 'F':
        if idade < 20:
            coun_mulher += 1
    if sexo == 'M':
        coun_homen += 1
    if idade >= 18:
        coun_maioridade += 1
    # Finalização do cadastro
    print(f'\033[32mCadastrado realizado com sucesso.\033[m')
    print('=' * 33)
    print('[1]Realizar outro cadastro. \n[2]Visualizar os dados. \n[0]Finalizar o progama.')
    opçao = int(input('Sua opção é- '))
    if opçao == 0:
        break
    if opçao == 2:
        print('_' * 30)
        print(emojize(f':arrow_right: Maiores de idade: {coun_maioridade}', use_aliases=True))
        print(emojize(f':arrow_right: Mulheres com menos de 20 anos: {coun_mulher}', use_aliases=True))
        print(emojize(f':arrow_right: Total de homens: {coun_homen}', use_aliases=True))
        print('Mais...')
        print('[1]Visualizar os nomes em ordem alfabética. \n[2]Visualizar quem é o mais novo e o mais velho. \n[3]Pesquisar por nome.')
        opçao2 = int(input('Sua opção é- '))
        if opçao2 == 1:
            for name in sorted(nomes):
                print(name)
        if opçao2 == 2:
            print(f'Mais novo: {nome_menor}')
            print(f'Mais velho: {nome_maior}')
        if opçao2 == 3:
            print('Ainda não está feito.')

        print('_' * 30)
        print('[1]Realizar outro cadastro. \n[0]Finalizar o progama.')
        n2 = int(input('Sua opção é- '))

        if n2 == 0:
            break
print('Finalizando...')
sleep(2)
print('Programa finalizado com sucesso.')