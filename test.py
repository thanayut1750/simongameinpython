import tkinter as tk
import random
from PIL import Image, ImageTk

class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=1080, width=850)
        self.canvas.pack()

        self.status = tk.Label(parent, text='Let\'s go!',font="arial").place(x=400,y=0)

        self.img1 = Image.open("images\img1.png")
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.limg1 = tk.Label(self.canvas,image=self.photo1)
        self.limg1.place(x=30,y=50)

        self.img2 = Image.open("images\img2.png")
        self.photo2 = ImageTk.PhotoImage(self.img2)
        self.limg2 = tk.Label(self.canvas,image=self.photo2)
        self.limg2.place(x=410,y=50)

        self.img3 = Image.open("images\img3.png")
        self.photo3 = ImageTk.PhotoImage(self.img3)
        self.limg3 = tk.Label(self.canvas,image=self.photo3)
        self.limg3.place(x=30,y=400)

        self.img4 = Image.open("images\img4.png")
        self.photo4 = ImageTk.PhotoImage(self.img4)
        self.limg4 = tk.Label(self.canvas,image=self.photo4)
        self.limg4.place(x=410,y=400)    

        img_got_click = [self.limg1,self.limg2,self.limg3,self.limg4]

        def pic_clicked(event):
           print("baaaa")


        self.limg1.bind('<1>', pic_clicked)
        self.limg2.bind('<1>', pic_clicked)
        self.limg3.bind('<1>', pic_clicked)
        self.limg4.bind('<1>', pic_clicked)


    


root = tk.Tk()
simon = Simon(root)
root.mainloop()