print(' Entrada permitida somente para convidados!')

convidados = ['Aurora', 'Bento', 'Luna', 'ícaro', 'Maya', 'caelum']

nome_convidado = input(" Convidado Digite o seu nome").capitalize().strip() 


if nome_convidado in convidados:
    posicao = convidados.index(nome_convidado)
    print(f'olá {nome_convidado.capitalize()} Seja bem-vindo ao Brasil21, aproveite o evento!')

else:
    print("Acesso negado. Seu nome não está na lista.")

    print('Agradecemos a prefêrencia')


