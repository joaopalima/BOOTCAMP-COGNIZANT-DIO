import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def globo():
    webbrowser.open('www.globo.com')

myglobo = Button(root, text='Abrir o Globo', command=globo).pack(pady=20)
root.mainloop() #chama o sistema