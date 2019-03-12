import tkinter as tk
from tkinter import messagebox
import mysql.connector as conn
import script as sc 

#basic setting for window
window = tk.Tk()
window.title("Banking App ")
window.minsize(400,300)

#main label 
tk.Label(window,text = " Log In ").pack()

#form 
tk.Label(window, text="Username").place(x = 50,y = 50)
tk.Label(window, text="Last Name").place(x = 50,y = 100)

name = tk.Entry(window)
name.place(x = 150,y = 50)

password = tk.Entry(window,show = '*')
password.place(x = 150,y = 100)

def showData():
	try:
		mydb = conn.connect(
	  		host="localhost",
	  		user="root",
	  		password="",
			database = "BMS"
		)
		rec = 0
		statement = mydb.cursor()
		sql = "SELECT * FROM user WHERE username = '" + str(name.get()) +"' AND password = '"  + str(password.get()) + "'"
		statement.execute(sql)
		rs = statement.fetchall()
		for i in rs:
			print(i)
			rec = 1
		if rec == 0:
			tk.messagebox.showerror("Error","Not a valid login creditials")
		else:
			tk.messagebox.showinfo("Info","Log in success")
		mydb.commit() 	
	except Exception as e:
		print(e)
	
	
tk.Button(window, text='Reset', command = window.quit).place(x = 100, y = 150)
tk.Button(window, text='Log - In', command = showData).place(x = 200, y = 150)

window.mainloop()
