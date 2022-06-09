from tkinter import *

root= Tk()
root.title('Hola Mundo')
root.iconbitmap('tech.ico')

Label(root,text='Usuarios').grid(row=0, column=0,padx=5,pady=5,sticky='w')
Entry(root,justify='left').grid(row=0,column=1,padx=5,pady=5)

Label(root,text='Contraseña').grid(row=1, column=0,padx=5,pady=5,sticky='w')
Entry(root,justify='center',show='*').grid(row=1,column=1,padx=10,pady=10)

root.mainloop()