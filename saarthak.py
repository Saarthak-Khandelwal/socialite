from random import *
import mysql.connector as sql
import tkinter 
from customtkinter import *
from time import *

def main():
    pass

MAIN_TITLE = "Socialite"
SQLPASSWORD = "bihani123"
DIMENSION = "360x640"
BG = "#3b1a73"
TC = "#f6a903"
DATABASE = "socialite"

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = CTk()  # create CTk window like you do with the Tk window
app.geometry(DIMENSION)

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

def loginFunction(username, password):
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
            mainPage()

        elif PASSWORD != pry[0][0]:
            popMsg("Invlaid Password")
  
        else:
            print('Error')
    else:
        popMsg("Invlaid Username")

def registrationFunction(username, password, pno):
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
            mainPage()
        else:
            popMsg("Username already exists")
    
    else:
        
        q = f'insert into user (uid, pwd, pno) values("{USERNAME}","{PASSWORD}", "{PNO}");'
        cur.execute(q)
        con.commit()
        loginPage()
        
'''''''''''''''
def clearing():
        username.delete(0,END)
        password.delete(0,END)
        mailid.delete(0,END)

'''


def mainLoginPage():
    clearPage()
    # Logo
    app.centrebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    # Previous page button
    registerButton = CTkButton(master=app, text="Register", width = 30, command=registerPage)
    registerButton.place(relx=0.5, rely=0.465, anchor=tkinter.CENTER)

    # Proceed button
    LoginButton = CTkButton(master=app, text="Login",width = 30, command=loginPage)
    LoginButton.place(relx=0.5, rely=0.535, anchor=tkinter.CENTER)

def loginPage():
    #clear page
    clearPage()

    #username txtbox
    username = CTkEntry(app, placeholder_text="Username")
    username.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    #app.entry.grid(row=1, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    #pswrd txtbox
    pwd = CTkEntry(app, placeholder_text="Password")
    pwd.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    #app.entry.grid(row=2, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    # Previous page button
    GoBackToChoicebutton = CTkButton(master=app, text="Go Back", width = 30, command=mainLoginPage)
    GoBackToChoicebutton.place(relx=0.5, rely=0.625, anchor=tkinter.CENTER)

    # Proceed button
    Proceedbutton = CTkButton(master=app, text="Login",width = 30, command=lambda: loginFunction(username, pwd))
    Proceedbutton.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    # Logo
    """
    app.sidebar_frame = CTkFrame(app, width=140, corner_radius=0)
    app.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    """

    app.centrebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

def registerPage():
    
    clearPage()

    #username txtbox
    username = CTkEntry(app, placeholder_text="Enter Username")
    username.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    #app.entry.grid(row=1, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    #pswrd txtbox
    pwd = CTkEntry(app, placeholder_text="Enter Password")
    pwd.place(relx=0.5, rely=0.43, anchor=tkinter.CENTER)
    #app.config(show="*")
    #app.entry.grid(row=2, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    #phno txtbox
    pno = CTkEntry(app, placeholder_text="Enter Phone Number")
    pno.place(relx=0.5, rely=0.51, anchor=tkinter.CENTER)

    # Previous page button
    GoBackToChoicebutton = CTkButton(master=app, text="Go Back", width = 30, command=mainLoginPage)
    GoBackToChoicebutton.place(relx=0.5, rely=0.72, anchor=tkinter.CENTER)

    # CreateAccount button
    CreateAccountbutton = CTkButton(master=app, text="Create Account",width = 30, command=lambda: registrationFunction(username, pwd, pno) )
    CreateAccountbutton.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)

    # Logo
    app.centrebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

def mainPage():
    clearPage()
    #logo
    app.sidebar_frame = CTkFrame(app, width=90, corner_radius=3)
    app.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    app.sidebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.sidebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.grid(row=0, column=0, padx=10, pady=(20, 10))

    #searchbar
    searchbar = CTkEntry(app, width = 50,placeholder_text="Mood kya hai?")
    searchbar.grid(row= 0, column=1, padx=(10, 0), pady=(30, 0), sticky="nsew")
    #app.entry.place(relx=0.5, rely=0.02)

    #searchbutton
    searchButton = CTkButton(master=app, text="🔍", width = 10, command=mainLoginPage)
    #searchButton.grid(row=0, column=2, padx=(0, 0), pady=(30, 0), sticky="nsew")
    searchButton.place(x=290, y=44, anchor=tkinter.CENTER)

    #tabview code
    app.tabview = CTkTabview(app, width=250, height=100)
    app.tabview.grid(row=1, column=1, padx=(20, 0), pady=(30, 0), columnspan = 2 , sticky="nsew")
    app.tabview.add("Outing Duration")
    app.tabview.add("Budget per person")
    app.tabview.tab("Outing Duration").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    app.tabview.tab("Budget per person").grid_columnconfigure(0, weight=1)


    #OutingDurationfilter
    app.optionmenu_1 = CTkOptionMenu(app.tabview.tab("Outing Duration"), dynamic_resizing=False,values=["0-1 hours", "1-2 hours", "2-3 hours"])
    app.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

    #Budgetfilter
    app.optionmenu_2 = CTkOptionMenu(app.tabview.tab("Budget per person"), dynamic_resizing=False,values=["250", "350", "500", "700"])
    app.optionmenu_2.grid(row=0, column=0, padx=30, pady=(20, 10))

    #Reccomendations window
    app.scrollable_frame = CTkScrollableFrame(app, label_text="Our Reccomendations")
    app.scrollable_frame.grid(row=3, column=1, padx=(20, 11), pady=(20, 0), columnspan = 2, sticky="nsew")
    app.scrollable_frame.grid_columnconfigure(0, weight=1)
    app.scrollable_frame_switches = []
    for i in range(5):
        switch = CTkButton(master=app.scrollable_frame, text=f"Reccomendation no {i}")
        switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        app.scrollable_frame_switches.append(switch)


    #Randomized Reccomendation
    '''
    for i in range(0,100):
        if i<50:
            sleep(0.03)
            app.textbox = CTkTextbox(app, width=200)
            app.textbox.place(x=0,y=0, anchor=tkinter.CENTER)
            app.textbox.insert("0.0", "Reccomendation no",random())
            app.textbox.destroy()
        if i>=50 and i<85:
            sleep(0.2)
            app.textbox = CTkTextbox(app, width=200)
            app.textbox.place(x=0,y=0, anchor=tkinter.CENTER)
            app.textbox.insert("0.0", "Reccomendation no",random())
            app.textbox.destroy()
        if i>=85 and i<95:
            sleep(0.4)
            app.textbox = CTkTextbox(app, width=200)
            app.textbox.place(x=0,y=0, anchor=tkinter.CENTER)
            app.textbox.insert("0.0", "Reccomendation no",random())
            app.textbox.destroy()
        if i>=95 and i<=100:
            sleep(0.4)
            app.textbox = CTkTextbox(app, width=200)
            app.textbox.place(x=0,y=0, anchor=tkinter.CENTER)
            app.textbox.insert("0.0", "Reccomendation no",random())
            app.textbox.destroy()
    '''
    app.textbox = CTkTextbox(app, width=210,height=20)
    app.textbox.place(x=250,y=500, anchor=tkinter.CENTER)
    app.textbox.insert("0.0", "Reccomendation no",random())


mainPage()
app.mainloop()


#print(app.username.get())