import random #>> Para ser um número aleatorio preciso importar a biblioteca 

print("\n" + "="*30)
print("\n--- Vamos Jogar---")

reiniciar = True #>> Essa Variavel verifica se o usúario deseja ou não continuar

##>> Esse while ele faz o jogo ser reiniciado quando pedido e faz a contagem das tentativas
while reiniciar:
    tentativa = 0 
    numero_secreto = random.randint(1, 10) #>> Aqui coloquei a ferramenta para ele colocar o número aleatorio de 1 a 10

    #>>Esse While ele faz a parte do jogo com o usúario perguntas e verificação se a resposta do usúario está certa.
    while True:
        palpite = int(input("Qual o seu palpite? "))
        tentativa +=1 #>> Aqui faz a contagem de tentativas até o acerto
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou! Com {tentativa} 🎉")
            print("\n" + "="*30)
            print("\n--- Fim Do Jogo---")
            opcao = input("Você deseja jogar novamente?(S/N)").strip() .upper()
            #>> Esse If faz a verificação se o usúario deseja jogar novamente 
            if opcao == 'S':
                break  # Esse break faz parte do IF opcao
            else:
                reiniciar = False
                print( "Jogo finalizado, volte sempre")
                print("\n" + "="*30)
                break
        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior. ⬆️")
        else:
            print("Muito alto! Tente um número menor. ⬇️")

