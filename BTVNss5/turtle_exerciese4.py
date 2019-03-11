from turtle import*
def draw_square(a, b):
    speed(0)
    color(b)
    for i in range(4):
        forward(a)
        left(90)
print(draw_square(100, "red"))


for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()