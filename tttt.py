import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
mvar=tk.IntVar()
mvar2=tk.IntVar()
check=tk.Checkbutton(janela,text='oi',variable=mvar).pack()
check=tk.Checkbutton(janela,text='oie',variable=mvar2).pack()
janela.mainloop()