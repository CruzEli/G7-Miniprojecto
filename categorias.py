import tkinter as tk
import pandas as pd
from interfaz_preguntas import InterfazPreguntas, Preguntas

def leer_bbdd():
    df = pd.read_excel("data/bbdd_preguntas.xlsx")
    return df

def selec_categoria(df, categoria):
    preguntas = []
    df_filtrado = df.query(f"Categoría == '{categoria}'")
    df_filtrado.reset_index(drop=True, inplace=True)
    print(df_filtrado)
    for i in range(len(df_filtrado)):
        preguntas.append(Preguntas(df_filtrado.loc[i, "Categoría"], df_filtrado.loc[i, "Pregunta"],
                              df_filtrado.loc[i, "Opción A"], df_filtrado.loc[i, "Opción B"],
                              df_filtrado.loc[i, "Opción C"], df_filtrado.loc[i, "Opción D"],
                              df_filtrado.loc[i, "Respuesta Correcta"]))
    ventana_categorias.destroy() 

    
    ventana_preguntas = tk.Tk()
    InterfazPreguntas(ventana_preguntas, preguntas)
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
    df = leer_bbdd()    
    categorias = list(df["Categoría"].unique())
    for categoria in categorias:
        print(categoria)
        boton = tk.Button(ventana_categorias, text=categoria, font=("Arial",15), command=lambda c=categoria: selec_categoria(df, c), width=15)
        boton.pack(pady=10)

    ventana_categorias.mainloop()

  