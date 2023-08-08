from tkinter import *
from PIL import ImageTk,Image
import os

def next_change():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

counter=1
root = Tk()
root.title('Wallpaper Application')
root.geometry('275x425')
root.configure(background='pink')

text_label = Label(root,text='Wallpaper Viewer',fg='black',bg='pink')
text_label.pack(pady=(10,10))
text_label.config(font=('verdana',16))

files = os.listdir('wallpaper_application/wallpapers')

img_array=[]
for file in files:
    img = Image.open(os.path.join('wallpaper_application/wallpapers',file))
    resize_img = img.resize((200,300))
    img = ImageTk.PhotoImage(resize_img)
    img_array.append(img)

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(10,10))

next_btn = Button(root,text='Next',fg='black',bg='pink',width=30,command=next_change)
next_btn.pack(pady=(5,10))


root.mainloop()