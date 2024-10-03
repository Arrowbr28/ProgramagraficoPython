import tkinter as tkinterzao

from tkinter import *

principal = tkinterzao.Tk()

menu = Menu(principal)

principal.config(menu=menu)

filemenu = Menu(menu)

menu.add_cascade(label='arquivo', menu=filemenu)

filemenu.add_command(label='teste')

filemenu.add_command(label= 'Open..' )

filemenu.add_separator()

filemenu.add_command(label="exit", command= principal.quit)

helpmenu = Menu(menu)

menu.add_cascade(label='help', menu= helpmenu)
helpmenu.add_command(label='About')

buscar = Menu(menu)

menu.add_cascade(label="buscar", menu= buscar)
buscar.add_command(label= 'Buscar')





botao = tkinterzao.Button(principal, text='pare', width='24', command=principal.destroy )

w = tkinterzao.Label(principal, text="Supermercado comprefacil")

w2 = tkinterzao.Label(principal, text="Sempre melhor para voce")

w.grid(row=0, column=0)
w2.grid(row=0, column=1)

principal.mainloop()