import tkinter as tk
from tkinter import ttk

entradas={'salame-R$2,00':2, 'batata-R$5,00':5}
A=['Pedidos: ']
B=[]

def pegar():
	A.append(combo.get())
	texto.set(A)
	B.append(entradas[combo.get()])

def finalizar():	
	texto2.set('Total: R$'+ str(sum(B)) +',00')
	

janela = tk.Tk()
texto= tk.StringVar()
texto2=tk.StringVar()
texto.set('Pedido: ')
texto2.set('Total: ')
combo=ttk.Combobox(janela)
combo.place(x=50,y=100)
combo['values']=('Escolha uma entrada','salame-R$2,00','batata-R$5,00')
combo.current(0)
botao=tk.Button(janela,command=pegar, text='Adicionar ao pedido').place(x=80,y=150)
botao2=tk.Button(janela,command=finalizar, text='Finalizar pedido').place(x=80,y=180)
etiqueta= tk.Label(janela,textvariable=texto).place(x=40,y=210)
etiqueta2= tk.Label(janela,textvariable=texto2).place(x=40,y=240)


janela.geometry("500x500")
janela.mainloop()
