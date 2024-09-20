for i in range(50):
    nomes = []
    nome = [input('Nome: ')]
    nomes = nomes, nomes.extend(nome)
    continuar = input('Deseja continuar? (S/N) ')
    if continuar == 'N' or continuar == 'n':
        print(nomes)
        break

