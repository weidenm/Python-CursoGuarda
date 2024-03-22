#ATIVIDADE 1
#1. Crie duas listas: uma lista de heróis e outra de dragões. Cada elemento de cada lista deve ser um dicionário com atributos como nome, elemento e poder.
#2. Implemente um loop que itere sobre ambas as listas, verificando as características mágicas de cada herói e dragão.
#3. Crie condições para formar alianças mágicas entre heróis e dragões. Por exemplo, alie um herói de elemento "fogo" a um dragão de elemento "água".
#4. Mostre as alianças formadas e as duplas mágicas que lutam bem juntas.

Dragao1 = ["Drogo","Água","Sopro congelante"]
Dragao2 = ["Tormenta","Fogo","Baforada desintegradora"]
Dragao3 = ["Mortex", "Fogo", "Sopro de Vulcão"]

Heroi1 = ["He-man","Fogo", "Espada de Grayskow"]
Heroi2 = ["Tundercats", "Água", "Olho de Tundera"]
Heroi3 = ["John Snow","Água", "Raio congelante"]

EquipeAgua = []
EquipeFogo = []

if Dragao1[1] ==  "Água":
    EquipeAgua.append(Dragao1[0])
else:
    EquipeFogo.append(Dragao1[0])

if Dragao2[1] == "Água":
    EquipeAgua.append(Dragao2[0])
else:
    EquipeFogo.append(Dragao2[0])

if Dragao3[1] == "Água":
    EquipeAgua.append(Dragao3[0])
else:
    EquipeFogo.append(Dragao3[0])

if Heroi1[1] == "Água":
    EquipeAgua.append(Heroi1[0])
else:
    EquipeFogo.append(Heroi1[0])

if Heroi2[1] == "Água":
    EquipeAgua.append(Heroi2[0])
else:
    EquipeFogo.append(Heroi2[0])

if Heroi3[1] == "Água":
    EquipeAgua.append(Heroi3[0])
else:
    EquipeFogo.append(Heroi3[0])


print("A equipe Água é composta por:", EquipeAgua)

print("A equipe Fogo é composta por:", EquipeFogo)

#ATIVIDADE 2
#1.	Defina uma variável chamada desafio_de_resistencia com um valor inicial representando a resistência a ser superada.
#2.	Utilize um loop para simular tentativas dos heróis em superar o desafio de resistência. Cada tentativa deve reduzir a resistência.
#3.	Verifique se a resistência chegou a zero. Se sim, os heróis superaram o desafio; caso contrário, continue as tentativas.
#4.	Mostre uma mensagem indicando se os heróis foram bem-sucedidos ou não no desafio.

desafio_de_resistencia = 1000

pontos = int(input("Digite quantos pontos de força você quer usar para vencer o desafio:"))
nTentativa = int(input("Digite quantidade de vezes deseja tentar"))

cont = 0

##while desafio_de_resistencia > 0:
  ##  desafio_de_resistencia = desafio_de_resistencia - pontos
   ## Cont = ContTentativa + 1
##print("Seu herói preciso de ", ContTentativa, "vezes para vencer o desafio.")

while cont < nTentativa:
    desafio_de_resistencia = desafio_de_resistencia - pontos
    cont = cont + 1

if desafio_de_resistencia <= 0:
    print("Seu herói superou o desafio com ", cont, " tentativas")
else:
    print("Não foi dessa vez. Empenhe-se mais para vencer.")

#ATIVIDADE 3
#1.Crie uma variável nivel_treinamento que represente o nível de intensidade do treinamento.
#2.Utilize estruturas condicionais para verificar o nível de treinamento e atribuir pontos de experiência aos heróis com base nesse nível.
#3.Mostre uma mensagem indicando o progresso dos heróis após o treinamento.
#4.Experimente criar diferentes cenários de treinamento com resultados variados.

