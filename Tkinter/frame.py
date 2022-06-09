from tkinter import *

root=Tk()
root.title("FerSho")
root.resizable(1,0)
root.iconbitmap('tech.ico')

#crear el marco 
frame=Frame(root,height=480,width=320)
frame.pack() 
frame.config(cursor='mouse') #define la forma del cursor
frame.config(bg='lightblue') #define el color del frame 
frame.config(bd=10) #define un tamaño de contorno
frame.config(relief='sunken') #define la forma del contorno 

root.config(cursor='pirate')
root.config(bg='red')
root.config(bd=5)
root.config(relief='groove')


#debe estar abajo
root.mainloop()