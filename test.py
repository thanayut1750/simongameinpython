import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import PhotoImage
class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=1080, width=750)
        self.canvas.pack()

        self.imageff = Image.open("images\img4ff.png")
        self.photoff = ImageTk.PhotoImage(self.imageff)



        self.dark = {'r':self.canvas.create_image(190, 250, image=self.photoff, ),
                        'g':self.canvas.create_image(580, 250, image=self.photoff, ),
                        'b':self.canvas.create_image(190,600, image=self.photoff, ),
                        'y':self.canvas.create_image(580, 600, image=self.photoff, )}
        self.light = {'r':self.canvas.create_image(190, 250, image=self.photoff, ),
                        'g':self.canvas.create_image(580, 250, image=self.photoff, ),
                        'b':self.canvas.create_image(190,600, image=self.photoff, ),
                        'y':self.canvas.create_image(580, 600, image=self.photoff, )}

        self.image1 = Image.open("images\img1.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.image2 = Image.open("images\img2.png")
        self.photo2 = ImageTk.PhotoImage(self.image2)

        self.image3 = Image.open("images\img3.png")
        self.photo3 = ImageTk.PhotoImage(self.image3)

        self.image4 = Image.open("images\img4.png")
        self.photo4 = ImageTk.PhotoImage(self.image4)


        self.squares = {'r':self.canvas.create_image(190, 250, image=self.photo1, ),
                        'g':self.canvas.create_image(580, 250, image=self.photo2, ),
                        'b':self.canvas.create_image(190,600, image=self.photo3, ),
                        'y':self.canvas.create_image(580, 600, image=self.photo4, )}
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