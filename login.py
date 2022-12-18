import tkinter as tk
import BaseDatos
from tkinter import messagebox

ventana= tk.Tk()
ventana.title("INGRESO AL SISTEMA")
ventana.geometry("400x200")


lUsuario=tk.Label(text="Ingrese su nombre de usuario")
lUsuario.place(x=130,y=10)
eUsuario=tk.Entry()
eUsuario.place(x=150,y=40)

lPass=tk.Label(text="Ingrese su contraseña")
lPass.place(x=130,y=70)
ePass=tk.Entry(show="*")
ePass.place(x=150,y=100)

def ingreso():
    username=eUsuario.get()
    password=ePass.get()
    if BaseDatos.login(username,password):
        messagebox.showinfo("Mensaje","Bienvenido a la plataforma")
    else:
        messagebox.showinfo("Mensaje","Ingreso Incorrecto")
    limpiarformulario()

def limpiarformulario():
    eUsuario.delete(0,tk.END)
    ePass.delete(0,tk.END)

blogin=tk.Button(text="login",width=10,height=2,bg="deep sky blue",fg="white",command=ingreso)
blogin.place(x=170,y=150)


tk.mainloop()