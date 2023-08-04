#exercise 2.1

movie=input("what is your favorite movie?")
book=input("what is your favorite book?")

print("movie: {}, book: {}". format(movie, book))

#exercise 2.2

friends = input("how many friends?")
pizzas=int(friends) * 0.5

print("you need {} pizzas for {} friends".format(pizzas, friends))

# Exercise 2.3

# Extension 1: Make the triangle blue
# To make the triangle blue, we need to set the color of the Turtle
# object before drawing the triangle.

import turtle

# Create a Turtle object
t = turtle.Turtle()

# Set the color to blue
t.color("blue")

# Draw a triangle
for _ in range(3):  #range() function generate a sequence of numbers from 0 to 2 (since range(3) generates numbers up to, but not including, 3)
    t.forward(100)  # move forward by 100 units. Since the turtle starts at the center of the screen by default, this command will draw the first side of the triangle, 100 units long.
    t.left(120)     # turn left by 120 degrees. After this command, the turtle will be facing in a new direction, which is 120 degrees counterclockwise from its previous orientation.

# Keep the window open until manually closed
turtle.done()

# Extension 2: Draw a circle
# To draw a circle, you need to use the circle() method of the 
# Turtle object. First, you have to move the turtle to the starting 
# position for the circle using the penup() and goto() methods.

import turtle

# Create a Turtle object
t = turtle.Turtle()

# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.left(120)
    
'''

The underscore character _ is often used as a variable name in Python when you don't plan to use the value of the variable. 
It's a convention to use _ as a variable name when you need to iterate over a sequence and you don't actually need the value 
of each item.

# Exemplo usando a variável de loop regularmente
for i in range(5):
    print(i)

# Saída:
# 0
# 1
# 2
# 3
# 4

# Exemplo usando o underscore como variável de loop
for _ in range(5):
    print("Hello")

# Saída:
# Hello
# Hello
# Hello
# Hello
# Hello

'''

# Move the turtle to a new position for the circle
t.penup()
t.goto(-50, -50)  # Adjust the coordinates to center the circle
t.pendown()

# Draw a circle
t.circle(50)

# Keep the window open until manually closed
turtle.done()

'''
after drawing the equilateral triangle, we want to draw a circle 
centered at a specific position on the screen. The position (-50, -50) was chosen 
somewhat arbitrarily to demonstrate how to move the turtle to a different location 
before drawing the circle.

In the turtle graphics coordinate system, the center of the screen is considered the 
origin (0, 0). The positive x-axis extends to the right, and the positive y-axis extends 
upward. The negative x-axis extends to the left, and the negative y-axis extends downward.

So, when we use goto(-50, -50), we are moving the turtle to the left by 50 units from the 
center (origin) in the x-direction and down by 50 units in the y-direction. This places the 
turtle at the position (-50, -50) before it starts drawing the circle.

'''

# exercise 2.4

#Extension 1: Draw a spiral
#To draw a spiral, we can repeatedly increase the side_length in 
# each iteration of the loop. This will create a spiral effect as the turtle moves.

import turtle

sides = int(input('Number of sides: ')) # Ask the user for the number of sides
angle = 360 / sides # Calculate the angle needed to turn

#Imagine drawing a polygon with 3 sides (a triangle). 
# The sum of its interior angles is (3-2) * 180 degrees = 180 degrees. 
# Since all sides of a triangle are equal, each angle of the triangle is 180 degrees / 3 sides = 60 degrees.
'''
    /\
   /  \
  /    \
 /______\

 Each angle is 60 degrees


Now, let's consider a polygon with 4 sides (a square). The sum of its interior angles is (4-2) * 180 degrees = 360 degrees. 
Again, all sides of the square are equal, so each angle of the square is 360 degrees / 4 sides = 90 degrees

   _____
  |     |
  |     |
  |_____|

 Each angle is 90 degrees

In general, for any polygon with n sides, each interior angle is given by dividing 360 degrees by the number of sides (n).

So, in the code provided, the line angle = 360 / sides calculates the angle needed to turn for each side of the polygon 
based on the number of sides specified by the user
'''
side_length = 60 # Set the initial side length to 60

for _ in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)
    side_length += 10  # Increase side_length for each iteration

turtle.done()


#Extension 2: Draw a circle using a for loop
#To draw a circle, we need to set the number of sides (sides) to a 
# large value, close to infinity. This will create the effect of drawing 
# a circle with a large number of tiny sides.

import turtle

# Set a large number of sides to approximate a circle
sides = 360 #360 sides is a circle
angle = 360 / sides # Calculate the angle needed to turn
# in this case, angle = 360 / 360 = 1, so the turtle will turn 1 degree for each side.
side_length = 2 # Set the initial side length to 2

for _ in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()

# In this extension, we set sides to 360, which means the 
# loop will draw 360 sides, effectively creating a circle. 
# We also reduce the side_length to make the sides very short, so when combined, 
# it appears as if a circle is drawn.



# exercise 2.5

import turtle

def draw_triangle(side_length):  # Define a function to draw a triangle
    for _ in range(3):  # Draw a triangle with side length of 100 units
        turtle.forward(side_length)  # move forward by 100 units
        turtle.left(120) # turn left by 120 degrees

def draw_circle(radius): # Define a function to draw a circle
    turtle.circle(radius) # Draw a circle with a radius of 50 units

# Set up the turtle
turtle.speed(1)  # Slowest speed
turtle.penup()
turtle.goto(-100, 0)  # Set initial position for triangle
turtle.pendown()

# Draw the triangle with side length of 100 units
draw_triangle(100)

# Move the turtle to a new position for the circle
turtle.penup()
turtle.goto(100, 0)  # Set initial position for circle
turtle.pendown()

# Draw a circle with a radius of 50 units
draw_circle(50)

# Keep the window open until manually closed
turtle.done()

#exercise 2.6

import turtle

def draw_triangle(side_length, color="black"):
    turtle.fillcolor(color) # Set the fill color
    turtle.begin_fill() # Begin the fill process
    for _ in range(3):
        turtle.forward(side_length) # move forward by 100 units
        turtle.left(120) # turn left by 120 degrees
    turtle.end_fill() # Complete the fill process

# Set up the turtle
turtle.speed(1)  # Slowest speed

# Draw a red triangle with side length of 100 units
draw_triangle(100, "red")

# Move the turtle to a new position for the next triangle
turtle.penup()
turtle.goto(200, 0)  # Set new position for the next triangle
turtle.pendown()

# Draw a blue triangle with side length of 150 units
draw_triangle(150, "blue")

# Keep the window open until manually closed
turtle.done()

# exercise 2.7

def circle_area(radius):  # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    return area  # return area here

circle_1 = circle_area(10)
print(circle_1)


'''
Added the radius parameter to the function definition, so when we call 
the function, we need to provide a value for the radius.

The formula to calculate the area of a circle is π * radius^2, where π (pi) 
is approximately 3.14. So, inside the function, we calculate the area using area = 3.14 * (radius ** 2).

Finally, we use the return statement to return the calculated area from the function.

When we call circle_area(10), it will calculate the area of a circle with a radius of 10 and store the 
result in circle_1. Then, it will print the calculated area using print(circle_1).

'''

#other exeemples of usinf turtle:

'''
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

'''