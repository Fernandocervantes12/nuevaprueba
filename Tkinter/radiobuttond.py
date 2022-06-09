from tkinter import *

def seleccionar():
    lb1.config(text=f'{semana.get()}')

def reset():
    semana.set(None)
    lb1.config(text='')


root=Tk()
root.title('Radio boton')
root.config(bg='orange')


semana= IntVar()

Radiobutton(root, text='semana 1',variable=semana, value=1,command=seleccionar).pack()
Radiobutton(root, text='semana 2',variable=semana, value=2,command=seleccionar).pack()
Radiobutton(root, text='semana 3',variable=semana, value=3,command=seleccionar).pack()

lb1=Label(root,bd=5,fg='red')
lb1.pack()

Button(root,text='reiniciar',command=reset, fg='brown',bg='lightblue').pack()



root.mainloop()
