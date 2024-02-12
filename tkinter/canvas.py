import tkinter as tk

# 创建一个窗口
root = tk.Tk()

# 创建一个Canvas部件
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# 在Canvas上绘制一个矩形
rect = canvas.create_rectangle(50, 50, 150, 150, fill='blue')

# 在Canvas上绘制一个圆
circle = canvas.create_oval(200, 200, 300, 300, fill='red')

# 显示窗口
root.mainloop()
