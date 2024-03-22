
class Equipe:
    def __init__(self,equipe_nome):
        self.equipe_nome = equipe_nome
        self.membros = []

class Heroi:
    def __init__(self, nome):
        self.nome = nome
        self.equipe = None

    def adicionar(self, equipe):
        if not self.equipe:
            equipe.membros.append(self)
            self.equipe = equipe
            print(f'{self.nome} ingressou na equipe {self.equipe.equipe_nome}')
        else:
            print(f'{self.nome} ja faz parte da equipe {self.equipe.equipe_nome}')


LigaDaJustica = Equipe("Liga da Justiça")
NovoHeroi = Heroi("Arqueiro Verde")
NovoHeroi.adicionar(LigaDaJustica)

print(f'Equipe de Heróis: {NovoHeroi.equipe.equipe_nome}')
print(NovoHeroi.equipe)