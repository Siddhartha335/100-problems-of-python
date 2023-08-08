from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

counter=1
root = Tk()
root.title('Wallpaper Viewer')
root.geometry('275x400')
root.configure(background='black')

text_label = Label(root,text="Wallpaper Viewer",fg='white',bg='black')
text_label.pack(pady=(5,5))
text_label.config(font=('verdana',14))

files = os.listdir('wallpaper_application/wallpapers')
img_array=[]
for file in files:
    img = Image.open(os.path.join('wallpaper_application/wallpapers',file))
    resized_img = img.resize((200,300))
    img = ImageTk.PhotoImage(resized_img)
    img_array.append(img)

# print(img_array)

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(5,5))

next_btn = Button(root,text='Next', bg='white',fg='black',width=10,command=rotate_image)
next_btn.pack(pady=(7,1))

root.mainloop()