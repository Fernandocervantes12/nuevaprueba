from tkinter import *

root=Tk()
root.title('menus')

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label='abrir')
filemenu.add_command(label='guaradr')
filemenu.add_command(label='cerrar')
filemenu.add_separator()
filemenu.add_command(label='salir', command=root.quit)

editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label='copiar')
editmenu.add_separator()
editmenu.add_command(label='pegar')
editmenu.add_command(label='regresar')

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label='ayuda')
helpmenu.add_command(label='acerca de...')
helpmenu.add_checkbutton(label='hey')
helpmenu.add_radiobutton(label='que pedo')

menubar.add_cascade(label='Archivo',menu=filemenu)
menubar.add_cascade(label='Editar',menu=editmenu)
menubar.add_cascade(label='Ayuda',menu=helpmenu)

root.mainloop()