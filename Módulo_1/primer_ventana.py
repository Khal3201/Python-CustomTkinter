# Objetivo: Aprender a instalar y configurar CustomTkinter para crear una interfaz básica.
# comando de instalación: pip install customtkinter

"""""
import customtkinter as ctk

ventana = ctk.CTk()
ventana.title("Ventana de custom tkinter")
ventana.geometry("400x300")

ctk.set_appearance_mode("dark") # Posibilidad de usar un modo claro y oscuro

ventana.mainloop()
"""""




"""""
Objetivo: Crear una ventana con un título personalizado y establecer el tamaño de la ventana.

Instrucciones: Crea una ventana con CustomTkinter de 600x400 píxeles y cambia el tema a "light".

 Coloca el título "Ventana de Prueba".
"""""
import customtkinter as ctk

ventana_actividad = ctk.CTk()
ventana_actividad.geometry("600x400")
ventana_actividad.title("Ventana de prueba")
ventana_actividad._set_appearance_mode("light")

ventana_actividad.mainloop()