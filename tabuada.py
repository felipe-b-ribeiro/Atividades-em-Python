numero = int(input('Digite um número para fazermos a tabuada do mesmo: '))

for i in range(1, 11):
    print(numero , ' x ' , i , ' = ' , i * numero)

numero2 = int(input('Digite um número para fazermos a exponenciação do mesmo: '))
exponenciacao = int(input('Digite o número de vezes que será exponenciado: '))

for i in range(1, exponenciacao + 1):
    print(pow(numero2, i))