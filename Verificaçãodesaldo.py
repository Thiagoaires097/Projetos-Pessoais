#Sistema de verificação de saldo e compras
aluno = ["Ana Beatriz", "João Pedro", "Lucas Gabriel", "Maria Eduarda", "Mariana Silva", "Guilherme Santos", "Beatriz Oliveira", "Enzo Gabriel", "Laura Martins", "Gustavo Henrique"]
saldo = [2500.50, 120.00, 3450.00, 890.30, 50.00, 2100.00, 780.45, 15.20, 10000.00, 450.00]
busca = input(' Digite seu nome ').strip()
posicao = aluno.index(busca)

nome_aluno = aluno [posicao]
saldo_aluno = saldo [posicao]

print(f"Aluno selecionado: {nome_aluno} | Saldo: R$ {saldo_aluno}")

totaldecompras = float(input(' Digite o valor da compra '))
print(totaldecompras)

if saldo_aluno >= totaldecompras:
    saldo_atualizado = saldo_aluno - totaldecompras
    print(f" Compra aprovada! Seu saldo atual é de R$ {saldo_atualizado:.2f} ")

else:
    print ("Saldo insuficiente para realizar essa compra.")


#Sistema de recarga do Saldo
valor_recarga = float(input(' Digite o valor desejado para recarga '))
novo_saldo = saldo_atualizado + valor_recarga
saldo[posicao] = novo_saldo


print(f'Parabéns! Recarga efetuada. Seu saldo agora é de R$ {novo_saldo:.2f}')

