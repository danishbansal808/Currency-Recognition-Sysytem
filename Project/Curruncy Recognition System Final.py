#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from playsound import playsound
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Currency Recognition App")
#window.geometry('1000x1000')
window.configure(bg = '#d9d9d9')
window.resizable(width=True, height=True)
file=[]
model=[]

label=tk.Label(window,text="CURRENCY RECOGNITION SYSTEM",font=('ROBOTO',40),fg = "red")#LAbel Making
label.grid(column=0,row=0)
def loadmodel():
    from numpy import loadtxt
    from keras.models import load_model
    import tensorflow as tf
    model.append(tf.keras.models.load_model('H:/Currency Recognition System/Experiments/Final Experiment/curruncyrecognition2.h5'))
    label1.configure(text="MODEL LOADED")    
    
bt1= Button (window,text='LOAD MODEL',command=loadmodel)
bt1.grid(column=1,row=3)
label1=tk.Label(window,text='Load Model',font=('ROBOTO',20));
label1.grid(column=0,row=3)
def selectfile():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select jpg file")
    label2.configure(text=filename)
    file.append(filename)
    label3.configure(text="")
bt2= Button (window,text='Select File',command=selectfile)#fg-->foreground color||bg-->background color
bt2.grid(column=1,row=4)
label2=tk.Label(window,text='Select Image File',font=('ROBOTO',20));
label2.grid(column=0,row=4)
# def open_img():
#     x = file[0]
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(window, image=img)
#     panel.image = img
#     panel.pack()
# bt4= Button (window,text='Show Image',command=open_img)#fg-->foreground color||bg-->background color
# bt4.grid(column=2,row=4)
def predection():
    import numpy as np
    from keras.preprocessing import image
    path = file[0]
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = model[0].predict(x)
    if(classes[0,0]==1):
        pred='Fifty'
        playsound('H:/Currency Recognition System/Project/Audios/fifty.mp3')
    if(classes[0,1]==1):
        pred='Five Hundred'
        playsound('H:/Currency Recognition System/Project/Audios/fivehundred.mp3')
    if(classes[0,2]==1):
        pred='Hundred'
        playsound('H:/Currency Recognition System/Project/Audios/hundred.mp3')
    if(classes[0,3]==1):
        pred='Ten'
        playsound('H:/Currency Recognition System/Project/Audios/ten.mp3')
    if(classes[0,4]==1):
        pred='Thousand'
        playsound('H:/Currency Recognition System/Project/Audios/thousand.mp3')
    if(classes[0,5]==1):
        pred='Twenty'
        playsound('H:/Currency Recognition System/Project/Audios/twenty.mp3')
    label3.config(text=pred)
    file.pop()
    label2.configure(text="Select Image File")
bt3= Button (window,text='Make Prediction',command=predection)#fg-->foreground color||bg-->background color
bt3.grid(column=1,row=5)
label3=tk.Label(window,text='',font=('ROBOTO',20));
label3.grid(column=0,row=5)
window.mainloop()


# In[ ]:




