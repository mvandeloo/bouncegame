from tkinter import *
import random
import time

tk = Tk()
tk.title("Spiel")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, schläger, color):
        self.canvas = canvas
        self.schläger = schläger
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_schläger(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
            
    def hit_schläger(self, pos):
        schläger_pos = self.canvas.coords(self.schläger.id)
        if pos[2] >= schläger_pos[0] and pos[0] <= schläger_pos[2]:
            if pos[3] >= schläger_pos[1] and pos[3] <= schläger_pos[3]:
                return True
        return False

class Schläger:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.nach_links)
        self.canvas.bind_all('<KeyPress-Right>', self.nach_rechts)
        
    def nach_links(self, evt):
        self.x = -2
        
    def nach_rechts(self, evt):
        self.x = 2
    def triff_schläger(self, pos):
        schläger_pos = self.canvas.coords(self.schläger.id)
        if pos[2] >= schläger_pos[0] and pos[0] <=[2]:
            if pos[3] >= schläger_pos[1] and pos[3] <= schläger_pos[3]:
                return True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
     
schläger = Schläger(canvas, 'blue')
ball = Ball(canvas, schläger, 'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        schläger.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
