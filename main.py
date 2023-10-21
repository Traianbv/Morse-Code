import pandas
from tkinter import *

def code():

    write_code = enter_code.get().upper()

    file = pandas.read_csv("cod.csv")

    dic = {row.Leter: row.Code for (index, row) in file.iterrows()}

    result = [dic[Leter] for Leter in write_code]

    show_code["text"] = result



window = Tk()
window.title("Morse Code")
window.config(padx=50, pady=10, bg="#E3F0F9")


title = Label(text="Convert your string in Morse Code !", font=("Georgia", 15, "bold"), bg="#E3F0F9")
title.grid(column=0, row=0, pady=30)

enter_code = Entry(width=50)
enter_code.grid(column=0, row=3, pady=20)

show_code = Label(text="", font=("Georgia", 15, "bold"), bg="#B6DBF4")
show_code.grid(column=0, row=5, pady=20)

button = Button(text="Convert", width=20, bg="#B6DBF4", command=code)
button.grid(column=0, row=4, pady=20)

window.mainloop()
