from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    def __init__(self):
        self.root = Tk()

        self.reset_button = Button(self.root, text='reset', command=self.clear)
        self.reset_button.grid(row='1', column='2')
        self.guess_button = Button(self.root, text='guess', command=self.guess)
        self.guess_button.grid(row='1', column='3')

        self.c = Canvas(self.root, bg='black', width=560, height=560)
        self.c.grid(row='0', columnspan=6)
        
        self.guess_frame = Frame(self.root, width=200, height=560)
        self.guess_frame.grid(row=0, column=7)
        Label(self.guess_frame, text='Guess: 0', width=20, font=("Arial", 25)).grid(row=0, column=0)

        for i in range(10):
            Label(self.guess_frame, text=f"{i}: {round(100/9, 2)}%", width=20).grid(row=i+1, column=0)
        
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 40
        self.color = 'white'
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=self.color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
    
    def clear(self):
        self.c = Canvas(self.root, bg='black', width=560, height=560)
        self.c.grid(row='0', columnspan=6)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    
    def guess(self):
        print('hi')


if __name__ == '__main__':
    Paint()