#Criando o dicionario vazio
user_info =  {}

#Dados do usuarios para cadastro
nome = input (' Digite seu nome ')

idade = input(' Digite sua idade ')

email = input(' Digite seu email ')

Cpf = input(' Digite seu CPF ')

suite = input (' Digite o número do quarto')

#Estamos guardando as informações digitada do usuario
user_info['nome'] = nome
user_info['idade'] = idade
user_info['email'] = email
user_info['CPF'] = Cpf
user_info['suite'] = suite

print(f'\n Cliente {nome} cadastrado com sucesso')


# O laço 'for' percorre cada par de informações dentro do user_info
for chave, valor in user_info.items():
    # Formatamos para que a chave apareça com a primeira letra maiúscula
    print(f"{chave.capitalize()}: {valor}")