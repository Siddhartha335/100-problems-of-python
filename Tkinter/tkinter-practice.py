from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'siddhartharaut33@gmail.com' and password == 'sid@123':
        messagebox.showinfo('Good! Login succesful')
    else:
        messagebox.showerror('Error! Login failed!')
        

root = Tk()
root.title('Login form by Sid')

# root.iconbitmap('favicon.ico')
# root.minsize(100,100)

root.geometry('350x500')

root.configure(background='#ed07b7')

img = Image.open('digisolve-logo.png')
resized_img = img.resize((80,80))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text='Digisolve',fg='white',bg='#ed07b7')
text_label.pack(pady=(10,10))
text_label.config(font=('verdana',20))

email_label = Label(root,text='Enter email',fg='white',bg='#ed07b7')
email_label.pack(pady=(10,10))
email_label.config(font=('verdana',14))

email_input = Entry(root,width=45)
email_input.pack(ipady=4,pady=(1,15))

password_label = Label(root,text='Enter password',fg='white',bg='#ed07b7')
password_label.pack(pady=(10,10))
password_label.config(font=('verdana',14))

password_input = Entry(root,width=45)
password_input.pack(ipady=4,pady=(1,15))


login_button = Button(root,text='Login',fg='white',bg='#ed07b7',width=15, command=handle_login)
login_button.pack(pady=(1,25))
login_button.config(font=('verdana',14))


root.mainloop()