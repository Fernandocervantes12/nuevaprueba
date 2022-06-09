from tkinter import *

def seleccionar():
    cadena=''
    if coca.get():
        cadena="la coca,"
    if pepsi.get():
        cadena +=" la pepsi "
    if dona.get():
        cadena +="y las donas "
    cadena+='son refrescos'
    labe1.config(text=cadena)
    print(cadena)

root=Tk()
root.title('checkbutton')
root.config(bd=20)

coca=IntVar()
pepsi=IntVar()
dona=IntVar()


Label(root, text='¿Cuales de estos son refrescos').pack()
Checkbutton(root, text='Coca Cola', variable=coca, onvalue=1, offvalue=0,command=seleccionar).pack(anchor='w')
Checkbutton(root, text='pepsi', variable=pepsi,onvalue=1, offvalue=0,command=seleccionar).pack(anchor='w')
Checkbutton(root, text='donas', variable=dona,onvalue=1, offvalue=0,command=seleccionar).pack(anchor='w')

labe1=Label(root,bd=20)
labe1.pack()



root.mainloop()
