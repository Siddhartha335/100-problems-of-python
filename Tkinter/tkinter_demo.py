from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    # print(email,password)
    if email == 'siddhartharaut33@gmail.com' and password == 'sid@123':
        messagebox.showinfo('Yayy!, Login successful')
    else:
        messagebox.showerror('Error!, Login failed')


root = Tk()

root.title('Login form')
# root.iconbitmap(default='favicon.ico')
# root.minsize(400,400)
root.geometry('350x500')

root.configure(background='#0096DC')

img = Image.open('digisolve-logo.png')
resized_img = img.resize((80,80))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)

img_label.pack(pady=(10,10))

text_label = Label(root,text='Digisolve',fg='white', bg='#0096DC')

text_label.pack()
text_label.config(font=('verdana',20))

email_label = Label(root,text='Enter email', fg='white', bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=40)
email_input.pack(ipady=4, pady=(1,15))

password_label = Label(root,text='Enter password', fg='white', bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=40)
password_input.pack(ipady=4,pady=(1,15))

login_button = Button(root,text='Login', bg='white', fg='black',width=15,command=handle_login)
login_button.pack(pady=(10,20))
login_button.config(font=('verdana',14))

root.mainloop()
