from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.bt_pen = Button(self.root, text="Pen", command=self.use_pen)
        self.bt_pen.grid(row=0, column=0)

        self.bt_brush = Button(self.root, text="Brush", command=self.use_brush)
        self.bt_brush.grid(row=0, column=1)

        self.bt_color = Button(self.root, text="Color", command=self.choose_color)
        self.bt_color.grid(row=0, column=2)

        self.bt_eraser = Button(self.root, text="Eraser", command=self.use_eraser)
        self.bt_eraser.grid(row=0, column=3)

        self.bt_delete = Button(self.root, text="Delete all", command=self.delete_all)
        self.bt_delete.grid(row=0, column=4)

        self.bt_choose_size= Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.bt_choose_size.grid(row=0, column=5)

        self.canvas = Canvas(self.root, bg="white", width=600, height=600)
        self.canvas.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()
    
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.bt_choose_size.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.bt_pen
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
    
    def use_pen(self):
        self.activate_button(self.bt_pen)
    
    def use_brush(self):
        self.activate_button(self.bt_brush)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.bt_eraser, eraser_mode=True)
    
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.bt_choose_size.get()
        if self.eraser_on:
            paint_color = 'white'
        else:
            paint_color = self.color
        
        if self.old_x and self.old_y:
            if self.active_button == self.bt_brush or self.eraser_on:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=self.line_width, fill=paint_color,
                                        capstyle=ROUND, smooth=TRUE, splinesteps=36)
            else:
                self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                        width=self.line_width, fill=paint_color,
                                        capstyle=BUTT, joinstyle=BEVEL,
                                        smooth=TRUE, splinesteps=12)
        self.old_x = event.x
        self.old_y = event.y

    def delete_all(self):
        self.canvas.destroy()
        self.canvas = Canvas(self.root, bg="white", width=600, height=600)
        self.canvas.grid(row=1, columnspan=5)
        self.setup()
        
    def reset(self, event):
        self.old_x, self.old_y = None, None
    
if __name__ == "__main__":
    Paint()
