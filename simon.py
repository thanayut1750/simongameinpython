import tkinter as tk
import csv
import random 
from tkinter import messagebox
from playsound import playsound
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1080x750")

#header label

level = 1
headlb = 'L  e  v  e  l    '+str(level)
levellb = tk.Label(root,text=headlb,font="arial 30 bold", width = len(headlb),bg="yellow")
levellb.pack(fill='x')



highest_score = tk.Label(root,text="Highest LEVEL : " ,font="arial 13",bg="yellow")
highest_score.place(x=10,y=15)

#End-header label


#load sound
#----------------------------------------------------------------------
def sound_img0():
    playsound("sound\img0.mp3")

def sound_img1():
    playsound("sound\img1.mp3")

def sound_img2():
    playsound("sound\img2.mp3")

def sound_img3():
    playsound("sound\img3.mp3")

def sound_wrong():
    playsound("sound\wrong.mp3")
#----------------------------------------------------------------------
   

#load image
#----------------------------------------------------------------------
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
#----------------------------------------------------------------------
limg1 = tk.Label(root,image=photo1)
limg1.place(x=130,y=50)

limg2 = tk.Label(root,image=photo2)
limg2.place(x=610,y=50)

limg3 = tk.Label(root,image=photo3)
limg3.place(x=130,y=400)

limg4 = tk.Label(root,image=photo4)
limg4.place(x=610,y=400)
#-----------------------------------------------------------------------

#Variable
#----------------------------------------------------------------------
allimg = [limg1,limg2,limg3,limg4]
photo = [photo1,photo2,photo3,photo4]

selection = []
pattern = []
#-----------------------------------------------------------------------

#**************************ALL MAIN FUNCTION***************************

def update_hscore():
    highest_sc = []
    with open("scorerec.csv",'rt') as read_score:
        read = csv.reader(read_score)
        next(read)
        next(read)
        for i in read:
            next(read)
            highest_sc.append(i[0])
        aa = max(highest_sc)
        highest_score.configure(text="Highest LEVEL : "+aa)

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

def select_img1(self):
    sound_img0()
    limg1.config(image=photo5)
    root.after(200,lambda:limg1.config(image=photo1))
    selection.append('img0')
    if pattern == selection:
        root.after(1500,next_pp)
    checkAns()

def select_img2(self):
    sound_img1()
    limg2.config(image=photo5)
    root.after(200,lambda:limg2.config(image=photo2))
    selection.append('img1')
    if pattern == selection:
        root.after(1500,next_pp)
    checkAns()

def select_img3(self):
    sound_img2()
    limg3.config(image=photo5)
    root.after(200,lambda:limg3.config(image=photo3))
    selection.append('img2')
    if pattern == selection:
        root.after(1500,next_pp)
    checkAns()

def select_img4(self):
    sound_img3()
    limg4.config(image=photo0)
    root.after(200,lambda:limg4.config(image=photo4))
    selection.append('img3')
    if pattern == selection:
        root.after(1500,next_pp)
    checkAns()

def csv_save_score():
    with open('scorerec.csv' ,'a') as scr:
        scr = csv.writer(scr)
        scr.writerow([level,len(selection)])   

def next_pp():
    if pattern == selection:
        a = random.randrange(len(allimg))
        allimg[a].config(image=photo5)
        root.after(500,lambda:allimg[a].config(image=photo[a]))
        pattern.append("img"+str(a))
        levelup()
    else:
        pass
    selection.clear()

def checkAns():
    global pattern,selection
    for i,y in zip(pattern,selection):
        if i == y:
            pass
        else:
            pattern.clear()
            global level
            global headlb
            sound_wrong()
            pattern.clear()
            selection.clear()
            limg1.unbind("<1>")
            limg2.unbind("<1>")
            limg3.unbind("<1>")
            limg4.unbind("<1>")
            ermessage = ["ปั๊ดโถ่ จำดิจำ","รัฐประหาร อะจำดิ","STUPID","เรือดำนํ้า"]
            b = random.randrange(4)
            messagebox.showinfo("ข้อแนะนำ", ermessage[b])
            level = 1
            headlb = 'L  e  v  e  l    '+str(level)
            levellb.configure(text=headlb)

def levelup():
    global level
    global headlb
    level += 1
    headlb = 'L  e  v  e  l    '+str(level)
    levellb.configure(text=headlb)
    csv_save_score()
    update_hscore()
#-----------------------------------------------------------------------
#**************************ALL MAIN FUNCTION***************************

btn = tk.Button(root,text="START",font="arial 40 bold",command=gamestart_animate).pack(side='bottom')
root.mainloop()