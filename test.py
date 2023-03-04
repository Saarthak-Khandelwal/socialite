import tkinter
from customtkinter import *
top = CTk()  
text = CTkLabel(master= top,
    text="Invlaid Password",
    width=250,)
    
#text.insert(END, "")  

text.place(relx= 0.5, rely = 0.3, anchor=tkinter.CENTER)  
ok = CTkButton(master=top, text="Register", width = 30, command= top.destroy)
ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
top.mainloop()