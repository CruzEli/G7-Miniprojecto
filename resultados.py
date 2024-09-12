import tkinter as tk


class Resultados():
    def __init__(self, vent, cnt, cnt_bien, cnt_mal):
        self.vent = vent
        self.vent.state('zoomed')
        self.vent.resizable(False, False)
        self.vent.config(bg="#ffcc99")
        self.label_1 = tk.Label(self.vent, text="Resultados")
        self.label_1.pack()


        self.contador = cnt
        self.label_2 = tk.Label(self.vent, text=f"Preguntas hechas:{self.contador}")
        self.label_2.pack()

        self.correctas = cnt_bien
        self.label_3 = tk.Label(self.vent, text=f"Preguntas Correctas:{self.correctas}")
        self.label_3.pack()

        self.incorrectas = cnt_mal
        self.label_4 = tk.Label(self.vent, text=f"Preguntas Incorrectas:{self.incorrectas}")
        self.label_4.pack()

        self.btn = tk.Button(self.vent, text="Salir", command=lambda: self.salir())
        self.btn.pack()


    
    def salir(self):
        self.vent.destroy()
    
    def print_text(self, text):
        print(text)



def page():
    ventana = tk.Tk()
    Resultados(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    page()
