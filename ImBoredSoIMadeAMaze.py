from tkinter import *
tk = Tk()
can = Canvas(tk, width=700, height=500)
can.pack()

can.create_rectangle(15, 15, 55, 55)

can.create_line(0, 495, 700, 495 )
can.create_text(35, 30, text='Start', font=('Helvetica', 10), fill='green')
can.create_text(190, 120, text='Made by Coding-Plebeain')
can.create_line(10, 0, 10, 500 )
can.create_line(60, 440, 640, 440 )
can.create_line(60, 0, 60, 440 )
can.create_line(640, 440, 640, 360 )
can.create_line(60, 440, 640, 440 )
can.create_line(640, 360, 300, 360 )
can.create_line(700, 300, 240, 300 )
can.create_line(240, 300, 240, 360 )
can.create_line(240, 360, 180, 360 )
can.create_line(180, 360, 180, 240 )
can.create_line(300, 360, 300, 420 )
can.create_line(300, 420, 120, 420 )
can.create_line(120, 420, 120, 180 )
can.create_line(120, 180, 300, 180 )
can.create_line(180, 240, 300, 240 )
can.create_line(180, 240, 360, 240 )
can.create_line(360, 240, 360, 120 )
can.create_line(300, 180, 300, 60 )
can.create_line(300, 60, 500, 60 )
can.create_line(360, 120, 560, 120 )
can.create_line(560, 120, 560, 60 )
can.create_line(560, 60, 560, 0 )
can.create_line(500, 60, 500, 0 )
can.create_text(530, 30, text='!Finish!', fill='green')

def u():
    import time
    for i in range(1, 4):
        can.move(1 , 0, -5)

def d():
    import time
    for i in range(1, 4):
        can.move(1 , 0, 5)

def l():
    import time
    for i in range(1, 4):
        can.move(1 , -7, 0)

def r():
    import time
    for i in range(1, 4):
        can.move(1 , 7, 0)
def maze():
     pass

from tkinter import *
btn = Button(tk, text='^----up----^', command=u)
btn.pack()
btn = Button(tk, text='<-----left-----', command=l)
btn.pack()
btn = Button(tk, text='-----right--->', command=r)
btn.pack()
btn = Button(tk, text='\/--down---\/', command=d)
btn.pack()
