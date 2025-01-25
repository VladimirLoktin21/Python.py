import turtle

# Настраиваем экран
screen = turtle.Screen()
screen.title("Рисуем домик")
screen.bgcolor("white")

# Функция для рисования квадрата
def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Функция для рисования треугольной крыши
def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Функция для рисования прямоугольной двери
def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Настраиваем черепашку
pen = turtle.Turtle()
pen.speed(3)

# Рисуем основание дома
pen.penup()
pen.goto(-75, -50)
pen.pendown()
draw_square(pen, 150, "lightblue")

# Рисуем крышу
pen.penup()
pen.goto(-75, 100)
pen.pendown()
draw_triangle(pen, 150, "brown")

# Рисуем дверь
pen.penup()
pen.goto(-30, -50)
pen.pendown()
draw_rectangle(pen, 40, 70, "darkblue")

# Рисуем окно
pen.penup()
pen.goto(-60, 10)
pen.pendown()
draw_square(pen, 30, "white")

# Завершаем работу
pen.hideturtle()
screen.mainloop()
