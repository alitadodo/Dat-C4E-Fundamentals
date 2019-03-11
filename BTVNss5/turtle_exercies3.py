from turtle import*
def draw_square(a, b):
    speed(0)
    color(b)
    for i in range(4):
        forward(a)
        left(90)
draw_square(100, "red")
mainloop()