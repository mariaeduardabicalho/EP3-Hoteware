import tkinter as tk
import time

from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)


class hotel:
	
	def __init__(self):
		# Janela principal.
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("500x500")
		self.window.rowconfigure(0, minsize=150, weight=1)
		self.window.rowconfigure(1, weight=1)
		self.window.columnconfigure(0, minsize=120, weight=1)
		self.window.columnconfigure(1, weight=1)
		self.botao=tk.Button(self.window)
		self.botao.configure(text='Funcionario')
		self.botao.configure(command=self.wfunci)
		self.botao.grid()
		self.mvar=tk.IntVar()

	def iniciar(self):
		self.window.mainloop()

	
	def apertou(self, event):
		self.postar()

	def wfunci(self):
		self.tela_user= tk.Toplevel()
		self.tela_user.geometry("500x500")
		self.tela_user.title("Tela funcionario")
		self.botao=tk.Button(self.tela_user)
		self.botao.configure(text='Quarto 1',background='green')
		self.botao.configure(command=self.quarto) #Como colocar o pedidos aqui?
		self.tela_user.geometry("500x500")
		self.tela_user.rowconfigure(0, minsize=150, weight=1)
		self.tela_user.rowconfigure(1, weight=1)
		self.tela_user.columnconfigure(0, minsize=120, weight=1)
		self.tela_user.columnconfigure(1, weight=1)
		self.botao.grid()
		self.update_clock()
		


	def update_clock(self): 
		now = time.strftime("%H:%M:%S")
		self.window.after(10000, self.update_clock)		
		if (f.get('/users',None)['Quarto1'])=="0" or (f.get('/servico',None)['Quarto1'])=="0":
			self.botao.configure(background='green')
		else:
			self.botao.configure(background='blue')


	def quarto(self):
		for x in f.get('/users',None)['Quarto1']:

			self.check=tk.Checkbutton(self.tela_user,text=x,variable=self.mvar,offvalue=0,command=self.apagarinfou).grid()
			self.mvar=tk.IntVar()
			if self.check==1:
				f.put('/users','Quarto1',x,'0')


		for x in f.get('/servico',None)['Quarto1']:
			self.check=tk.Checkbutton(self.tela_user,text=x,variable=self.mvar,command=self.apagarinfos).grid()
			if self.check==1:
				f.put('/servico','Quarto1',x,'0')

		self.mvar=tk.IntVar()
		self.check3=tk.Checkbutton(self.tela_user,text=f.get('/total',None)['Quarto1'],variable=self.mvar,command=self.apagarinfot).grid()
		if self.check3==1:
			f.put('/total','Quarto1',x,'0')
	



		"""
		self.botao2=tk.Button(self.tela_user)		
		self.botao2.configure(text=f.get('/users',None)['Quarto1'])
		self.botao2.grid(row=1, column=0)
		self.botao2.configure(command=self.apagarinfo)


		self.botao3=tk.Button(self.tela_user)		
		self.botao3.configure(text=f.get('/servico',None)['Quarto1'])
		self.botao3.grid(row=1, column=0)
		self.botao3.configure(command=self.apagarinfo)

		"""

	def apagarinfou(self):
		f.put('/users','Quarto1','0')

	def apagarinfos(self):
		f.put('/servico','Quarto1','0')

	def apagarinfot(self):
		f.put('/total','Quarto1','0')
		

		
		
app = hotel()
app.iniciar()
