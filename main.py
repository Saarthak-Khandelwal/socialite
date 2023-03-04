from random import *
import mysql.connector as sql
from tkinter import *

def main():
    pass

MAIN_TITLE = "Socialite"
SQLPASSWORD = "bihani123"
DIMENSION = "400x600"
BG = "#3b1a73"
TC = "#f6a903"

def  home_page(USERNAME):
    global RC
    RC =1
    root = Tk()
    root.title(MAIN_TITLE)
    #root.geometry(DIMENSION)
    root.option_add("*Button.Background", TC)
    root.configure(bg = BG)
    #root.option_add("Background", "Yellow")

    def deliver(RC, OC = 0):
        global rootc
        if RC:
            root.destroy()
            RC = 0
        if OC:
            rootd.destroy()
        rootc = Tk()
        rootc.option_add("*Button.Background", TC)
        rootc.configure(bg = BG)
        rootc.title(MAIN_TITLE)
        con = sql.connect(host = 'localhost', user = 'root', password = 'bihani123', database = 'amazon_del')
        cur = con.cursor()
        q = f"select loca,rno,time from jobs;"
        cur.execute(q)
        s = cur.fetchall()
        msg = Text(rootc,borderwidth=5,width = 55,height =  3)
        all_files = ""
        for x in s:
            for y in x:
                all_files += str(y)
                all_files += (15-len(str(y)))*" "
            all_files+= "\n"
        msg.insert(END,all_files)
        Pickup = Button(rootc,width=55,text='Pickup',command=lambda: collect(RC,1))

        Pickup.grid(row = 0, columnspan=3 )
        msg.grid(row = 1,rowspan= 10, columnspan=3)


    def collect(RC, OC = 0):
        global rootd
        if RC:
            root.destroy()
            RC = 0
        if OC:
            rootc.destroy()
        rootd = Tk()
        rootd.option_add("*Button.Background", TC)
        rootd.configure(bg = BG)
        rootd.title(MAIN_TITLE)
        time = Entry(rootd,borderwidth=5)
        time.insert(0,'Time as HH:MM')
        loc = Entry(rootd,borderwidth=5)
        loc.insert(0,'Location to deliver')
        
        def submit():
            con = sql.connect(host = 'localhost', user = 'root', password = 'bihani123', database = 'amazon_del')
            cur = con.cursor()
            LOC = loc.get()
            TIME = time.get()
            q = f'insert into  jobs(rno, loca, time) values("{USERNAME}","{LOC}", "{TIME}");'
            cur.execute(q)
            con.commit()
            message.delete('1.0',END)
            message.insert(END, "Data Added Successfully")
            
          
        Submit = Button(rootd,width=55,text='Submit',command=submit)
        Deliver = Button(rootd,width=55,text='Delivery',command=lambda: deliver(RC,1))

        message = Text(rootd,borderwidth=5,width = 55,height =  3)
        message.insert(END,'''Waiting for input''')

        loc.grid(row=0,column=0)
        time.grid(row=0,column=1)
        Submit.grid(row=1,column=0,columnspan=2)
        Deliver.grid(row=2,column=0,columnspan=2)
        message.grid(row=3,column=0,columnspan=2)

    Deliver = Button(root,width=55,text='Delivery',command=lambda: deliver(RC))
    Pickup = Button(root,width=55,text='Pickup',command=lambda: collect(RC))

    Deliver.grid(row=2,column=0,columnspan=2, padx= 10, pady=100)
    Pickup.grid(row=1,column = 0,columnspan=2,padx= 10, pady=10)
    

def reg_page():
    global USERNAME
    root = Tk()
    root.title(MAIN_TITLE)
    root.option_add("*Button.Background", TC)
    root.configure(bg = BG)
    #root.geometry(DIMENSION)

    username = Entry(root,borderwidth=5)
    username.insert(0,'Registration Number')
    mailid = Entry(root,borderwidth=5)
    mailid.insert(0,'Mail ID')
    password = Entry(root,borderwidth=5)
    password.insert(0,'Password')
    message = Text(root,borderwidth=5,width = 55,height =  3)
    message.insert(END,'''Enter UserName and Passwd.
    Register if first time user 
    Login for preexisting account''')

    
    def clearing():
        username.delete(0,END)
        password.delete(0,END)
        mailid.delete(0,END)
        
    def gate():
        USERNAME = username.get()
        PASSWORD = password.get()

        con = sql.connect(host = 'localhost', user = 'root', password = 'bihani123', database = 'amazon_del')
        cur = con.cursor()

        pqry = f"select pass,rno from login where rno = '{USERNAME}';"
        cur.execute(pqry)
        pry = cur.fetchall()

        if pry:
            #print(pry[0][0], PASSWORD, pry[0][1])
            if pry[0][0] == PASSWORD:
                root.destroy()
                home_page(USERNAME)

            elif PASSWORD != pry[0][0]:
                message.delete('1.0',END)
                message.insert(END,'Incorrect Password')
            else:
                message.delete('1.0',END)
                message.insert(END,'Error')
        else:
            message.delete('1.0',END)
            message.insert(END,'Invalid Username. Try again or Register')

    def registeration():
        
        USERNAME = username.get()
        PASSWORD = password.get()
        MAILID = mailid.get()

        con = sql.connect(host = 'localhost', user = 'root', password = 'bihani123', database = 'amazon_del')
        cur = con.cursor()

        pqry = f"select pass from login where rno = '{USERNAME}';"
        cur.execute(pqry)
        pry = cur.fetchall()

        print (pry)
        if pry :
            if PASSWORD == pry[0][0]:
                gate()
            else:
                message.delete('1.0',END)
                message.insert(END,'Rno already exists')
        else:
            q = f'insert into login (rno, pass, mailid) values("{USERNAME}","{PASSWORD}", "{MAILID}");'
            cur.execute(q)
            con.commit()
            message.delete('1.0',END)
            message.insert(END,'Successfully Registered ! Click Login')
        
    login = Button(root,width=55,text='Login',command=gate)
    clear = Button(root,width=55,text='Clear',command=clearing)
    register = Button(root, width = 55, text = 'Register', command = registeration)

    username.grid(row=0,column=0)
    password.grid(row=0,column=1)
    mailid.grid(row=0, column=2 )
    login.grid(row=3,column=0,columnspan=3)
    clear.grid(row=4,column=0,columnspan=3)
    register.grid(row=2,column=0,columnspan=3)
    message.grid(row=1,column = 0,columnspan=3)
        
    root.mainloop()

reg_page()

main()