#Sistema de verificação de saldo e compras
aluno = ["Ana Beatriz", "João Pedro", "Lucas Gabriel", "Maria Eduarda", "Mariana Silva", "Guilherme Santos", "Beatriz Oliveira", "Enzo Gabriel", "Laura Martins", "Gustavo Henrique"]
saldo = [2500.50, 120.00, 3450.00, 890.30, 50.00, 2100.00, 780.45, 15.20, 10000.00, 450.00]

#Loop para o programa nunca parar
while True:
    print("\n" + "="*30)
    print("\n--- NOVO ATENDIMENTO ---")

    busca = input('Digite seu nome (ou "SAIR"): ').strip()

    if busca.upper() == "SAIR":
        print("Sistema encerrado.")
        continue # <-- O segredo está aqui! Ele ignora o que está embaixo e volta para o topo.
    
    posicao = aluno.index(busca)

    nome_aluno = aluno [posicao]
    saldo_aluno = saldo [posicao]

    saldo_atualizado = saldo_aluno
    print(f"Aluno selecionado: {nome_aluno} | Saldo: R$ {saldo_aluno}")

#Sistema de compras
    totaldecompras = float(input(' Digite o valor da compra '))
    print(totaldecompras)

    if saldo_aluno >= totaldecompras:
        saldo_atualizado = saldo_aluno - totaldecompras
        print(f" Compra aprovada! Seu saldo atual é de R$ {saldo_atualizado:.2f} ")

    else:
        print ("Saldo insuficiente para realizar essa compra.")


#Sistema de recarga do Saldo

    opcao = input('Deseja realizar uma recarga? (S/N)').strip() .upper()
    if opcao == "S":
        valor_recarga = float(input(' Digite o valor desejado para recarga '))
        novo_saldo = saldo_atualizado + valor_recarga
        saldo[posicao] = novo_saldo
        print(f'Parabéns! Recarga efetuada. Seu saldo agora é de R$ {novo_saldo:.2f}')

# O que acontece se ele digitar 'N' ou qualquer outra coisa
    else: 
         print("Compra finalizada com sucesso! Obrigado.")


