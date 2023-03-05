from random import *
import mysql.connector as sql
import tkinter 
from customtkinter import *
from time import *
import datetime
from PIL import Image
import os

MAIN_TITLE = "Socialite"
SQLPASSWORD = "bihani123"
DIMENSION = "360x640"
BG = "#3b1a73"
TC = "#f6a903"
DATABASE = "socialite"
rand_i=1
att=["chill","laid back","live music","dance","ambience","good food","aeshetic","fast food","aeshetic","fast food","North Indian","just coffee","happy","serene","shopping","creative"]
TEMP = [(9, 'Idam', 100, None, 'hangout, live music, light,beverages,snacks', 5.0, datetime.timedelta(seconds=64800), None, 'live music,dance,ambience'), (17, "Nesam's", 150, 300, 'Craft Boutique,Native Groceries,Handmade Accessories', 5.0, datetime.timedelta(seconds=36000), '7200998882', 'serene,shopping,creative'), (15, 'LXG', 130, None, 'Gaming,Fun,Hangout,AC', 4.7, datetime.timedelta(seconds=25200), '9884035135', 'chill,laidback,happy'), (3, 'Hot Stone Kitchen', 200, None, 'Italian,Pizza,Burger,Fast food', 4.4, datetime.timedelta(seconds=43200), '9962676676', 'ambience,fast food,chill'), (8, 'McDonald?s', 250, 100, 'Burger,Fast food', 4.4, datetime.timedelta(seconds=36900), '9994180481', 'fast food, good food,laidback'), (14, 'Miniso', 500, 350, 'In-Store Shopping,Stationery,Perfumes,Bags,Gifts', 4.4, datetime.timedelta(seconds=37800), '6383746815', 'shopping,happy')]
pry = TEMP


set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = CTk()  # create CTk window like you do with the Tk window
app.geometry(DIMENSION)


    

def clearPageu():
    for widget in app.winfo_children():
        widget.destroy()
    background()

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
    background()

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
        attributeSelectionPage(USERNAME)
        
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

    # Logo
    '''
    app.sidebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.sidebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.sidebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
    '''
    # Name of restaurant 
    app.centrebar_frame = CTkFrame(app, width=360, height= 180,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

    app.res_group = CTkLabel(master=app.centrebar_frame,text=f"{rname}",font = CTkFont(size = 30, weight ="bold"))
    app.res_group.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nsew")

    #tabview
    app.tabview = CTkTabview(app, width=150, height=50)
    app.tabview.place(relx = 0.5,rely=0.4,anchor=tkinter.CENTER)
    app.tabview.add("General Info")
    app.tabview.add("Reviews")
    app.tabview.tab("General Info").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    app.tabview.tab("Reviews").grid_columnconfigure(0, weight=1)
    #General Info
    """
    app.textbox = CTkTextbox(app.tabview.tab("General Info"), width=250)
    app.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    app.textbox.insert("0.0", "Type:\n\n" + f"{type}"+"\n\nCost:\n\n" + f"₹{price}"+"\n\nFare:\n\n" + f"₹{fare}")
    """
    text = CTkLabel(master= app.tabview.tab("General Info"),
        text="Type:\n\n" + f"{type}"+"\n\nCost:\n\n" + f"₹{price}"+"\n\nFare:\n\n" + f"₹{fare}",
        width=250,)
    text.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    
        #rating bar
    app.slider_progressbar_frame = CTkFrame(app.tabview.tab("General Info"), fg_color="transparent")
    app.slider_progressbar_frame.grid(row=4, column=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
    app.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
    app.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
    app.progressbar_2 = CTkProgressBar(app.slider_progressbar_frame)
    app.progressbar_2.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
    app.progressbar_2.set(ratingo/5)
    app.res_group = CTkLabel(master=app.slider_progressbar_frame,text="Rating:")
    app.res_group.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="") 
    #Reviews
    app.optionmenu_2 = CTkOptionMenu(app.tabview.tab("Reviews"), dynamic_resizing=False,values=["250", "350", "500", "700"])
    app.optionmenu_2.grid(row=0, column=0, padx=30, pady=(20, 10))
    
    #back button
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
    username.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
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
    app.centrebar_frame.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

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
    CreateAccountbutton = CTkButton(master=app, text="Create Account",width = 30, command=lambda: registrationFunction(username, pwd, pno, attributeSelectionPage))
    CreateAccountbutton.place(relx=0.5, rely=0.66, anchor=tkinter.CENTER)

    # Logo
    app.centrebar_frame = CTkFrame(app, width=140, height= 80,corner_radius=0)
    app.centrebar_frame.place(relx=0.5, rely=0, anchor=tkinter.CENTER)
    #app.centrebar_frame.grid_rowconfigure(4, weight=1)
    app.logo_label = CTkLabel(app.centrebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

def attributeSelectionPage(USERNAME):
    clearPage()
    listOfAt = []
    
    #checkboxes
    app.attriList = []
    m=0
    n=0
    ct=0
    '''
    app.scrollable_frame = CTkScrollableFrame(app, label_text="What's on your mind?")
    app.scrollable_frame.grid(row=8, column=4, padx=(40, 0), pady=(80, 0), sticky="nsew",rowspan=3,columnspan=4)
    app.scrollable_frame.grid_columnconfigure(0, weight=1)
    '''
    app.att_frame = CTkFrame(app)
    #app.att_frame.grid(row=0, column=0, columnspan = 10, padx=(20, 0), pady=(20, 0), sticky="nsew")
    app.att_frame.place(relx = 0.5, y = 35, anchor = tkinter.CENTER)
    app.att_group = CTkLabel(master=app.att_frame, text="What's on your mind?")
    app.att_group.grid(row=0, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")
    att_choice=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    #Reccomendations window
    app.scrollable_frame = CTkScrollableFrame(app, width = 250, height = 350)
    app.scrollable_frame.place(relx = 0.12, rely = 0.12)
    #app.scrollable_frame.grid_columnconfigure(0, weight=1)
    app.scrollable_frame_chk = []
    
    def chktoggle(k):
        listOfAt.append(att[k])
        #print(listOfAt)
        
        # if len(listOfAt)>1:
        #     print (True)
        #     for i in range(14):
        #         if(chk[i].get()==0):
        #             chk[i].configure(state="disabled")
        # elif len(listOfAt)<=2:
        #     for i in range(14):
        #         chk[i].configure(state="enabled")
    
    def submitAt():
        stri = ""
        
        for x in range(len(listOfAt)):
            if x ==0:
                stri = listOfAt[x]
            else:
                stri += f",{listOfAt[x]}"
        
        con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD, database = DATABASE)
        cur = con.cursor()

        pqry2 = f"update user set attributeu = '{stri}' where uid = '{USERNAME}';"
        #insert into user (uid, pwd, pno) values("{USERNAME}","{PASSWORD}", "{PNO}");
        cur.execute(pqry2)
        con.commit()
        mainPage(pry)

    chk = dict()
    for i in range(7):
        chk[i] = CTkCheckBox(master=app.scrollable_frame,text=f"{att[i]}",command= lambda k=i: chktoggle(k))
        chk[i].grid(row=i+2, column = 0, padx=10, pady=(0, 30))
        app.scrollable_frame_chk.append(chk[i])
    
    for i in range(7,14):
        chk[i] = CTkCheckBox(master=app.scrollable_frame,text=f"{att[i]}",command= lambda k=i: chktoggle(k))
        chk[i].grid(row=i+2 -7, column = 1, padx=10, pady=(0, 30))
        app.scrollable_frame_chk.append(chk[i])
    
    
    # Proceed button
    LoginButton = CTkButton(master=app, text="Login",width = 30, command=submitAt)
    LoginButton.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
    

def mainPage(ude):
    clearPageu()
    #logo

    ude = ude
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
    
    #top sidebar
    app.sidebar_frame = CTkFrame(app, width=90, height = 600, corner_radius=5)
    app.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew",pady = (20,20))
    app.sidebar_frame.grid_rowconfigure(4, weight=1)
    
    #app.sidebar_frame.place(x=50, y=20, anchor=tkinter.CENTER)

    app.logo_label = CTkLabel(app.sidebar_frame, text="SocialIte", font=CTkFont(size=20, weight="bold"))
    app.logo_label.grid(row=0, column=0, padx=10, pady=(15, 10), sticky= "nsew")
    #app.logo_label.grid_rowconfigure()

    #bottom sidebar
    app.sidebarl_frame = CTkFrame(app, width=90,height = 100, corner_radius=3)
    app.sidebarl_frame.grid(row=6, column=0, rowspan=3, sticky="nsew", pady = (10,10))
    app.sidebarl_frame.grid_rowconfigure(4, weight=1)
    app.pts_label = CTkLabel(app.sidebarl_frame, text=f"  Points \n\n {pts} \n\n 👤\n\n {uid}" , font=CTkFont(size=15, weight="bold"))
    app.pts_label.grid(row=0, column=0, padx=10, pady=(15, 10))

    #searchbar
    searchbar = CTkEntry(app, width = 50,placeholder_text="Mood kya hai?")
    searchbar.grid(row= 0, column=1, padx=(10, 0), pady=(5, 0), sticky="nsew")
    #app.entry.place(relx=0.5, rely=0.02)
    
    def search():
        SEARCH = search.get()
        con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD, database = DATABASE)
        cur = con.cursor()

        pqry3 = f"select rid,rname,price,fare,type,ratingo,starttime, rpno,attribute from rdetails;"
        cur.execute(pqry3)
        pry3 = cur.fetchall()


    def srch():
        searchterm=searchbar.get()
        print(searchterm)

    #searchbutton
    searchButton = CTkButton(master=app, text="🔍", width = 10, command=srch)
    #searchButton.grid(row=0, column=2, padx=(0, 0), pady=(30, 0), sticky="nsew")
    searchButton.place(x=285, y=19, anchor=tkinter.CENTER)

    #tabview code
    app.tabview = CTkTabview(app, width=250, height=100)
    app.tabview.grid(row=1, column=1, padx=(12, 0), pady=(5, 0), columnspan = 3 , sticky="nsew")
    app.tabview.add("Outing Duration")
    app.tabview.add("Budget per person")
    #app.tabview.add("Other Filters")
    app.tabview.tab("Outing Duration").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    app.tabview.tab("Budget per person").grid_columnconfigure(0, weight=1)
    #app.tabview.tab("Other Filters").grid_columnconfigure(0, weight=1)


    #OutingDurationfilter
    app.optionmenu_1 = CTkOptionMenu(app.tabview.tab("Outing Duration"), dynamic_resizing=False,values=["0-1 hours", "1-2 hours", "2-3 hours"])
    app.optionmenu_1.grid(row=0, column=0, padx=20, pady=(10, 5))

    #Budgetfilter
    app.optionmenu_2 = CTkOptionMenu(app.tabview.tab("Budget per person"), dynamic_resizing=False,values=["250", "350", "500", "700"])
    app.optionmenu_2.grid(row=0, column=0, padx=30, pady=(20, 10))
    
    #Otherfilter
    app.scrollable_frame = CTkScrollableFrame(app, height = 80 ,label_text="Our Reccomendations")
    app.scrollable_frame.grid(row=3, column=1, padx=(14, 11), pady=(14, 0), columnspan = 2, sticky="nsew")
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
    '''
    for i in range(5):
        print (pry[i])
        switch = CTkButton(master=app.scrollable_frame, text=f"Reccomendation {pry[i][1]}", command= lambda: rpage(pry[i],ude))
        switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        app.scrollable_frame_switches.append(switch)
    '''
    
    def switchCreator(x):
        switchtr = dict()

        for i in range(x):
            switchtr[i] = CTkButton(master=app.scrollable_frame, text=f"{pry[i][1]}", command= lambda k=i: rpage(pry[k],ude))
            switchtr[i].grid(row=i, column=0, padx=10, pady=(0, 20))
            app.scrollable_frame_switches.append(switchtr[i])

    switchCreator(5)

    def forME():
        pass
        
    



    recButton = CTkButton(master=app, text="For Me", width = 50, command=mainLoginPage)
    recButton.place(relx=0.45, rely=0.95, anchor=tkinter.CENTER)

    # CreateAccount button
    CreateAccountbutton = CTkButton(master=app, text="Trending",width = 50, command=mainLoginPage)
    CreateAccountbutton.place(relx=0.75, rely=0.95, anchor=tkinter.CENTER)

    #Randomized Reccomendation
    global rand_i
    app.textbox = CTkTextbox(app, width=210,height=10)
    app.textbox.place(x=250,y=500, anchor=tkinter.CENTER)
    app.textbox.insert("1.0", "Reccomendation no "+str(randint(0,28)))

def background():
    current_path = os.path.dirname(os.path.realpath(__file__))
    current_path=current_path.replace("\\","/")
    try:
        app.bg_image = CTkImage(Image.open(current_path+"/LETS.png"),size=(360,640))
        app.bg_image_label = CTkLabel(app, image=app.bg_image)
        app.bg_image_label.grid(row=0, column=0)
    except IOError:
        pass

#attributeSelectionPage()
#mainPage([[1], ["karan"], [90]])
#background()
mainLoginPage()
#mainPage([[1],[1],[1]])
app.mainloop()


#print(app.username.get())
