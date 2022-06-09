from tkinter import*

root=Tk()
root.title('H&M')
root.config(bg='blue')

#cuadro de texto para un comentario o una descripcion por ejemplo

texto=Text(root,width=50,height=30,padx=15,pady=15,selectbackground='red',font=('haoni',12))
texto.pack()
texto.config(width=50,height=30,padx=15,pady=15,selectbackground='red',font=('haoni',12))

root.mainloop()