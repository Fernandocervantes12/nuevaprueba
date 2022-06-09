from statistics import mode
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser as color
from tkinter import filedialog as file




def test():
    """
    #messagebox.showinfo('vemtana nueva','informacion aqui')
    #messagebox.showerror('ventana de error','hubo un error')
    #messagebox.showwarning('ventana de precaucion','prevente de ello')
    resultado=messagebox.askquestion('salir','desea salir?')
    if resultado == 'yes':
        root.quit()
    messagebox.askokcancel('salir','desea salir') devuelve un True o False
    """
    #messagebox.askretrycancel('reintentar','no se puede conectar')
    #messagebox.askyesno('salir','desea salir')
    #color=color.askcolor(title='elige un color')
    ruta=file.askopenfilename(title='abrir archivo',filetypes=(('fichero de python','*.py'),))
    print(ruta)
    #equivale a open(fichero,'w')
    fichero=file.asksaveasfile(title='guardar archivo',defaultextension='.py',mode='a+')

    
root=Tk()

Button(root, text='click',command=test).pack()


root.mainloop()