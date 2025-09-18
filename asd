from turtle import*
import random

speed(0)

def road(x,y):
    penup()
    goto(x,y)
    pendown()
    color('dimgray')
    width(70)
    forward(550)

def star(x, y, size, c):
    penup()
    goto(x, y)
    pendown()
    color(c)
    begin_fill()
    count = 0
    while count < 5:
        forward(size)
        right(144)
        count += 1
    end_fill()

def draw_rect(x, y, width, height, color_name):
    penup()
    goto(x, y)
    pendown()
    color(color_name)
    begin_fill()
    count = 0
    while count < 2:
        forward(width)
        left(90)
        forward(height)
        left(90)
        count += 1
    end_fill()
def building1(x, y, c):
    draw_rect(x, y, 100, 250, c)
    windows(x, y, "yellow")

def sun (x, y,c):
    penup()
    goto (x, y)
    pendown()
    color(c)
    begin_fill()
    circle(150)
    end_fill()

def windows(x, y, c):
    rows = 5
    cols = 3
    win_w = 25
    win_h = 35
    row = 0
    while row < rows:
        col = 0
        while col < cols:
            penup()
            goto(x + col * (win_w + 5) + 10, y + row * (win_h + 5) + 10)
            pendown()
            color(c)
            begin_fill()
            count = 0
            while count < 4:
                forward(win_w)
                left(90)
                count += 1
            end_fill()
            col += 1
        row += 1

def backround(mode):
    if mode == "day":
        width(1000)
        color('lightblue')
        forward(10)
        road(-275, -235)

        width(1)
        sun(250, 250,"yellow")
        building1(-159, -200, "gray")
        building1(-60, -210, "lightgray")
        building1(53, -200, "slategray")
        

    elif mode == "night":
        draw_rect(-450, -300, 900, 600,  "midnightblue")
        count = 0
        while count < 15:
            star(random.randint(-250, 250), random.randint(100, 280,), random.randint(5, 10),  "yellow")
            count+=1
        building1(-159, -200, "gray")
        building1(-60, -250, "lightgray")
        building1(53, -240, "slategray")



backround(input("day or night?"))




exitonclick()
