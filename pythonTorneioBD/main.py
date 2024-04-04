import sqlite3

conn = sqlite3.connect("heroes_dragons.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT  EXISTS heroes
    (id INTEGER PRIMARY KEY AUTOINCREMENT , 
    name TEXT,
    health INTEGER,
    attack INTEGER)''')


cursor.execute('''CREATE TABLE IF NOT  EXISTS dragons
    (id INTEGER PRIMARY KEY AUTOINCREMENT , 
    name TEXT,
    health INTEGER,
    attack INTEGER)''')

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Hero(Character):
    def __str__(self):
        return f"Heroi {self.name}, Vida: {self.health}, Attack: {self.attack}"

class Dragon(Character):
    def __str__(self):
        return f"Dragão {self.name}, Vida: {self.health}, Attack: {self.attack}"

#INSERE DADOS DOS HEROIS E DRAGOES
def insert_hero(hero):
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO heroes (name, health, attack) VALUES (?,?,?)",
                   (hero.name, hero.health, hero.attack))
    conn.commit()
    conn.close()


def insert_dragon(dragon):
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dragons (name, health, attack) VALUES (?,?,?)",
                   (dragon.name, dragon.health, dragon.attack))
    conn.commit()
    conn.close()

#RECUPERA OS DADOS DO PERSONAGEM

def get_heroes():
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM heroes")
    heroes_data = cursor.fetchall()
    conn.close()

    heroes = [Hero(*data[1:]) for data in heroes_data]
    return heroes

def get_dragons():
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dragons")
    dragons_data = cursor.fetchall()
    conn.close()

    dragons = [Dragon(*data[1:]) for data in dragons_data]
    return dragons

#CRIA TORNEIO
def executa_torneio():
    heroes = get_heroes()
    dragons = get_dragons()

    for hero in heroes:
        for dragon in dragons:
            if hero.attack > dragon.attack:
                print(f"{hero.name} venceu {dragon.name}")
            else
                print(f"{dragon.name} venceu {hero.name}")



executa_torneio()
#drag = Dragon('Drak',100, 50)
#insert_dragon(drag)

