import tkinter as tk

from firebase import firebase
f = firebase.FirebaseApplication('https://ep3-hotware.firebaseio.com', None)


class hotel:
	
	def __init__(self):
		# Janela principal.
		self.window = tk.Tk()
		self.window.title("Hotware")
		self.window.geometry("300x200+100+100")
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
		self.tela_user.geometry("400x400+100+100")
		self.tela_user.title("Tela funcionario")
		self.botao=tk.Button(self.tela_user)
		self.botao.configure(text='Quarto 1',background='green')
		self.botao.configure(command=self.quarto) #Como colocar o pedidos aqui?
		self.tela_user.geometry("400x400+100+100")
		self.tela_user.rowconfigure(0, minsize=150, weight=1)
		self.tela_user.rowconfigure(1, weight=1)
		self.tela_user.columnconfigure(0, minsize=120, weight=1)
		self.tela_user.columnconfigure(1, weight=1)
		#Lb2 = tk.Listbox(self.tela_user)
		#Lb2.insert(1, "ola")
		#teste = 'Quarto1'
				#Lb2.insert(1, ) #fazer o botao abrir a tela que tem isso
		self.botao.grid()
		#Lb2.pack()		

	def quarto(self):
		self.botao2=tk.Button(self.tela_user)
		
		self.botao2.configure(text=f.get('/users',None)['Quarto1'])
		self.botao2.grid(row=1, column=0)
		
		
app = hotel()
app.iniciar()

#loop infinito com tempo wait pra atualizar notificacaoes do fnc pra checar o firebase