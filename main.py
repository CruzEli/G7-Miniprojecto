import tkinter as tk
from PIL import ImageTk, Image

class Inicio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('480x550')
        self.ventana.state('zoomed')
        self.ventana.resizable(0, 0)

        self.bg_frame = Image.open('img/background1.png')
        foto = ImageTk.PhotoImage(self.bg_frame) 
        self.bg_panel = tk.Label(self.ventana, image=foto)
        self.bg_panel.image = foto
        self.bg_panel.pack(fill='both', expand=True)

        self.lgn_frame = tk.Frame(self.ventana, bg='#000000', width='950', height=600)
        self.lgn_frame.place(x=200, y=70)


        # Título lateral superior izquierdo
        self.txt = 'PREGUNTADOS'
        self.encabezado = tk.Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#000000', fg='white') 
        self.encabezado.place(x=80, y=30, width=300, height=30)


        # Imágen lateral izquierda
        self.imagen_lateral = Image.open('img/vector.png')
        foto = ImageTk.PhotoImage(self.imagen_lateral) 
        self.imagen_lateral_label = tk.Label(self.lgn_frame, image=foto, bg='#000000')
        self.imagen_lateral_label.image = foto
        self.imagen_lateral_label.place(x=5, y=100)


        # Botón preguntados (LLeva al inicio del juego)
        self.preguntados = Image.open('img/preguntadoss.png')
        self.preguntados = self.preguntados.resize((200, 200))  # Cambia el tamaño según necesites
        foto = ImageTk.PhotoImage(self.preguntados)
        self.preguntados_button = tk.Button(self.lgn_frame, image=foto, bg='#000000', borderwidth=0)
        self.preguntados_button.image = foto
        self.preguntados_button.place(x=625, y=125)   

def page():
    ventana = tk.Tk()
    Inicio(ventana)
    ventana.mainloop()

if __name__ == '__main__':
    page()
