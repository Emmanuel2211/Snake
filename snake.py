"""Snake, classic arcade game.

Cambios:
Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, 
pero al azar, de una serie de 5 diferentes colores, excepto el rojo.

Editado por Emmanuel Cruz
            David Alonso Chang Ortega - A01658631
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
snake_colors = ["#00FCFC","#00FC32","#FC6F00","#F8FC00","#BBFC00"]
food_colors = ["#007709","#FC0076","#AC00FC","#2E00FC","#FC00DD"]
s_rng = snake_colors[randrange(0,4)]
f_rng = food_colors[randrange(0,4)]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, s_rng)

    square(food.x, food.y, 9, f_rng)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
