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

# Lista de personagens disponíveis (mesmo código anterior)

# Simulação de batalha (mesmo código anterior)

if heroi_escolhido.hp > 0:
    print(f"{heroi_escolhido.nome} venceu o dragão!")
    heroi_escolhido.experiencia += 100  # Exemplo: ganha 100 pontos de experiência
    if heroi_escolhido.experiencia >= 200:  # Exemplo: avança para o próximo nível
        heroi_escolhido.nivel += 1
        print(f"{heroi_escolhido.nome} avançou para o nível {heroi_escolhido.nivel}!")
        # Implemente mais lógica de recompensas aqui (novas habilidades, equipamentos, etc.)
else:
    print(f"{heroi_escolhido.nome} foi derrotado pelo dragão. Tente novamente!")

# Divirta-se expandindo o jogo com mais funcionalidades!