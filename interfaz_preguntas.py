import tkinter as tk
from PIL import ImageTk, Image

class InterfazPreguntas(tk.Frame):
    def __init__(self, vent, pregunta):
        self.pregunta = pregunta
        self.vent = vent
        self.vent.state('zoomed')
        self.vent.resizable(False, False)
        self.vent.config(bg="#ffcc99")


        self.frame_1 = tk.Frame(self.vent)
        self.frame_1.place(relx=0.025, rely=0.025,relwidth=0.95, relheight=0.35)
        
        
        self.frame_2 = tk.Frame(self.vent, bg="#ffcc99")
        self.frame_2.place(relx=0.025, rely=0.5,relwidth=0.95, relheight=0.475)
        
        
        self.lbl_categoria = tk.Label(self.frame_1, text=self.pregunta.categoria)
        self.lbl_categoria.pack()
        self.lbl_pregunta = tk.Label(self.frame_1, text=self.pregunta.pregunta)
        self.lbl_pregunta.pack(expand=True, fill="both")
        self.lbl_reloj = tk.Label(self.vent, text="reloj")
        self.lbl_reloj.place(relx=0.4, rely=0.4, relwidth=.2, relheight=.075)
        
        # Botones
        self.btn_opcion_A = tk.Button(self.frame_2, text=self.pregunta.opc_a)
        self.btn_opcion_A.place(relx=0, rely=0, relwidth=1, relheight=.22)
        self.btn_opcion_B = tk.Button(self.frame_2, text=self.pregunta.opc_b)
        self.btn_opcion_B.place(relx=0, rely=.26, relwidth=1, relheight=.22)
        self.btn_opcion_C = tk.Button(self.frame_2, text=self.pregunta.opc_c)
        self.btn_opcion_C.place(relx=0, rely=.52, relwidth=1, relheight=.22 )
        self.btn_opcion_D = tk.Button(self.frame_2, text=self.pregunta.opc_d)
        self.btn_opcion_D.place(relx=0, rely=.78, relwidth=1, relheight=.22)
   


class Preguntas:
    def __init__(self, categoria, pregunta, opc_a, opc_b,
                 opc_c, opc_d, opc_correc):
        self.categoria = categoria
        self.pregunta = pregunta
        self.opc_a = opc_a
        self.opc_b = opc_b
        self.opc_c = opc_c
        self.opc_d = opc_d
        self.opc_correc = opc_correc
        
preg_1 = Preguntas("Ciencia", "Cual es el pigmento que les da a las plantas el color verde?",
                   "Cloroformo", "Clorofila", "Cloroverde", "Cloroalgo", "Clorofila")

def page():
    ventana = tk.Tk()
    InterfazPreguntas(ventana, preg_1)
    ventana.mainloop()

if __name__ == "__main__":
    page()