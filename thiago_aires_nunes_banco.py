saldo = 500.00


valor_compra = float(input("Qual o valor da compra que deseja fazer? R$ "))


if valor_compra <= saldo:
    print("Compra aprovada! Obrigado.")
else:
    print("Saldo insuficiente, compra negada!")