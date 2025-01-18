from tkinter import *
import tkinter as tk
window=Tk()
window.geometry("1352x740")
window.title('phone book version 0.001')
# to change icon of windows
icon = PhotoImage(file='qrt.png')
window.iconphoto(True,icon)
##DEFINED FUNCTIONS OF VARIOUS BUTTONS
def save():
     
     contact_name=entry_NAME.get()
     print('NAME : '+contact_name+"'s details saved")
     contact_num=entry_num.get()
     print('phone number : '+contact_num)
     contact=entry_lacation.get()
     print('location : '+contact)
     email=entry_email.get()
     print('email adress:'+ email)
     f=open('contacts.dat', 'a')
     f.write('  name: '+ entry_NAME.get())
     f.write('  phone number : '+ entry_num.get())
     f.write('  location: '+ entry_lacation.get())
     f.write('  email@: '+ entry_email.get())
     f.close()
     f=open('contacts.dat','r')
     print(f.read() +"  saved                                            ")
     
# DISPLAYS FOR THE SCREEN
phone_book_label=Label(window,text='phone book',font=('ink free',40,'bold'),fg='red',bg='blue')
label_NAME=Label(window,text='NAME')
entry_NAME=Entry(window)

label_location=Label(window,text="LOCATION")
entry_lacation=Entry(window)
label_email=Label(window,text="EMAIL ADDRES")
entry_email=Entry(window)
label_num=Label(window,text=' PHONE NUMBER')
entry_num=Entry(window)

button=Button(window,text="SAVE CONTACT",command=save)
##if label_NAME== :
##     tk.Label(window, text=str('saved')).grid(row=9, column=4)
##else:
##     tk.Label(window, text=str('notsaved')).grid(row=9, column=4)

#  GRID FOR POSITIONING
label_NAME.grid(row=2,column=0)
entry_NAME.grid(row=3, column=0)

phone_book_label.grid(row=0, column=10)
label_location.grid(row=4, column=0)
entry_lacation.grid(row=5, column=0)
label_email.grid(row=2, column=10)
entry_email.grid(row=3, column=10)
label_num.grid(row=6, column=0)
entry_num.grid(row=7, column=0)
button.grid(row=8, column=10)



def submit():
     username =entry.get()
     f=open('contacts.dat','r')
     print(f.read())
     

def delete():
     entry.delete(0,END)

def backspace():
     entry.delete(len(entry.get())-1,END) 

     
submit=Button(window,text="search for contacts",command=submit)
submit.config(fg='red')
submit.config(fg='blue')

delete=Button(window,text="delete",command=delete)
delete.config(fg='red')
delete.config(fg='blue')

backspace=Button(window,text="backspace",command=backspace)
backspace.config(fg='red')
backspace.config(fg='blue')

entry = Entry()
entry.config(font=('ink free',10))
entry.config(fg='blue')
entry.config(bg='red')
entry.insert(80,'SEARCH FOR CONTACTS')
##entry.config(width=40)

backspace.grid(row=1,column=1)
submit.grid(row=1,column=3)
delete.grid(row=1,column=2)
entry.grid(row=1,column=0)
window.mainloop()
