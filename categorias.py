import tkinter as tk
from interfaz_preguntas import InterfazPreguntas, Preguntas

def selec_categoria(categoria):
    print(f"Categoria seleccionada: {categoria}")
    ventana_categorias.withdraw()  
    preg_1 = Preguntas(categoria, "Cual es el pigmento que les da a las plantas el color verde?",
                       "Cloroformo", "Clorofila", "Cloroverde", "Cloroalgo", "Clorofila")
    
    ventana_preguntas = tk.Tk()
    InterfazPreguntas(ventana_preguntas, preg_1)
    ventana_preguntas.mainloop()

def mostrar_categorias():
    global ventana_categorias
    ventana_categorias = tk.Tk()
    ventana_categorias.title("Categorías")
    ventana_categorias.state('zoomed')

    # Defino color de fondo
    ventana_categorias.config(bg="#ffcc99")

    # Crea etiqueta para títulos
    titulo = tk.Label(ventana_categorias, text= "ELEGIR CATEGORIA", font=("Arial",20), bg= "#ffbf00")
    titulo.pack(pady= 21)

    # Crea botones para las categorías
    categorias = ["Ciencia", "Deporte", "Arte"]
    for categoria in categorias:
        boton = tk.Button(ventana_categorias, text=categoria, font=("Arial",15), command=lambda c=categoria: selec_categoria(c), width=15)
        boton.pack(pady=10)

    ventana_categorias.mainloop()

  