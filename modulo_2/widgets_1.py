"""""
códigos de ejemplo:

______________________________
etiqueta = ctk.CTkLabel(ventana, text="¡Hola, CustomTkinter!", font=("Arial", 20))
etiqueta.pack(pady=20)
______________________________

______________________________
def saludar():
    print("¡Hola desde el botón!")

boton = ctk.CTkButton(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)
___________________________

___________________________
entrada = ctk.CTkEntry(ventana, placeholder_text="Escribe algo aquí")
entrada.pack(pady=10)
___________________________

___________________________
def mostrar_valor(valor):
    print(f"Valor del slider: {valor}")

slider = ctk.CTkSlider(ventana, from_=0, to=100, command=mostrar_valor)
slider.pack(pady=20)
___________________________

Actividad 2:
Objetivo: Crear una interfaz con los siguientes elementos:

Una etiqueta que diga "Bienvenido".

Un botón que al hacer clic muestre un mensaje en la consola.

Un campo de entrada de texto donde el usuario pueda escribir su nombre.

Un slider para seleccionar un valor entre 1 y 10.

Pistas: Asegúrate de utilizar .pack(pady=10) para separar los widgets.

"""""

import customtkinter as ctk

ventana = ctk.CTk()

ventana.geometry("600x400")
ventana.title("interfaz con widgets")
ventana._set_appearance_mode("light")


etiqueta = ctk.CTkLabel(ventana, text="Bienvenido", font=("arial",20))
etiqueta.pack(pady=10)
def Mostrar_mensaje():
    print("waoos")
boton = ctk.CTkButton(ventana, text="¡haz click!", command=Mostrar_mensaje)
boton.pack(pady=10)
ventana.mainloop()