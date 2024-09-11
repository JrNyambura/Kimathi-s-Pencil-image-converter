from tkinter import *
from tkinter import Tk, ttk
from tkinter import filedialog as fd

from PIL import Image, ImageTk

import cv2


#colors
c0="#ffffff"
c1="#000000"
c2="#63b9ff"

window = Tk()
window.title("")
window.geometry("300x356")
window.configure(background=c0)
window.resizable(width=FALSE, height=FALSE)

global original_img, l_img, img 

original_img = ['']

def choose_img():
    global original_img, l_img, img
    img = fd.askopenfilename()
    original_img.append(img)
    
    img = Image.open(img)
    img = img.resize((110, 200))
    img = ImageTk.PhotoImage(img)
    
    l_image = Label(window, image = img, bg=c0, fg=c1)
    l_image.place(x=60, y=60)
    
    
    
def convert_img():
    global original_img, l_img, img
    
    
    scale_value = scale.get()
    
    # load chosen image
    img = cv2.imread(original_img[-1])
    
    
    #convert image one color space to another
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred_img = cv2.GaussianBlur(converted_img, (25, 25), 300, 300)
    
    
    img_to_pencil = cv2.divide(converted_img, blurred_img, scale = scale_value)
    
    cv2.imwrite('saved_img.png', img_to_pencil) 
    
    img = Image.open('saved_img.png')
    img = img.resize((110, 200)) 
    img = ImageTk.PhotoImage(img)
    
    l_image = Label(window, image = img, bg=c0, fg=c1)
    l_image.place(x=60, y=60)
    
stlye = ttk.Style(window)
stlye.theme_use("clam")

app_img = Image.open("image.jpg")
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo =Label(window, image=app_img, text="Img to pencil drawing", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('System 15 bold'), bg=c1)
app_logo.place(x=0, y=0)

l_options = Label(window, text="Settings-----------------------------------------------".upper(), anchor=NW, font=('Arial 10 bold'), bg=c0, fg=c1)
l_options.place(x=10, y=260)

scale = Scale(window, from_=0, to=255, length=120, bg=c0, fg='red', orient=HORIZONTAL)
scale.place(x=10, y=300)

b_choose = Button(window, text="Select Image", command=choose_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=c2, fg=c1)
b_choose.place(x=147, y=287)

b_save = Button(window, text="Save Image", command=convert_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=c2, fg=c1)
b_save.place(x=147, y=323)

window.mainloop()