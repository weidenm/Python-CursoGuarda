import sqlite3

conn = sqlite3.connect("heroes_dragons.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT  EXISTS heroes
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
    cursor.execute("INSERT INTO heroes (name, health, attack) VALUES (?,?,?)",
                   (dragon.name, dragon.health, dragon.attack))
    conn.commit()
    conn.close()

