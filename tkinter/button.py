import tkinter as tk

def greet():
    print("你好，欢迎使用 Tkinter!")

root = tk.Tk()
root.geometry('300x200')
greet_button = tk.Button(root, text="打招呼", command=greet)
greet_button.pack()

root.mainloop()