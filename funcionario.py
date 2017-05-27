import tkinter as tk
import time
from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)


class hotel:
	
	def __init__(self):
		# Janela principal.
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(),self.window.winfo_screenheight()))
		self.window.rowconfigure(0, minsize=150, weight=1)
		self.window.rowconfigure(1, weight=1)
		self.window.columnconfigure(0, minsize=120, weight=1)
		self.window.columnconfigure(1, weight=1)

		self.botao=tk.Button(self.window)
		self.botao.configure(text='Funcionario')
		self.botao.configure(command=self.wfunci)
		self.botao.grid()

	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar()

	def wfunci(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("{0}x{1}+0+0".format(self.tela_user.winfo_screenwidth(),self.tela_user.winfo_screenheight()))
		self.tela_user.title("Tela funcionario")
		self.tela_user.columnconfigure(0, minsize=120, weight=1)
		self.tela_user.columnconfigure(1, weight=1)
		self.tela_user.columnconfigure(2, weight=1)
		self.tela_user.columnconfigure(3, weight=1)

		self.botao=tk.Button(self.tela_user)
		self.botao.configure(text='Quarto 1',background='green')
		self.botao.configure(command=lambda : self.quarto('Quarto1',0))

		self.botao2=tk.Button(self.tela_user)
		self.botao2.configure(text='Quarto 2',background='green')
		self.botao2.configure(command=lambda : self.quarto('Quarto2',1))

		self.botao3=tk.Button(self.tela_user)
		self.botao3.configure(text='Quarto 3',background='green')
		self.botao3.configure(command=lambda : self.quarto('Quarto3',2))

		self.botao4=tk.Button(self.tela_user)
		self.botao4.configure(text='Quarto 4',background='green')
		self.botao4.configure(command=lambda : self.quarto('Quarto4',3))
		#self.botao4.configure(command= lambda : self.x(" AAA "))

		self.botao.grid(row=0,column=0)
		self.botao2.grid(row=0,column=1)
		self.botao3.grid(row=0,column=2)
		self.botao4.grid(row=0,column=3)
		
		self.update_clock()

	def update_clock(self): 
		now = time.strftime("%H:%M:%S")
		self.window.after(1000, self.update_clock)		
		if (f.get('/users',None)['Quarto1'])=="0" and (f.get('/servico',None)['Quarto1'])=="0" and (f.get('/total',None)['Quarto1'])=="0":
			self.botao.configure(background='green')
		else:
			self.botao.configure(background='blue')
		if (f.get('/users',None)['Quarto2'])=="0" and (f.get('/servico',None)['Quarto2'])=="0" and (f.get('/total',None)['Quarto2'])=="0":
			self.botao2.configure(background='green')
		else:
			self.botao2.configure(background='blue')
		if (f.get('/users',None)['Quarto3'])=="0" and (f.get('/servico',None)['Quarto3'])=="0" and (f.get('/total',None)['Quarto3'])=="0":
			self.botao3.configure(background='green')
		else:
			self.botao3.configure(background='blue')
		if (f.get('/users',None)['Quarto4'])=="0" and (f.get('/servico',None)['Quarto4'])=="0" and (f.get('/total',None)['Quarto4'])=="0":
			self.botao4.configure(background='green')
		else:
			self.botao4.configure(background='blue')


	def quarto(self,q,c):
		if f.get('/users',None)[q] != '0':
			self.check=tk.Checkbutton(self.tela_user,text=f.get('/users',None)[q],variable=self.mvar,offvalue=0,command=self.apagarinfou).grid(row=2,column=c)
			self.mvar=tk.IntVar()
			if self.check==1:
				f.put('/users',q,'0')

		if f.get('/servico',None)[q] != '0':
			for i in range(len(f.get('/servico',None)[q])):
				x=f.get('/servico',None)[q][i]
				self.mvar=tk.IntVar()
				self.check=tk.Checkbutton(self.tela_user,text=x,variable=self.mvar,command=self.apagarinfos).grid(row=4+i,column=c)
				if self.check==1:
					f.put('/servico',q,x,'0')


		self.mvar=tk.IntVar()
		if f.get('/total',None)[q] != '0':
			self.check3=tk.Checkbutton(self.tela_user,text='Total: R$' + str(f.get('/total',None)[q])+ ',00',variable=self.mvar,command=self.apagarinfot).grid(row=3,column=c)
			if self.check3==1:
				f.put('/total',q,'0')
	

	def apagarinfou(self):
		f.put('/users',q,'0')

	def apagarinfos(self):
		f.put('/servico',q,'0')

	def apagarinfot(self):
		f.put('/total',q,'0')
		
		
app = hotel()
app.iniciar()