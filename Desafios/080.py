pos = 0
numeros = []
for c in range(0, 5):
    n1 = int(input(f'Digite o {c + 1}° número- '))
    if c == 0 or n1 > numeros[-1]:
        numeros.append(n1)
    else:
        while pos < len(numeros):
            if n1 <= numeros[pos]:
                numeros.insert(pos, n1)
                break
            pos += 1
print(numeros)
