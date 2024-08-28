import tkinter as tk  

def   selec_categoria(categoria):
    print(f"Categoria seleccionada: {categoria}")

# crea la ventana principal 
ventana = tk.Tk()
ventana.title("ELEGIR CATEGORIA")
ventana.geometry("480x550")  #Defino tamaño de la ventana
ventana.state('zoomed')
#defino color de fondo
ventana.config(bg="#ffcc99")


# crea etiqueta para titulos
 
titulo = tk.Label(ventana, text= "ELEGIR CATEGORIA", font=("Arial",20), bg= "#ffbf00")
titulo.pack(pady= 21)
 
# crea botones para las categorias

categorias = ["Ciencia", "Deporte", "Arte"]  
for categoria in categorias:  
    boton = tk.Button(ventana, text=categoria, font=(" arial",15), command=lambda c=categoria: selec_categoria(c), width=15)
    boton.pack(pady=10)

#  ejecuto la aplicacion
ventana.mainloop() 
  