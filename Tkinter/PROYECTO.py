from tkinter import*
from tkinter import filedialog as dl

ruta=''

def guardar():
    global ruta
    mensaje.set('guadando archivo')

    if ruta != "":
        contenido=texto.get(1.0,'end-1c')
        fichero=open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
    else:
        guardar_como()
                
    
def nuevo():
    global ruta
    mensaje.set('nuevo archivo')
    ruta=''
    texto.delete(1.0,'end')

def guardar_como():
    global ruta
    mensaje.set('guardando archivo como')
    fichero=dl.asksaveasfile(title='Guardar como', mode='w',defaultextension='.txt')
    if fichero is not None:
        contenido=texto.get(1.0,'end-1c')
        ruta= fichero.name
        fichero=open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('guardado correctamente')
    else:
        mensaje.set('guardado cancelado')


def abrir():
    global ruta
    mensaje.set('abriendo archivo')
    ruta=dl.askopenfilename(title='Abrir Archivo',defaultextension='.txt',
    filetypes=(('fichero de texto','.*txt'),))
    if ruta != "":
        fichero=open(ruta,'r')
        contenido=fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert',contenido)
        fichero.close()


root= Tk()
root.title('editor de ficheros')
root.config(bd=10)

menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label='abrir',command=abrir)
filemenu.add_command(label='Nuevo',command=nuevo)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como',command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir',command=root.quit)

menubar.add_cascade(menu=filemenu,label='ARCHIVO')

texto=Text(root,bd=0,pady=4,padx=6,font=('consolas',12))
texto.pack(fill='both',expand=1)

mensaje=StringVar()
mensaje.set('bienvenido al editor')
monitor=Label(root, textvariable=mensaje,justify='left')
monitor.pack(side='left')
root.mainloop()
