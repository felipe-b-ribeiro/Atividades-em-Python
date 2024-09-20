
while True:
    print('\n')
    print("Olá! Verifique se você pode doar sangue.")
    print('\n')

    idade = int(input("Qual a sua idade? "))
    if idade > 69 or idade < 16:
        print('\n')
        print("Você não está apto para doação de sangue.")
        break

    saude = input("Você está em boas condições de saúde? ")
    if saude == 'nao' or saude == "Nao" or saude == 'Não' or saude == 'não':
        print('\n')
        print("Você não está apto para doação de sangue.")
        break       

    peso = int(input("Qual é o seu peso? (Em KG) "))
    if peso < 50:
        print('\n')
        print("Você não está apto para doação de sangue.")
        break

    sono = int(input("Quantas horas de sono você teve na última noite? "))
    if sono < 6:
        print('\n')
        print("Você não está apto para doação de sangue.")
        break

    alimentacao = input("Você se alimentou bem nos últimos dias? (Sim/Não) ")
    if alimentacao == 'nao' or alimentacao == 'não' or alimentacao == 'Não' or alimentacao == 'Nao':
        print('\n')
        print("Você não está apto para doação de sangue.")
        break
    
    print('\n')
    print("Parabéns! Você está apto a doar sangue!")
    print('\n')
    
    deseja = input('Deseja verificar outra pessoa? ')
    if deseja == 'não' or deseja == 'Não' or deseja == 'nao' or deseja == 'Nao':
        break