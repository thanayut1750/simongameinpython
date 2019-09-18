import tkinter as tk
import random
from PIL import Image, ImageTk

class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=1080, width=750)
        self.canvas.pack()

        self.img1 = PhotoImage(file="images\img1.png")
        self.canvas.create_image(130,50,anchor=NW, image=img1)

        self.img2 = PhotoImage(file="images\img2.png")
        self.canvas.create_image(610,50,anchor=EN, image=img2)
        
        self.img3 = PhotoImage(file="images\img3.png")
        self.canvas.create_image(130,400,anchor=WS, image=img3)

        self.img4 = PhotoImage(file="images\img4.png")
        self.canvas.create_image(610,400,anchor=ES, image=img4)
        
        self.dark = {'r':'darkred', 'g':'darkgreen', 'b':'darkblue', 'y':'darkgoldenrod'}
        self.light = {'r':'red', 'g':'green', 'b':'blue', 'y':'goldenrod'}
        self.squares = {'r':self.canvas.create_rectangle(0, 0, 200, 200,
                                              fill='darkred', outline='darkred'),
                        'g':self.canvas.create_rectangle(200, 0, 400, 200,
                                              fill='darkgreen', outline='darkgreen'),
                        'b':self.canvas.create_rectangle(0, 200, 200, 400,
                                              fill='darkblue', outline='darkblue'),
                        'y':self.canvas.create_rectangle(200, 200, 400, 400,
                                              fill='darkgoldenrod', outline='darkgoldenrod')}
        self.ids = {v:k for k,v in self.squares.items()}
        self.high_score = 0
        self.status = tk.Label(root, text='Let\'s go!')
        self.status.pack()
        self.parent.bind('<h>', self.score)
        self.draw_board()
        
    def draw_board(self):
        self.pattern = random.choice('rgby')
        self.selections = ''
        self.parent.after(1000, self.animate)
        
    def animate(self, idx=0):
        c = self.pattern[idx]
        self.canvas.itemconfig(self.squares[c], fill=self.light[c], outline=self.light[c])
        self.parent.after(500, lambda: self.canvas.itemconfig(self.squares[c],
                               fill=self.dark[c], outline=self.dark[c]))
        idx += 1
        if idx < len(self.pattern):
            self.parent.after(1000, lambda: self.animate(idx))
        else:
            self.canvas.bind('<1>', self.select)
    
    def select(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        color = self.ids[id]
        self.selections += color
        self.canvas.itemconfig(id,
                               fill=self.light[color], outline=self.light[color])
        self.parent.after(800, lambda: self.canvas.itemconfig(id,
                               fill=self.dark[color], outline=self.dark[color]))
        if self.pattern == self.selections:
            self.canvas.unbind('<1>')
            self.status.config(text='Right!')
            self.parent.after(2000, lambda: self.status.config(text=''))
            self.pattern += random.choice('rgby')
            self.selections = ''
            self.high_score = max(self.high_score, len(self.pattern))
            self.parent.after(2000, self.animate)
        elif self.pattern[len(self.selections)-1] != color:
            self.canvas.unbind('<1>')
            self.status.config(text='Nope!')
            self.parent.after(2000, lambda: self.status.config(text=''))
            self.parent.after(2000, self.draw_board)
            
    def score(self, event=None):
        self.status.config(text=self.high_score)
        self.parent.after(2000, lambda: self.status.config(text=''))
        
root = tk.Tk()
simon = Simon(root)
root.mainloop()