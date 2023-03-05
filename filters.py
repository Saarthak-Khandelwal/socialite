from random import *
import mysql.connector as sql
import tkinter 
from customtkinter import *
from time import *

con = sql.connect(host = 'localhost', user = 'root', password = "bihani123", database = "socialite")
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

''' #OutingDurationfilter
    app.optionmenu_1 = CTkOptionMenu(app.tabview.tab("Outing Duration"), dynamic_resizing=False,values=["0-1 hours", "1-2 hours", "2-3 hours"])

    #Budgetfilter
    app.optionmenu_2 = CTkOptionMenu(app.tabview.tab("Budget per person"), dynamic_resizing=False,values=["250", "350", "500", "700"])'''

'''max_budget = 700
pqry = f"SELECT DISTINCT rid, rname, price, fare, type, ratingo, starttime, rpno, attribute " \
       f"FROM rdetails " \
       f"WHERE price + fare <= {max_budget} " \
       f"ORDER BY ratingo DESC"

cur.execute(pqry)
pry = cur.fetchall()
print(pry)'''''''''

'''user_input = "fast food"
pqry = f"SELECT DISTINCT rid, rname, price, fare, type, ratingo, starttime, rpno, attribute FROM rdetails WHERE attribute IN ('{user_input}') ORDER BY ratingo DESC "
cur.execute(pqry)
pry = cur.fetchall()
print(pry)

lister = []

pqry = f"select distinct rid,attribute from rdetails"
cur.execute(pqry)
pry = cur.fetchall()
print(pry)

for x in pry:
    if not x[1]:
        continue
    l = x[1].split(",")
    for m in l:
        if m == user_input:
            lister.append(x[0])

print(lister)lister = []

pqry = f"select distinct rid,attribute from rdetails"
cur.execute(pqry)
pry = cur.fetchall()
print(pry)

for x in pry:
    if not x[1]:
        continue
    l = x[1].split(",")
    for m in l:
        if m == user_input:
            lister.append(x[0])

print(lister)'''


def search(user_input):
        SEARCH = search.get()
        con = sql.connect(host = 'localhost', user = 'root', password = SQLPASSWORD, database = DATABASE)
        cur = con.cursor()

        SELECT * FROM rdetails WHERE rname,attribute LIKE "('{user_input}')%"  

        pqry3 = f"select rid,rname,price,fare,type,ratingo,starttime, rpno,attribute from rdetails;"
        cur.execute(pqry3)
        pry3 = cur.fetchall()
        print(pry3)
user_input = "ne"
search(user_input)lister = []

pqry = f"select distinct rid,attribute from rdetails"
cur.execute(pqry)
pry = cur.fetchall()
print(pry)

for x in pry:
    if not x[1]:
        continue
    l = x[1].split(",")
    for m in l:
        if m == user_input:
            lister.append(x[0])

print(lister)