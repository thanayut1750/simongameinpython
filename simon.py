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

#Key press to start fn
def key(event):
    print("asdasdasdasd")

#root.bind("<Key>",key)
#End-Key press to start fn

#load image
img1 = Image.open("images\img1.png")
photo1 = ImageTk.PhotoImage(img1)

img2 = Image.open("images\img2.png")
photo2 = ImageTk.PhotoImage(img2)

img3 = Image.open("images\img3.png")
photo3 = ImageTk.PhotoImage(img3)

img4 = Image.open("images\img4.png")
photo4 = ImageTk.PhotoImage(img4)
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


limg1.bind('<Button-1>', key)
limg2.bind('<Button-1>', key)
limg3.bind('<Button-1>', key)
limg4.bind('<Button-1>', key)



root.mainloop()