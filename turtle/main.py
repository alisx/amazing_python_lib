import turtle

# 初始化
win = turtle.Screen()
win.bgcolor('white')  # 设置背景颜色
turtle.speed(10)

# 绘制心形
def draw_heart(turtle, x, y, color, outline):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(outline)  # 设置边缘颜色
    turtle.pensize(4)  # 让箭更粗
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-100, 200)
    turtle.left(114)
    turtle.circle(-100, 200)
    turtle.forward(180)
    turtle.right(160)  # 为了让心形的尖更尖，我们添加了这一行
    turtle.color(color)  # 设置填充颜色
    turtle.end_fill()

# 绘制箭
def draw_arrow(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('gold')  # 修改箭的颜色为金色
    turtle.pensize(8)  # 让箭更粗
    turtle.setheading(-45)
    turtle.forward(80)
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    turtle.forward(200)
    turtle.right(20)
    turtle.backward(50)
    turtle.forward(50)
    turtle.left(40)
    turtle.backward(50)
    turtle.forward(50)

# 绘制文字
def draw_text(turtle, x, y, text):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('red')  # 修改文字颜色为金色
    turtle.write(text, align="center", font=("Courier", 30, "bold"))  # 增大字体大小，使其更粗

import time

time.sleep(5)
# 创建一个新的 turtle 对象
t = turtle.Turtle()

# 画第一颗心
draw_heart(t, -100, -50, 'red', 'gold')

# 移动到第二颗心的位置
t.penup()
t.right(55)  # 调整方向以便向左下移动
t.forward(50)  # 向左下移动一定的距离
# t.left(80)  # 调整方向以便开始画第二颗心
t.pendown()

# 画第二颗心
draw_heart(t, t.xcor(), t.ycor(), 'red', 'gold')

# 画箭
draw_arrow(t, -200, 300)

# 写文字
draw_text(t, -30, -100, 'I Love You！')

# 结束绘图
turtle.done()