import tkinter as tk
from tkinter import messagebox
import BaseDatos
import utils
import base64

ventana= tk.Tk()
ventana.title("Base de Datos")
ventana.geometry("400x400")
ventana.configure(bg="#49A")

lMiEtiqueta=tk.Label(text="Manuel Saquilán",font=("Verdana",12,"bold"))
lMiEtiqueta.place(x=250,y=370)
lMiEtiqueta.configure(bg="#49A")

lUsuario=tk.Label(text="Ingrese su nombre de usuario")
lUsuario.place(x=10,y=10)
lUsuario.configure(bg="#49A")
eUsuario=tk.Entry()
eUsuario.place(x=210,y=10)

lEmail=tk.Label(text="Ingrese su mail")
lEmail.place(x=10,y=50)
lEmail.configure(bg="#49A")
eEmail=tk.Entry()
eEmail.place(x=210,y=50)

lNacimiento=tk.Label(text="Ingrese su fecha de nacimiento")
lNacimiento.place(x=10,y=90)
lNacimiento.configure(bg="#49A")
eNacimiento=tk.Entry()
eNacimiento.place(x=210,y=90)

lPass=tk.Label(text="Ingrese su contraseña")
lPass.place(x=10,y=130)
lPass.configure(bg="#49A")
ePass=tk.Entry(show="*")
ePass.place(x=210,y=130)

def comprobarPassword():
  password=ePass.get()
  password=password.encode('ascii')
  password=base64.b64encode(password)
  if len(password)<8:
        messagebox.showinfo("Mensaje", "La contraseña debe tener al menos 8 caracteres")
        limpiarFormulario()

def guardar():
    username=eUsuario.get()
    email=eEmail.get()
    nacimiento=eNacimiento.get()
    password=ePass.get()
    if utils.nameValidator(username):
        if utils.dateValidator(nacimiento):
            if utils.emailValidator(email):
                try:
                    comprobarPassword()
                    BaseDatos.savedata(username,email,nacimiento,password)
                    messagebox.showinfo("Mensaje", "Usuario registrado exitosamente")
                    limpiarFormulario()
                except:
                    messagebox.showinfo("Mensaje","El usuario no pudo ser registrado")
            else:
                messagebox.showinfo("Mensaje", "Correo eléctronico con formato incorrecto")
        else:
            messagebox.showinfo("Mensaje", "Fecha con formato incorrecto")
    else:
        messagebox.showinfo("Mensaje","nombre con Formato Incorrecto")
        limpiarFormulario()
def limpiarFormulario():
    eUsuario.delete(0,tk.END)
    eEmail.delete(0,tk.END)
    eNacimiento.delete(0,tk.END)
    ePass.delete(0,tk.END)
botonGuardar=tk.Button(text="REGISTRO",width=10,height=2,bg="pale green",command=guardar)
botonGuardar.place(x=170,y=210)

tk.mainloop()