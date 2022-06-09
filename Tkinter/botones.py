from tkinter import *

def sumar():
    r.set(float(n1.get())+float(n2.get()))
    borrar()
def resta():
    r.set(float(n1.get())-float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get())*float(n2.get()))
    borrar()

def borrar():
    n1.set('')
    n2.set('')

root=Tk()
root.title('calculadora')
root.config(bd=15,bg='lightblue')


n1=StringVar()
n2=StringVar()
r=StringVar()


Label(root,text='primer numero',fg='purple',bg='lightblue',font=('Arial',10)).pack()
Entry(root,justify='left',textvariable=n1,fg='red').pack()
Label(root,text='segundo numero',fg='purple',bg='lightblue',font=('Arial',10)).pack()
Entry(root,justify='left',textvariable=n2,fg='red').pack()
Label(root,text='resultado',fg='purple',bg='lightblue',font=('Arial',10)).pack()
Entry(root,justify='center',textvariable=r,fg='blue',state='disable').pack()

Button(root, text='sumar', command=sumar,bg='orange',width=8,height=2,font=('Calibri',12)).pack(side='left',padx=15,pady=15)
Button(root, text='resta', command=resta,bg='orange',width=8,height=2,font=('Calibri',12)).pack(side='left',padx=15,pady=15)
Button(root, text='producto', command=producto,bg='orange',width=8,height=2,font=('Calibri',12)).pack(side='left',padx=15,pady=15)

root.mainloop()