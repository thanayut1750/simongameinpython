import tkinter as tk
import time
import random 
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1080x750")



#header label
headlb = 'Press A key to Start'
label1 = tk.Label(root,text=headlb,font="arial", width = len(headlb),bg="yellow")
label1.pack()
#End-header label



#load image
img1 = Image.open("images\img1.png")
photo1 = ImageTk.PhotoImage(img1)

img2 = Image.open("images\img2.png")
photo2 = ImageTk.PhotoImage(img2)

img3 = Image.open("images\img3.png")
photo3 = ImageTk.PhotoImage(img3)

img4 = Image.open("images\img4.png")
photo4 = ImageTk.PhotoImage(img4)

img5 = Image.open("images\img4ff.png")
photo5 = ImageTk.PhotoImage(img5)
#End-load image

#label with img
limg1 = tk.Label(root,image=photo1)
limg1.place(x=130,y=50)

limg2 = tk.Label(root,image=photo2)
limg2.place(x=610,y=50)

limg3 = tk.Label(root,image=photo3)
limg3.place(x=130,y=400)

limg4 = tk.Label(root,image=photo4)
limg4.place(x=610,y=400)

allimg = [limg1,limg2,limg3,limg4]
photo = [photo1,photo2,photo3,photo4]

status = False
selection =[]
pattern = []

def animate(idx =0):
    a = random.randrange(0,4)
    allimg[a].config(image=photo5)
    root.after(1000,lambda:allimg[a].config(image=photo[a]))
    idx += 1
    if idx < len(allimg):
        root.after(1000,lambda:animate(idx))
    else:
        for i in allimg:
            i.bind("<1>",lambda  i=i:select(i))


def select(img):
    b = img
    selection.append(b)
    print(selection)
    status = False

    


root.after(2000,animate)
#Key press to start fn
def keyimg1(event):
    limg1["image"] = photo5
    limg1.after(300,func=animation1)
def animation1():
    limg1["image"] = photo1



def keyimg2(event):
    limg2["image"] = photo5
    limg2.after(300,func=animation2)
def animation2():
    limg2["image"] = photo2


def keyimg3(event):
    limg3["image"] = photo5
    limg3.after(300,func=animation3)
def animation3():
    limg3["image"] = photo3


def keyimg4(event):
    limg4["image"] = photo5
    limg4.after(300,func=animation4)
def animation4():
    limg4["image"] = photo4
    next_startgame()

#root.bind("<Key>",key)
#End-Key press to start fn

# limg1.bind('<1>', keyimg1)
# limg2.bind('<1>', keyimg2)
# limg3.bind('<1>', keyimg3)
# limg4.bind('<1>', keyimg4)




root.mainloop()