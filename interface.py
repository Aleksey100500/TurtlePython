import turtle

joe = turtle.Turtle()
joe.speed(1000)
joe.color('red')

colors = ['red', 'brown', 'green', 'blue']

def sq(a):
    for i in range(3):
        joe.color(colors[i%4])
        joe.forward(a)
        joe.left(120)

dlina = 10
for i in range(160):
    sq(dlina)
    joe.right(10)
    dlina = dlina + 1