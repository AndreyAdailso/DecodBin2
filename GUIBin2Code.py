from Bin2Code import bin_convert
from Bin2Code import check_bin
from tkinter import *
from functools import partial

def convert():
    bin_str = box_entry.get()
    if check_bin(bin_str) == True:
        box_exit["text"] = bin_convert(bin_str)
    else:
        box_exit["text"] = "Digite um número valido."

window = Tk()

lb_decimal = Label(window, text="Decimal:", bg='gray77')
lb_decimal.grid(row=5, column=0)

lb_binary = Label(window, text="Binário:", bg='gray77')
lb_binary.grid(row=3, column=0)

box_exit = Label(window, text="Resultado", bg="white" )
box_exit.grid(row=5,column=1, sticky=W+E)

box_entry = Entry(window)
box_entry.grid(row=3, column=1, sticky=W+E)

lb_space = Label(window, width=2, height=2)
lb_space.grid(row=4, column=1)

button = Button(window, text="Decodificar", command=convert)
button.grid(row=6, column=1)

window.title("Bin2Code GUI")
window.resizable(False, False)
window.mainloop()
