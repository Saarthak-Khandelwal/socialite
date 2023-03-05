from random import *
import mysql.connector as sql
import tkinter 
from customtkinter import *
from time import *

from moduleOwn import *


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

def main():
    pass

def clearPageu():
    for widget in app.winfo_children():
        widget.destroy()







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
        
def rpage(pry,ude):
    clearPageu()

    rid = pry[0]
    rname = pry[1]
    price = pry[2]
    fare = pry[3]
    type = pry[4]
    ratingo = pry[5]
    starttime = pry[6]
    rpno = pry[7]
    attribute = pry[8]
    
    backButton = CTkButton(master=app, text="Go Back", width = 30, command =lambda: mainPage(ude) )
    backButton.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

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
    Proceedbutton = CTkButton(master=app, text="Login",width = 30, command=lambda: loginFunction(username, pwd, mainPage))
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
    CreateAccountbutton = CTkButton(master=app, text="Create Account",width = 30, command=lambda: registrationFunction(username, pwd, pno, loginPage) )
    CreateAccountbutton.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)

    # Logo
    app.centrebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

def mainPage(ude):
    clearPageu()
    #logo
    
    uid = ude[1][0]
    pts = ude[2][0]

    con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD, database = DATABASE)
    cur = con.cursor()

    pqry2 = f"select rid,rname,price,fare,type,ratingo,starttime, rpno,attribute from rdetails;"
    cur.execute(pqry2)
    pry2 = cur.fetchall()

    pqry = f'select distinct rid,rname,price,fare,type,ratingo,starttime, rpno,attribute from rdetails order by ratingo desc'
    cur.execute(pqry)
    pry = cur.fetchall()
    
    rid = pry[0]
    rname = pry[1]
    price = pry[2]
    fare = pry[3]
    type = pry[4]
    ratingo = pry[5]
    starttime = pry[6]
    rpno = pry[7]
    attribute = pry[8]

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
    app.tabview.grid(row=1, column=1, padx=(20, 0), pady=(30, 0), columnspan = 3 , sticky="nsew")
    app.tabview.add("Outing Duration")
    app.tabview.add("Budget per person")
    app.tabview.add("Other Filters")
    app.tabview.tab("Outing Duration").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    app.tabview.tab("Budget per person").grid_columnconfigure(0, weight=1)
    app.tabview.tab("Other Filters").grid_columnconfigure(0, weight=1)


    #OutingDurationfilter
    app.optionmenu_1 = CTkOptionMenu(app.tabview.tab("Outing Duration"), dynamic_resizing=False,values=["0-1 hours", "1-2 hours", "2-3 hours"])
    app.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

    #Budgetfilter
    app.optionmenu_2 = CTkOptionMenu(app.tabview.tab("Budget per person"), dynamic_resizing=False,values=["250", "350", "500", "700"])
    app.optionmenu_2.grid(row=0, column=0, padx=30, pady=(20, 10))
    
    #Otherfilter
    app.scrollable_frame = CTkScrollableFrame(app, label_text="Our Reccomendations")
    app.scrollable_frame.grid(row=3, column=1, padx=(20, 11), pady=(20, 0), columnspan = 2, sticky="nsew")
    app.scrollable_frame.grid_columnconfigure(0, weight=1)
    app.scrollable_frame_switches = []
    att=["chill","laid back","live music","dance","ambience","good food","aeshetic","fast food","aeshetic","fast food","North Indian","just coffee","happy","serene","shopping","creative"]
    for i in range(0,14):
        switch = CTkSwitch(master=app.scrollable_frame, text=f"{i}")
        switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        app.scrollable_frame_switches.append(switch)

    #Reccomendations window
    app.scrollable_frame = CTkScrollableFrame(app, label_text="Our Reccomendations")
    app.scrollable_frame.grid(row=3, column=1, padx=(20, 11), pady=(20, 0), columnspan = 2, sticky="nsew")
    app.scrollable_frame.grid_columnconfigure(0, weight=1)
    app.scrollable_frame_switches = []
    for i in range(5):
        switch = CTkButton(master=app.scrollable_frame, text=f"Reccomendation {pry[i][1]}", command= lambda: rpage(pry[i],ude))
        switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        app.scrollable_frame_switches.append(switch)

    #Randomized Reccomendation
    global rand_i
    app.textbox = CTkTextbox(app, width=210,height=10)
    app.textbox.place(x=250,y=500, anchor=tkinter.CENTER)
    app.textbox.insert("1.0", "Reccomendation no "+str(round(100*random())))


mainPage([[1],["Karan"],[40]])
app.mainloop()


#print(app.username.get())