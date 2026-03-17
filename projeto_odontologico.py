    #Iniciando o sistema
    #OPÇÃO DO MENU DE ATENDIMENTO



    # Inicializando as listas (banco de dados temporário)
pacientes = [] # Criando lista para guardar os pacientes cadastrado
agendamentos = [] #Criando a lista para os agendamento, onde paciente tem um dentista
funcionarios = [] # Criando lista para guardar os funcionarios
convenios = [] # Criando lista para guardar os convenios cadastrados


while True:
    print("\n" + "=" * 30)
    print(" --------Bem Vindo a clinica Aires Odontologia\n Qual a opção desejada?-------------")
    print("1. Cadastro de paciente")
    print("2. agendamento de paciente")
    print("3. cadastra funcionario")
    print("4. cadastrar convênio")
    print("5. Buscar paciente")
    print(".8 Sair")
    print("=" * 30)

            # Pedindo ao usuário uma opção
    escolha = input("Escolha uma opção: ")
            # Convertendo a resposta do usuario em INTEIRO e comparando com o numero 1



    if escolha == "8":
        print("Saindo do sistema... Até logo!")
        exit

        #//////////////////////////////////////////////////////////////////////////////////////
## Parte do Paciente
    if int(escolha)==1:
        
    # Guardando os valores de cada dado em determinada variavel 
        # (nome, data de nascimento,CPF,Email,telefone)
        nome = input("Digite o nome completo: ")
        datanascimento = input("Digite a data de nascimento: ")
        CPF = input("Digite o CPF: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")

        if nome.strip() == "" or datanascimento.strip() == "" or CPF.strip() == "" or email.strip() == "" or telefone.strip() == "":
            print("valor invalido (não pode ser vazio)")
            exit()

            # Guardando as informações em um dicionário Paciente
        else:
            novo_paciente = {
                "nome": nome,
                "data de nascimento": datanascimento,
                "cpf": CPF,
                "email": email,
                "telefone": telefone
            
        }
        pacientes.append(novo_paciente) # Adiciona à lista geral
        print(f"\nPaciente: {nome} cadastrado com sucesso!")
        print(pacientes)

#//////////////////////////////////////////////////////////////////////////////////////
## Parte do agendamento
    elif int (escolha) == 2:
        print("\n--- Novo Agendamento ---")
        nome_paciente = input("Nome do Paciente: ")
        data_consulta = input("Data da consulta (DD/MM/AAAA): ")
        profissional = input("Digite o nome do profissional: ")
        pagamento = input("Digite a forma de pagamento: ")


        if nome_paciente.strip() == "" or data_consulta.strip() == "" or profissional.strip() == "" or pagamento.strip() == "":
            print("valor invalido (não pode ser vazio)")
            exit()

# Guardando as informações em um dicionário Agendamento
        agendamentos_paci = {
        "Nome do Paciente": nome_paciente,
        "Data da consulta": data_consulta,
        "Profissional":profissional,
        "Forma de pagamento":pagamento
        }
        agendamentos.append(agendamentos_paci)
        print(f" \n Agendamento para {nome_paciente} concluído com sucesso!")
        for agenda in agendamentos:
            print(f"Paciente: {agenda['Nome do Paciente']}")
            print(f"Data: {agenda['Data da consulta']}")
            print(f"profissional: {agenda['Profissional']}")
            print(f"Pagamento: {agenda['Forma de pagamento']}")
            print("-" * 20) # Linha separadora entre um agendamento e outro
            print(agendamentos)

    #//////////////////////////////////////////////////////////////////////////////////////
    ## Parte do funcionario
        # //////////////////////////////////////////////////////////////////////////////////////

    elif int(escolha) == 3:
        print("=" * 10)
# Salvando as entradas em variáveis
        nome_funcionario = input(" Digite o nome completo do funcionario: ")
        funcao = input(" Qual a função do funcionario: ")
        contrato = input(" Qual o tipo de contratação: ")
        email_funcionario = input(" Digite EMAIL: ")
        tel_funcionario = input(" Digite TELEFONE: ")
    
        if nome_funcionario.strip() == "" or funcao.strip() == "" or contrato.strip() == "" or email_funcionario.strip() == "" or tel_funcionario.strip() == "":
            print("valor invalido (não pode ser vazio)")
            exit()
        print(funcionarios)

        # Organizando em um dicionário funcionario
        novo_funcionario = {
            "nome": nome_funcionario,
            "funcao": funcao,
            "contrato": contrato,
            "email": email_funcionario,
            "telefone": tel_funcionario
        }
        # Adicionando à lista funcionario
        funcionarios.append(novo_funcionario)
        print("Funcionário cadastrado com sucesso!")

# //////////////////////////////////////////////////////////////////////////////////////
## Parte do convênio
    elif int(escolha) == 4:
        print("=" * 10)
        conv_nome = input(" Digite o nome convênio: ")
        cnpj = input(" Digite o CNPJ: ")
        categoria = input(" Digite a categoria do convênio: ")
        tel_convenio = input(" Digite o telefone de contato: ")

        novo_convenio = {
            "nome": conv_nome,
            "cnpj": cnpj,
            "categoria": categoria,
            "telefone": tel_convenio
        }
        convenios.append(novo_convenio)
        print("Convênio cadastrado!")


        # //////////////////////////////////////////////////////////////////////////////////////
## Parte consultar pacientes pelo CPF

    # //////////////////////////////////////////////////////////////////////////////////////
    ## Parte consultar pacientes pelo CPF
    elif int(escolha) == 5:
        print("\n--- Consultar Paciente ---")
        cpf_busca = input("Digite o CPF do paciente para buscar: ").strip()
        if not pacientes:
            print("Nenhum paciente cadastrado no sistema ainda.")
        else:
            # AQUI: O input que faltava para perguntar o CPF
            
            encontrado = False # Variável de controle
            
            for p in pacientes:
                # Comparamos o CPF digitado com o que está no banco de dados
                if p["cpf"] == cpf_busca:
                    print("\n" + "="*30)
                    print(f"Paciente: {p['nome']}")
                    print(f"Data de Nascimento: {p['data de nascimento']}")
                    print(f"CPF: {p['cpf']}")
                    print(f"E-mail: {p['email']}")
                    print(f"Telefone: {p['telefone']}")
                    print(f"data da consulta")
                    print("="*30)
                    encontrado = True
                    break # Se achou, para de procurar na lista
            
            if not encontrado:
                print(f"\n[!] Paciente com CPF {cpf_busca} não encontrado.")