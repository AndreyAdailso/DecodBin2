from tkinter import *
from functools import partial

def bin_convert():
    """ Recebe uma string representando um binario e retorna o valor em int decimal."""
    decimal = 0
    digt_bin = []
    bin_str = box_entry.get()

    for i in bin_str:
        digt_bin.append(int(i))
    
    for index in range(0, len(digt_bin)):
        n = digt_bin[index] * (2**(len(digt_bin) - 1 - index)) 
        decimal = decimal + n
        
    box_exit["text"] = str(decimal)


window = Tk()

window.title("Bin2Code GUI")

lb_decimal = Label(window, text="Decimal:", bg='gray77')
lb_binary = Label(window, text="Binário:", bg='gray77')
box_exit = Label(window, text="Resultado", bg="white" )
box_entry = Entry(window)
lb_space = Label(window, width=2, height=2)
button = Button(window, text="Decodificar", command=bin_convert)

lb_binary.grid(row=3, column=0)
box_entry.grid(row=3, column=1, sticky=W+E)
lb_space.grid(row=4, column=1)
lb_decimal.grid(row=5, column=0)
box_exit.grid(row=5,column=1, sticky=W+E)
button.grid(row=6, column=1)

window.geometry("300x300")

window.mainloop()
