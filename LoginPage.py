#creating login page
from tkinter import *
# from urllib.request import urlopen
# import sqlite3
import os
import tkinter.messagebox as tm
# FileName = "RegistrationData.db"
# TableName = "RegistrationDetails"

def LoginClick():
	Content = os.system('curl "http://192.241.244.177/ChatApplication/CheckLogin.php?UserId=" + UserId.get() + "Password=" + Password.get()"')
	for Attributes in Content:
		print(Attributes)
		# if Attributes == 1:
		# 	tm.showinfo("Login info", "Successfully logged in")
		# else:
		# 	tm.showerror("Login error", "Invalid details")
	# Counter = 0
	# Connection = sqlite3.connect(FileName)
	# SelectQuery = "SELECT UserId, Password FROM " + TableName 
	# Result = Connection.execute(SelectQuery)
	# for Attributes in Result:
	# 	# print(Attributes)
	# 	if Attributes[0] == UserId.get() and Attributes[1] == Password.get():
	
	# 		# Counter = 1
	# # if Counter == 0:
		

root = Tk(className = "Login Page")
root.geometry("500x500")
Welcome = Label(root, text = "Welcome", font = 50).grid(row = 0,column = 1)
UserId = Label(root, text = "User Id").grid(row = 1)
Password = Label(root, text = "Password").grid(row = 2)
UserId = Entry(root)
Password = Entry(root, show = "*")
UserId.grid(row = 1, column = 1)
Password.grid(row = 2, column = 1)
Login = Button(root, text = "Login", fg = "blue", command = LoginClick).grid(row = 3, column = 1)
root.mainloop()
