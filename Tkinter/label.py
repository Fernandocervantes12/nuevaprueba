
from tkinter import *

root=Tk()
root.title('PUTOS')
root.iconbitmap('tech.ico')
root.config(bg='red')
root.config(bd=15)
root.config(relief='groove')
root.config(cursor='pirate')

frame=Frame(root,height=480,width=320)
frame.pack()
frame.config(bg='lightblue')
frame.config(bd=10)
frame.config(relief='sunken')
frame.config(cursor='spider')

# creacion de etiquetas de texto e imagenes
label=Label(root,text='hola chicos')
label.pack(anchor='center')
label.config(bg='blue', fg='yellow', font=('verdana',14))
Label(root,text='otra etiqueta').pack(side='left')
label2=Label(root,text='otra putines')
label2.pack(anchor='nw')
label2.config(bg='orange',fg='white')

image= PhotoImage(file='bebe.gif')
Label(frame, image=image , bd=1 ).pack(anchor='center')

root.mainloop()
