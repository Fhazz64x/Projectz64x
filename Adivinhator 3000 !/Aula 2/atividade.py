print ("********************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
   print("Tentativa {} de {} de {} ".format(rodada,total_de_tentativas))

   chute_str = input("Dite o seu número: ")
   print("Voce digitou ", chute_str)
   chute = int(chute_str)

   acertou = chute == numero_secreto

   chute > numero_secreto

   chute < numero_secreto

   if(acertou):
       print("Parabéns ! você acertou !")
   else:
       if(maior):
           print("O seu chute foi maior que o número secreto!")
       elif(menor):
           print("O seu chute foi menor do que número secreto!")

        rodada = rodada + 1

print("Fim de jogo")
