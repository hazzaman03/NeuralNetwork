from tkinter import *

from PIL import Image
import PIL.ImageOps    
import os
import numpy as np


class Paint(object):

    def __init__(self):
        self.root = Tk()

        self.reset_button = Button(self.root, text='reset', command=self.clear)
        self.reset_button.grid(row='1', column='2')

        self.c = Canvas(self.root, bg='white', width=560, height=560)
        self.c.grid(row='0', columnspan=5)
        
        self.guess_frame = Frame(self.root, width=200, height=560)
        self.guess_frame.grid(row=0, column=7)
        self.guess()
        
        self.old_x = None
        self.old_y = None
        self.line_width = 45
        self.color = 'black'
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        
        self.root.mainloop()
        
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
        self.guess()
        
    def clear(self):
        self.c = Canvas(self.root, bg='white', width=560, height=560)
        self.c.grid(row='0', columnspan=5)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.guess()
        
    def guess(self):
        self.c.postscript(file="ps.ps")
        img = Image.open('ps.ps').convert('L')
        img = img.resize((28,28), Image.BICUBIC)
        img = PIL.ImageOps.invert(img)
        cwd_str = os.getcwd()
        os.remove(cwd_str + '/ps.ps')
        arr = np.array(img)
        arr = np.divide(arr, 256)
        
        Label(self.guess_frame, text='Guess: 0', width=20, font=("Arial", 25)).grid(row=0, column=0)

        for i in range(10):
            Label(self.guess_frame, text=f"{i}: {round(100/9, 2)}%", width=20).grid(row=i+1, column=0)


if __name__ == '__main__':
    Paint()