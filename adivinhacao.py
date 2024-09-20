adivinha = int(input('Tente adivinhar um número de 1 a 100. '))
while adivinha != 45:
    if adivinha > 100:
        print('É só até 100, seu animal')
        adivinha = int(input('Tente adivinhar um número de 1 a 100. '))
    elif adivinha > 45:
        print('O número digitado é maior que o número secreto')
        adivinha = int(input('Tente adivinhar um número de 1 a 100. '))
    elif adivinha < 45:
        print('O número digitado é menor que o número secreto')
        adivinha = int(input('Tente adivinhar um número de 1 a 100. '))
else:
    print('Parabéns! Você ganhou!')
