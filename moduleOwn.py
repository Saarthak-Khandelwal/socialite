from random import *
import mysql.connector as sql
import tkinter 
from customtkinter import *
from time import *


MAIN_TITLE = "Socialite"
SQLPASSWORD = "bihani123"
DIMENSION = "360x640"
BG = "#3b1a73"
TC = "#f6a903"
DATABASE = "socialite"
rand_i=1

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = CTk()  # create CTk window like you do with the Tk window
app.geometry(DIMENSION)







#---------------------------------------------------------------------------------------------------------------------
# Login/ Reg Functions
def popMsg(msg):
    top = CTk()  
    text = CTkLabel(master= top,
        text=f"{msg}",
        width=250,)
    text.place(relx= 0.5, rely = 0.3, anchor=tkinter.CENTER)  
    ok = CTkButton(master=top, text="OK", width = 30, command= top.destroy)
    ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    top.mainloop()

def clearPage():
    for widget in app.winfo_children():
        widget.destroy()

def loginFunction(username, password, mainPage ):
    USERNAME = username.get()
    PASSWORD = password.get()

    con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD, database = DATABASE)
    cur = con.cursor()

    pqry = f"select pwd,uid,pts from user where uid = '{USERNAME}';"
    cur.execute(pqry)
    pry = cur.fetchall()

    if pry:
        #print(pry[0][0], PASSWORD, pry[0][1])
        if pry[0][0] == PASSWORD:
            mainPage(pry)

        elif PASSWORD != pry[0][0]:
            popMsg("Invlaid Password")
  
        else:
            print('Error')
    else:
        popMsg("Invlaid Username")

def registrationFunction(username, password, pno,loginPage):
    USERNAME = username.get()
    PASSWORD = password.get()
    PNO = pno.get()

    con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD , database = DATABASE)
    cur = con.cursor()

    pqry = f"select PWD from user where uid = '{USERNAME}';"
    cur.execute(pqry)
    pry = cur.fetchall()

    if pry :
        if PASSWORD == pry[0][0]:
            popMsg("Account already exists")
        else:
            popMsg("Username already exists")
    
    else:
        
        q = f'insert into user (uid, pwd, pno) values("{USERNAME}","{PASSWORD}", "{PNO}");'
        cur.execute(q)
        con.commit()
        loginPage()
        

