import turtle

# Create a turtle object
#my_turtle = turtle.Turtle()

# Move the turtle to draw a square
#for _ in range(4):
#    my_turtle.forward(100)
#   my_turtle.left(90)

# Keep the window open until closed manually
#turtle.done()

side_length = 100
angle = 120

turtle.color("blue","blue")

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.end_fill()

# Setting both pen color and fill color to blue
turtle.color("blue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Setting pen color to blue and fill color to red
turtle.color("blue", "red")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()


import turtle

tartaruga = turtle.Turtle()

# Vamos definir as cores
tartaruga.color("blue", "red")

# Agora vamos desenhar um círculo com as cores definidas
tartaruga.begin_fill()  # Inicia o preenchimento
tartaruga.circle(50)    # Desenha um círculo com raio 50
tartaruga.end_fill()    # Finaliza o preenchimento

# Agora vamos desenhar um círculo todo azul
tartaruga.color("blue")  # Apenas a cor azul agora
tartaruga.penup()        # Levanta a canetinha para não desenhar linhas
tartaruga.goto(100, 0)   # Move a tartaruga para outra posição
tartaruga.pendown()      # Abaixa a canetinha novamente
tartaruga.circle(50)    # Desenha outro círculo

tartaruga.done()         # Termina o desenho


turtle.done()

