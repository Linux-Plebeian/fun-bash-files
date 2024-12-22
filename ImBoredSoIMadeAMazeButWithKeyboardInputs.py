from tkinter import *
tk = Tk()
can = Canvas(tk, height=500, width=700)
can.pack()
can.create_rectangle(20, 20, 40, 40)

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



def moveup(event):
    can.move(1, 0, -20)
def movedown(event):
    can.move(1, 0, 20)
def moveleft(event):
    can.move(1, -20, 0)
def moveright(event):
    can.move(1, 20, 0)

can.bind_all('<KeyPress-w>', moveup)
can.bind_all('<KeyPress-s>', movedown)
can.bind_all('<KeyPress-a>', moveleft)
can.bind_all('<KeyPress-d>', moveright)
