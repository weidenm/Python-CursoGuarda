# Seleção de Personagens:
# Primeiro, vamos criar uma lista predefinida de personagens disponíveis. Cada personagem terá um nome e atributos como pontos de vida (vida), pontos de ataque (ataque) e habilidades especiais.
# O jogador poderá escolher seu herói a partir dessa lista.
# Sistema de Batalha por Turno:
# Vamos criar uma classe para representar os personagens (heróis e dragões).
# Durante a batalha, os jogadores e os dragões se enfrentarão em turnos alternados.
# Os jogadores poderão atacar, defender ou usar habilidades especiais.
# Os dragões também terão suas próprias ações.
# O combate será baseado nos atributos dos personagens e nas decisões tomadas pelos jogadores.
# Progressão de Níveis:
# Implementaremos um sistema de progressão baseado nas vitórias dos jogadores.
# À medida que vencem batalhas, os jogadores avançam para níveis mais difíceis.
# Isso pode incluir o aumento da dificuldade dos oponentes e a introdução de novos desafios.
# Recompensas e Inventário:
# Ofereceremos recompensas aos jogadores vitoriosos, como novas habilidades, equipamentos ou itens.
# Criaremos um sistema de inventário para que os jogadores possam gerenciar seus itens.
# Aqui está um esboço inicial do código. Vamos expandi-lo com mais detalhes:


class Personagem:
    def __init__(self, nome, vida, ataque, habilidades):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.habilidades = habilidades


class Jogador(Personagem):
    def __init__(self, nome, vida, ataque, habilidades):
        super().__init__(nome, vida, ataque, habilidades)
        self.nivel = 1
        self.experiencia = 0

    def atacar(self, alvo):
        dano = self.ataque
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

    def defender(self):
        print(f"{self.nome} se defende e reduz o dano recebido!")

    def salvar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"{self.nome},{self.vida},{self.ataque}\n")

    @classmethod
    def recuperar_de_arquivo(cls, nome_arquivo):
        personagens = []
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, vida, ataque = linha.strip().split(',')
                personagem = cls(nome, int(vida), int(ataque), [])
                personagens.append(personagem)
        return personagens


class Dragao(Personagem):
    def __init__(self, nome, vida, ataque, habilidades):
        super().__init__(nome, vida, ataque, habilidades)

    def atacar(self, alvo):
        dano = self.ataque
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")


# Lista de personagens disponíveis
personagens_disponiveis = [
    Jogador("Guerreiro", 100, 20, ["Ataque Poderoso", "Defesa"]),
    Jogador("Mago", 80, 30, ["Bola de Fogo", "Cura"]),
    Dragao("Dragão Vermelho", 150, 25, ["Sopro de Fogo"]),
    # Adicione mais personagens aqui
]

# Lógica para seleção de personagem pelo jogador
print("Escolha seu herói:")
for i, personagem in enumerate(personagens_disponiveis):
    print(f"{i + 1}. {personagem.nome}")

escolha = int(input("Digite o número do herói desejado: ")) - 1
heroi_escolhido  = personagens_disponiveis[escolha]
print(f"Você escolheu {heroi_escolhido.nome}!")

# Salvar o herói em um arquivo
heroi_escolhido.salvar_arquivo("personagens.txt")

# Recuperar personagens do arquivo
personagens_salvos = Jogador.recuperar_de_arquivo("personagens.txt")
print("Personagens salvos:")
for p in personagens_salvos:
    print(f"{p.nome} (vida: {p.vida}, ataque: {p.ataque})")

#Define o inimigo
dragao = personagens_disponiveis[-1]  # Vamos enfrentar o dragão vermelho

while heroi_escolhido.vida > 0 and dragao.vida > 0:
    heroi_escolhido.atacar(dragao)
    dragao.atacar(heroi_escolhido)

if heroi_escolhido.vida > 0:
    print(f"{heroi_escolhido.nome} venceu o dragão!")
    heroi_escolhido.experiencia += 100  # Exemplo: ganha 100 pontos de experiência


    if heroi_escolhido.experiencia >= 200:  # Exemplo: avança para o próximo nível
        heroi_escolhido.nivel += 1
        print(f"{heroi_escolhido.nome} avançou para o nível {heroi_escolhido.nivel}!")
        # Implemente a lógica de recompensas e progressão de níveis aqui

else:
    print(f"{heroi_escolhido.nome} foi derrotado pelo dragão. Tente novamente!")
