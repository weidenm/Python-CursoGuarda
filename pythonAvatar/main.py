# Exemplo: Criação de um avatar com Turtle
import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

avatar = turtle.Turtle()
avatar.shape("turtle")
avatar.color("blue")
avatar.penup()

# Desenhar cabelo
avatar.goto(-50, 150)
avatar.pendown()
avatar.circle(50)
avatar.penup()

# Desenhar olhos
avatar.goto(-30, 120)
avatar.dot(15, "black")
avatar.goto(20, 120)
avatar.dot(15, "black")

# Desenhar corpo
avatar.goto(0, 50)
avatar.pendown()
avatar.circle(50)
avatar.penup()

# Desenhar braços
avatar.goto(-70, 20)
avatar.pendown()
avatar.goto(-120, -20)
avatar.penup()
avatar.goto(70, 20)
avatar.pendown()
avatar.goto(120, -20)
avatar.penup()

# Desenhar pernas
avatar.goto(-50, -50)
avatar.pendown()
avatar.goto(-70, -120)
avatar.penup()
avatar.goto(50, -50)
avatar.pendown()
avatar.goto(70, -120)

screen.mainloop()