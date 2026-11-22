import tkinter as tk
from jugador import crear_mago


def iniciar_aplicacion():
    ventana = tk.Tk()
    ventana.title("La aventura del mago")
    ventana.geometry("650x450")
    ventana.resizable(False, False)

    #titulo de la aventura
    titulo = tk.Label(
        ventana,
        text="La aventura del mago",
        font=("Times New Roman", 24, "bold"),
    )
    titulo.pack(pady=25)

    descripcion = tk.Label(
        ventana,
        text="Una nueva aventura esta por comenzar...",
        font=("Times New Roman", 12),
    )
    descripcion.pack(pady=10)

    #Campo para ingresar el nombre del mago
    etiqueta_nombre = tk.Label(
        ventana,
        text="Como se llamara nuestro mago?",
    )
    etiqueta_nombre.pack(pady=10)

    entrada_nombre = tk.Entry(
        ventana,
        font=("Times New Roman", 14),
        justify="center",
    )
    entrada_nombre.pack(pady=5)
    entrada_nombre.insert(0, "Aldric")  # Valor por defecto

    #Aqui responderemos al click
    def comenzar():
        nombre = entrada_nombre.get().strip() or "Aldric"
        jugador = crear_mago(nombre)
        titulo.config(text=f"Bienvenido, {jugador.nombre}!")
        descripcion.config(
            text=f"Eres un {jugador.clase} y tienes "
                f"{jugador.vida} puntos de vida."
        )

        etiqueta_nombre.pack_forget()
        entrada_nombre.pack_forget()
        boton_comenzar.pack_forget()

    boton_comenzar = tk.Button(
        ventana,
        text="Comenzar aventura",
        font=("Times New Roman", 12, "bold"),
        command=comenzar,
    )
    boton_comenzar.pack(pady=25)

    ventana.mainloop() 