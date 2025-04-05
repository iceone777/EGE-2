import turtle as t
k = 15
t.up()
t.tracer(0)
for x in range(-30, 30):
    for y in range(-20, 20):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.speed(1000)
t.tracer(1)
t.goto(-25 * k, 10 * k)
t.down()
t.right(30)
t.forward(4 * k)
t.right(330)
t.down()
t.forward(4 * k)
t.right(90)
t.forward(7 * k)
t.right(45)
t.forward((4 * 2**0.5) * k)
t.right(135)
t.forward(11 * k)