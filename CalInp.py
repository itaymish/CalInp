try:
	from tkinter import *
	import tkinter as tk
	import tkinter
	from tkinter import messagebox
except ImportError:
	from Tkinter import *
	from Tkinter import messagebox

def code():
	global cct

	root = Tk()
	root.title("CalInp")

	hlp = Label(root, text="Enter a number - Any number.\nEnter an operator - +, -, * and /.\nEnter another number - Any number.")
	hlp.grid()

	fnum = Entry(root, width=30)
	fnum.grid()

	oper = Entry(root, width=30)
	oper.grid()
       
	snum = Entry(root, width=30)
	snum.grid()                                                 

	def calcul():
		global rslt
		global rval

		fval = fnum.get()
		oval = oper.get()
		sval = snum.get()

		if oval == '+':
			rval = float(fval) + float(sval)
		elif oval == '-':
			rval = float(fval) - float(sval)
		elif oval == '*':
			rval = float(fval) * float(sval)
		elif oval == '/':
			rval = float(fval) / float(sval)

		messagebox.showinfo("CalInp", "The answer is...\n" + str(rval))

		rval = 0

	def clear():
		fnum.delete(0, END)
		fnum.insert(0, "")

		oper.delete(0, END)
		oper.insert(0, "")

		snum.delete(0, END)
		snum.insert(0, "")

	cal = Button(root, text="Calculate", command=calcul)
	cal.grid()

	clr = Button(root, text="Clear", command=clear)
	clr.grid()

	root.mainloop()

code()
