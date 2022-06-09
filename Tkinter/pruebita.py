from tkinter import *

root= Tk()
root.title('Nu')
root.iconbitmap('nu-icon.ico')
root.config(bg='purple',bd=15)

n1=StringVar()
nf=StringVar()

menubar=Menu(root)
root.config(menu=menubar)

calculomenu=Menu(menubar, tearoff=0)
calculomenu.add_command(label='suma')
calculomenu.add_command(label='resta')
calculomenu.add_separator()
calculomenu.add_command(label='multiplicacion')


prestamomenu=Menu(menubar, tearoff=0)
prestamomenu.add_command(label='configuracion')
prestamomenu.add_command(label='semanas')
prestamomenu.add_separator()
prestamomenu.add_command(label='meses')

interesmenu=Menu(menubar,tearoff=0)
interesmenu.add_command(label='ajustes')
interesmenu.add_command(label='meses')
interesmenu.add_separator()
interesmenu.add_command(label='semanas')

menubar.add_cascade(label='calculadora', menu=calculomenu)
menubar.add_cascade(label='prestamos',menu=prestamomenu)
menubar.add_cascade(label='intereses', menu=interesmenu)


def interes():
    nf.set(float(n1.get())*.03)


Label(root, text='Prestamos', justify='center', fg='white',bg='purple', font=('lucida fax',13),bd=10).pack()
Entry(root, justify='left', font=('Arial',12),textvariable=n1,bd=3).pack()

Label(root, text='interes', justify='center', fg='white',bg='purple', font=('verdana',13),bd=10).pack()
Entry(root, justify='center', font=('Arial',12),textvariable=nf,bd=3 , state='disable').pack()

Button(root,command=interes ,text='Calcular',width=17 , height=2).pack(padx=10,pady=20)



root.mainloop()
