
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from passlib.hash import sha512_crypt
import webbrowser
import os

creds = 'tempfile.temp'

def Signup():

	global roots
	global nameE
	global passwordE

	roots = Tk()
	roots.bind('<Escape>',quit) # for develop k24
	roots.title('demo')
	roots.geometry("800x600")
	roots.focus_set()
	roots.configure(background='#F7F7F7')

	# image = Image.open("src/img/3.jpg")
	# headerF = Frame(roots, width=100, height=100, bg="#F7F7F7", highlightthickness=0, bd= 0)
	# imgTk = ImageTk.PhotoImage(image)
	# header = Label(headerF, image=imgTk)
	# header.pack(side="top")
	# headerF.pack(side="top", padx=5, pady=5)

	nameL = Label(roots, text="Nuevo Usuario", font=("roboto",14), bg="#F7F7F7", fg="#052F6C")
	nameL.pack(side="top")
	nameE = Entry(roots, font=("roboto",12), relief="flat", fg="#052F6C")
	nameE.pack(side="top", padx=5, pady=5)

	passwordL = Label(roots, text="Nueva Contraseña", anchor="center", font=("roboto",14), bg="#F7F7F7", fg="#052F6C")
	passwordL.pack(side="top")
	passwordE = Entry(roots, font=("roboto",12), show="•", relief="flat", fg="#052F6C")
	passwordE.pack(side="top", padx=5, pady=5)

	SignupButton = Button(roots, text="Registrarse", command=FSSignup, 
						  background="#052F6C", relief="flat", 
						  foreground="#F7F7F7", font=("roboto",12),
						  width=10, pady=3, padx=6)
	SignupButton.pack(side="top", padx=5, pady=5)

	footer_frame = Frame(roots, width=30, height=30, bg="#F7F7F7")
	footerL = Text(footer_frame, text="developed by k24", font=("roboto", 8), bg="#F7F7F7")
	footerL.pack(side="right")
	footer_frame.pack(side="bottom", fill="x")

	roots.mainloop()

def FSSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())
		f.write('\n')
		f.write(passwordE.get())
		f.close()

	roots.destroy()
	Login()


def Login():
	global nameE
	global passwordE
	global rootl
	
	rootl = Tk()
	rootl.bind('<Escape>',quit) # for develop k24
	rootl.title('demo')
	rootl.geometry("800x600")
	rootl.focus_set()
	rootl.configure(background='#F7F7F7')

	# title = Label(rootl, text="R.A.WS: M.J", font=("roboto", 24, "bold"), bg="#F7F7F7", fg="#052F6C")
	# title.pack(side="top")	

	# image = Image.open("src/img/3.jpg") # Pueden cambiar entre los distintos tipos de imagenes que prepare cambiando el número
	# headerF = Frame(rootl, width=100, height=100, bg="#F7F7F7", highlightthickness=0, bd= 0)
	# imgTk = ImageTk.PhotoImage(image)
	# header = Label(headerF, image=imgTk)
	# header.pack(side="top")
	# headerF.pack(side="top", padx=5, pady=5)

	nameF = Frame(rootl, bg="#F7F7F7")
	nameF.pack(side="top")
	nameL = Label(nameF, text="Usuario", font=("roboto", 14), bg="#F7F7F7", fg="#052F6C")
	nameL.pack(side="top")
	nameE = Entry(nameF, font=("roboto",12), relief="flat", fg="#052F6C", 
				  highlightbackground="#052F6C", highlightthickness=1, highlightcolor="#052F6C")
	nameE.bind('<Return>', CheckLogin)
	nameE.pack(side="top", padx=5, pady=5)

	passwordF = Frame(rootl, bg="#F7F7F7")
	passwordF.pack(side="top")
	passwordL = Label(passwordF, text="Contraseña", font=("roboto", 14), bg="#F7F7F7", fg="#052F6C")
	passwordL.pack(side="top")
	passwordE = Entry(passwordF, show="•", font=("roboto", 12), relief="flat", fg="#052F6C", 
					  highlightbackground="#052F6C", highlightthickness=1, highlightcolor="#052F6C")
	passwordE.bind('<Return>', CheckLogin)
	passwordE.pack(side="top", padx="5", pady="5")

	LoginButton = Button(rootl, text="Ingresar", command=CheckLogin,
						 background="#052F6C", relief="flat",
						 foreground="#F7F7F7", font=("roboto",12),
						 width=10, pady=3, padx=6)
	LoginButton.pack(side="top", padx=5, pady=5)

	footer_frame = Frame(rootl, width=30, height=30, bg="#F7F7F7")
	verL = Label(footer_frame, text="v1.0", font=("roboto", 8), bg="#F7F7F7") # AQUI VA LA VERSION DE SU SOFTWARE
	verL.pack(side="left")
	aboutL = Label(footer_frame, text="About", font=("roboto", 8), bg="#F7F7F7", fg="#536DFE", cursor="hand2")
	aboutL.bind("<Button-1>", k24_info)
	aboutL.pack(side="right")
	footer_frame.pack(side="bottom", fill="x")

	# ttk.Style().configure("TButton", foreground="red")
	# rmuser = ttk.Button(rootl, text="Delete User", command=DelUser)
	# rmuser.grid(columnspan=2, stick=W)

	rootl.mainloop()

def CheckLogin(*vals):
	if nameE.get() and passwordE.get():
		print(nameE.get())
		sha512_passwd = sha512_crypt.encrypt(passwordE.get(), rounds=5000)
		print(sha512_passwd)
		# Aqui pueden realiar la conexion con su base de datos y comparar los datos

	if not passwordE.get():
		passwordE.focus()
		passwordE.config(highlightbackground="#D50000", highlightcolor="#D50000")
	else:
		passwordE.config(highlightbackground="#052F6C", highlightcolor="#052F6C")

	if not nameE.get():
		nameE.focus()
		nameE.config(highlightbackground="#D50000", highlightcolor="#D50000")
	else:
		nameE.config(highlightbackground="#052F6C", highlightcolor="#052F6C")


def k24_info(*vals):
	rootk = Tk()

	rootk.title('About')

	rootk.geometry("300x150")
	windowWidth = rootk.winfo_reqwidth()
	windowHeight = rootk.winfo_reqheight()
	positionRight = int(rootk.winfo_screenwidth()/2 - windowWidth/2)
	positionDown = int(rootk.winfo_screenheight()/2 - windowHeight/2)

	rootk.geometry("+{}+{}".format(positionRight, positionDown))

	rootk.bind('<Escape>',quit)
	rootk.configure(bg="#F7F7F7")

	mainL = Label(rootk, text="Developed by \n Jesus Rojas", font=("roboto", 12, "bold"), fg="#424242", bg="#F7F7F7")
	mainL.pack(side="top")
	f = Frame(rootk, bg="#F7F7F7")
	f.pack(side="top", pady=8, padx=8)
	secondL1 = Label(f, text="GitHub", font=("trebuchet MS", 10), fg="#536DFE", bg="#F7F7F7", cursor="hand2")
	secondL1.bind("<Button-1>", call_back_github)
	secondL1.pack(side="left")
	secondL2 = Label(f, text="LinkedIn", font=("trebuchet MS", 10), fg="#536DFE", bg="#F7F7F7", cursor="hand2")
	secondL2.bind("<Button-1>", call_back_linkedin)
	secondL2.pack(side="left")

	footerL = Label(rootk, text="jora2415@gmail.com \n 2018 - 2019", font=("roboto", 10, "bold"), fg="#424242", bg="#F7F7F7")
	footerL.pack(side="bottom", padx=8, pady=8)

def call_back_github(*event):
	webbrowser.open_new(r"https://github.com/kamicase24")

def call_back_linkedin(*event):
	webbrowser.open_new(r"linkedin.com/in/jrojasart/")


	# with open(creds) as f:
	# 	data = f.readlines()
	# 	print(data)
	# 	user = data[0].rstrip()
	# 	password = data[1].rstrip()

	# if nameE.get() == user and passwordE.get() == password:
	# 	r = Tk()
	# 	r.title(':D')
	# 	r.geometry('150x50')
	# 	rlbl = Label(r, text='\n[+] Ha ingresado')
	# 	rlbl.pack()
	# 	r.mainloop()
	# else:
	# 	r = Tk()
	# 	r.title(':c')
	# 	r.geometry('150x50')
	# 	rlbl = Label(r, text='\n[+] Ingreso Invalido')
	# 	rlbl.pack()
	# 	r.mainloop()

# def DelUser():

# 	os.remove(creds)
# 	rootl.destroy()
# 	Signup()

Login()

# if os.path.isfile(creds):
# 	Login()
# else:
# 	Signup()