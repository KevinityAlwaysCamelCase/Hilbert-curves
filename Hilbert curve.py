import time
import turtle


def hilbert_curve(t, order, angle, step):
    if order == 0:
        return
    t.right(angle)
    hilbert_curve(t, order - 1, -angle, step)
    t.forward(step)
    t.left(angle)
    hilbert_curve(t, order - 1, angle, step)
    t.forward(step)
    hilbert_curve(t, order - 1, angle, step)
    t.left(angle)
    t.forward(step)
    hilbert_curve(t, order - 1, -angle, step)
    t.right(angle)

    time.sleep(0)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
screen.tracer(50)

start_x = -276
start_y = -276
angle = -90

colors = ["red", "blue", "green", "orange", "purple", "brown", "cyan"]

while True:
    t.clear()
    t.goto(start_x, start_y)
    t.pendown()
    act = input("type(it='iterate from order 1 to 7, both included'; ord='chooses only one order'; exit='exit the "
                "software'): ")
    if act == "it":
        for i in range(1, 8):
            t.goto(start_x, start_y)
            t.color(colors[i-1])
            hilbert_curve(t, i, angle, 552 / (2 ** i - 1))
            screen.update()
            time.sleep(1)
    elif act == "ord":
        order = int(input("order(integer): "))
        step = 552 / (2 ** order - 1)
        hilbert_curve(t, order, angle, step)
        screen.update()
        time.sleep(5)
    elif act == "exit":
        break
    else:
        print("please choose from the given options")
    t.penup()
    t.color("black")