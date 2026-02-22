nome = input(' Digite seu nome ')
saldo = 3500
print(f' Olá {nome} seu saldo atual e de {saldo} ')

valorcompras = float(input(' Digite o valor das compras '))
print(f' O valor das compra foi de {valorcompras}')

if saldo >= valorcompras:
    saldoatual = saldo - valorcompras
    print(f"Compra aprovada! Seu saldo atual é de {saldoatual}")

else:
    print ("Saldo insuficiente para realizar essa compra.")