class Personagem:
    def __init__(self, nome, hp, atk, habilidades):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.habilidades = habilidades

class Jogador(Personagem):
    def __init__(self, nome, hp, atk, habilidades):
        super().__init__(nome, hp, atk, habilidades)
        self.nivel = 1
        self.experiencia = 0

    def atacar(self, alvo):
        dano = self.atk
        alvo.hp -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

    def defender(self):
        print(f"{self.nome} se defende e reduz o dano recebido!")

class Dragao(Personagem):
    def __init__(self, nome, hp, atk, habilidades):
        super().__init__(nome, hp, atk, habilidades)

    def atacar(self, alvo):
        dano = self.atk
        alvo.hp -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

# Lista de personagens disponíveis
personagens_disponiveis = [
    Jogador("Guerreiro", 100, 20, ["Ataque Poderoso", "Defesa"]),
    Jogador("Mago", 80, 30, ["Bola de Fogo", "Cura"]),
    Dragao("Dragão Vermelho", 150, 25, ["Sopro de Fogo"]),
    # Adicione mais personagens aqui
]

# Lógica para seleção de personagem pelo jogador (mesmo código anterior)

# Simulação de batalha
heroi_escolhido = personagens_disponiveis[escolha]
dragao = personagens_disponiveis[-1]  # Vamos enfrentar o dragão vermelho

while heroi_escolhido.hp > 0 and dragao.hp > 0:
    heroi_escolhido.atacar(dragao)
    dragao.atacar(heroi_escolhido)

if heroi_escolhido.hp > 0:
    print(f"{heroi_escolhido.nome} venceu o dragão!")
    # lógica de recompensas e progressão de níveis aqui
else:
    print(f"{heroi_escolhido.nome} foi derrotado pelo dragão. Tente novamente!")
