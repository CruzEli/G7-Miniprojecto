import tkinter as tk

class QuizWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.state("zoomed")
        self.window.resizable(False, False)


def page():
    window = tk.Tk()
    QuizWindow(window)
    window.mainloop()


if __name__ == "__main__":
    page()


ventana = tk.Tk()

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Dimensiones de la ventana y calculo de coordenadas
ancho_ventana = 480
alto_ventana = 548
posicion_x = (ancho_pantalla-ancho_ventana)/2   # Para centrar la ventana en la pantalla
posicion_y = (alto_pantalla-alto_ventana)/2

ventana.title("Preguntas")
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{int(posicion_x)}+{int(posicion_y)}")
ventana.resizable(False, False)     # Bloquea el tamaño de la ventana

# Marcos
frame_pregunta = tk.Frame(ventana)
frame_pregunta.configure(width=460, height=200, bg="red")
frame_pregunta.pack()

# Etiquetas
label_categoria = tk.Label(frame_pregunta, text="Categoría", bg="yellow")
label_categoria.pack()

# Texto
text_pregunta = tk.Text(frame_pregunta)
text_pregunta.config(width= 440, height= 150, selectbackground="red", bg="blue")
text_pregunta.pack()

# Botones
boton_A = tk.Button(ventana, text= "Opcion A", padx= 150, pady= 10)
boton_A.pack()

boton_B = tk.Button(ventana, text= "Opcion B", padx= 150, pady= 10)
boton_B.pack()

boton_C = tk.Button(ventana, text= "Opcion C", padx= 150, pady= 10)
boton_C.pack()

boton_D = tk.Button(ventana, text= "Opcion Dddddddddddddddddddddddddddddd", padx= 150, pady= 10)
boton_D.pack()

# Iniciacion de la ventana
ventana.mainloop()


class Preguntas:
    def __init__(self, titulo,opcion_a, correcta):
        self.titulo = titulo
        self.opcion_a = opcion_a
        self.correcta =correcta

preguntas = []
for item in range(1, 10):
    preguntas.append(Preguntas(f"titulo{item}", "opcion1","opcion1" ))

for i in preguntas:
    print(i.titulo)
