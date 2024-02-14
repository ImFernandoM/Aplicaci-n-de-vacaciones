import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from datetime import datetime

#------------------------> CREAR VENTANA <------------------------
# Creamos una instancia de la ventana principal
ventana = tk.Tk()

# Configuramos el título de la ventana
ventana.title("Vacaciones AGP MX")

# Configuramos las dimensiones de la ventana
ventana.geometry("1300x600")

#-------------------------------> CARGAR IMAGEN <-----------------------
# Cargamos la imagen
imagen = PhotoImage(file="AGP_Logo_Full_Color_sGlass (1).png")

# Creamos un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen)

# Configuramos el ancho y alto del label para que se ajuste a la imagen
label_imagen.config(width=imagen.width(), height=imagen.height())

# Creamos un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen)

#-------------------------------> ESCALAR IMAGEN <-----------------------

# Factor de escala para modificar el tamaño de la imagen
factor_escala = 0.25  # Por ejemplo, reducir a la mitad

# Modificamos el tamaño de la imagen aplicando el factor de escala
imagen_redimensionada = imagen.subsample(int(1/factor_escala), int(1/factor_escala))

# Creamos un widget Label para mostrar la imagen redimensionada
label_imagen = tk.Label(ventana, image=imagen_redimensionada)

# Configuramos el ancho y alto del label para que se ajuste al tamaño de la imagen redimensionada
ancho_nuevo = int(imagen.width() * factor_escala)
alto_nuevo = int(imagen.height() * factor_escala)
label_imagen.config(width=ancho_nuevo, height=alto_nuevo)

#-------------------------------> LISTA <-----------------------

# Crear el widget Treeview
tabla = ttk.Treeview(ventana)

# Definir las columnas de la tabla
tabla["columns"] = ("Nombre", "Dias de vacaciones", "Dias solicitados",  "fecha de solicitud", "Correo")

# Formatear las columnas
tabla.column("#0", width=0, stretch=tk.NO)  # Columna oculta
tabla.column("Nombre", anchor=tk.CENTER, width=150)
tabla.column("Dias de vacaciones", anchor=tk.CENTER, width=200)
tabla.column("Dias solicitados", anchor=tk.CENTER, width=200)
tabla.column("fecha de solicitud", anchor=tk.CENTER, width=200)
tabla.column("Correo", anchor=tk.CENTER, width=525)

# Agregar encabezados de columna
tabla.heading("#0", text="", anchor=tk.CENTER)  # Encabezado de columna oculta
tabla.heading("Nombre", text="Nombre", anchor=tk.CENTER)
tabla.heading("Dias de vacaciones", text="Dias de vacaciones", anchor=tk.CENTER)
tabla.heading("Dias solicitados", text="Dias solicitados", anchor=tk.CENTER)
tabla.heading("fecha de solicitud", text="fecha de solicitud", anchor=tk.CENTER)
tabla.heading("Correo", text="Correo", anchor=tk.CENTER)

# Agregar datos a la tabla
datos = [
    ("Abigail", 30, 10, "juan@example.com"),
    ("Alejandro", 25, 8, "maria@example.com"),
    ("Carlos", 35, 3, "pedro@example.com"),
    ("Cecilia", 28, 15, "luisa@example.com"),
    ("Dario", 28, 10, "luisa@example.com"),
    ("Edwin", 28, 1, "luisa@example.com"),
    ("Guillermo", 28, 21, "luisa@example.com"),
    ("Lorna", 28, 15, "luisa@example.com")
]

for i, (nombre, edad, correo, dias) in enumerate(datos, start=1):
    tabla.insert("", tk.END, iid=i, values=(nombre, edad, correo))

#-------------------------------> POSICION DE LA TABLA <-----------------------

# Mostrar la tabla en la ventana, posicionándola abajo (BOTTOM)
tabla.place(relx=1, rely=0, anchor=tk.S)

tabla.pack(side=tk.BOTTOM)

tabla.place(relx=0.5, rely=0.7, anchor=tk.S)

#-------------------------------> COLOCAR LA FECHA <-----------------------

# Función para actualizar la fecha actual
def actualizar_fecha():
    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    etiqueta_fecha.config(text="Fecha actual: " + fecha_actual)

# Obtener la fecha actual
fecha_actual = datetime.today().strftime('%Y-%m-%d')

# Crear un Label para mostrar la fecha actual
etiqueta_fecha = tk.Label(ventana, text="Fecha actual: " + fecha_actual)
etiqueta_fecha.pack()

etiqueta_fecha.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)  # Colocar en la parte superior izquierda y margen de 10px
#-------------------------------> PROYECTAR LA APP <-----------------------
# Mostramos el widget Label en la ventana
label_imagen.pack()

# Mostramos la ventana
ventana.mainloop()

