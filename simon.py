import tkinter as tk
import time
import random 
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1080x750")



#header label
headlb = 'Level'
label1 = tk.Label(root,text=headlb,font="arial", width = len(headlb),bg="yellow")
label1.pack()
#End-header label

#load image----------------------------------------------------------------------
img0 = Image.open("images/thuglife.png")
photo0 = ImageTk.PhotoImage(img0)

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

#-----------------------------------------------------------------------
#label with img
limg1 = tk.Label(root,image=photo1)
limg1.place(x=130,y=50)

limg2 = tk.Label(root,image=photo2)
limg2.place(x=610,y=50)

limg3 = tk.Label(root,image=photo3)
limg3.place(x=130,y=400)

limg4 = tk.Label(root,image=photo4)
limg4.place(x=610,y=400)
#-----------------------------------------------------------------------

allimg = [limg1,limg2,limg3,limg4]
photo = [photo1,photo2,photo3,photo4]

status = False
selection = []
pattern = []

#-----------------------------------------------------------------------
def gamestart_animate(idx =0):  
    a = random.randrange(len(allimg))
    pattern.append("img"+str(a))
    allimg[a].config(image=photo5)
    root.after(500,lambda:allimg[a].config(image=photo[a]))
    idx += 1
    if idx < len(allimg)-2:
        root.after(1000,lambda:gamestart_animate(idx))   
    else:
        limg1.bind("<1>", select_img1)
        limg2.bind("<1>", select_img2)
        limg3.bind("<1>", select_img3)
        limg4.bind("<1>", select_img4)
#-----------------------------------------------------------------------
def select_img1(self):
    limg1.config(image=photo5)
    root.after(500,lambda:limg1.config(image=photo1))
    selection.append('img0')
    if pattern == selection:
        root.after(1500,next_pp)

def select_img2(self):
    limg2.config(image=photo5)
    root.after(500,lambda:limg2.config(image=photo2))
    selection.append('img1')
    if pattern == selection:
        root.after(1500,next_pp)

def select_img3(self):
    limg3.config(image=photo5)
    root.after(500,lambda:limg3.config(image=photo3))
    selection.append('img2')
    if pattern == selection:
        root.after(1500,next_pp)

def select_img4(self):
    limg4.config(image=photo0)
    root.after(500,lambda:limg4.config(image=photo4))
    selection.append('img3')
    if pattern == selection:
        root.after(1500,next_pp)
#-----------------------------------------------------------------------
def showscore():
    print("userclick:"+str(selection))
    print("pattern:"+str(pattern))
#-----------------------------------------------------------------------
def next_pp():
    if pattern == selection:
        a = random.randrange(len(allimg))
        allimg[a].config(image=photo5)
        root.after(500,lambda:allimg[a].config(image=photo[a]))
        pattern.append("img"+str(a))
    else:
        pass
    selection.clear()
#-----------------------------------------------------------------------
def checkAns():
    if pattern != selection:
        print("try again")


root.after(2000,gamestart_animate)

btn = tk.Button(root,text="SHOW SCORE",command=showscore).pack(side='bottom')





#root.bind("<Key>",key)





root.mainloop()