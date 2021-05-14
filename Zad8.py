from tkinter import *

window = Tk()
ww = 1000
wh = 500

canvas = Canvas(window, width=ww, height=wh, bg="white")
canvas.grid()
l1 =10
l2 =15


b1 = canvas.create_rectangle(10,wh-l1, 10+l1, wh, fill="blue")
window.mainloop()