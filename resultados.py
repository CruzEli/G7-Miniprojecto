import tkinter as tk


class Resultados():
    def __init__(self, vent, cnt, cnt_bien, cnt_mal):
        self.vent = vent
        self.vent.state('zoomed')
        self.vent.resizable(False, False)
        self.vent.config(bg="#ffcc99")
        self.label_1 = tk.Label(self.vent, text="Resultados", bg="#ffcc99", bd=2, relief="ridge", padx=20, pady=20)
        self.label_1.pack()


        self.contador = cnt
        self.label_2 = tk.Label(self.vent, text=f"Preguntas hechas:{self.contador}",  font=("Arial", 24, "bold"), bg="#ffcc99")
        self.label_2.pack(pady=50)

        self.correctas = cnt_bien
        self.label_3 = tk.Label(self.vent, text=f"Preguntas Correctas:{self.correctas}", font=("Arial", 18), bg="#ffcc99")
        self.label_3.pack(pady=10)

        self.incorrectas = cnt_mal
        self.label_4 = tk.Label(self.vent, text=f"Preguntas Incorrectas:{self.incorrectas}", font=("Arial", 18), bg="#ffcc99")
        self.label_4.pack(pady=10)

        self.btn = tk.Button(self.vent, text="Salir", font=("Arial", 18), width=10, height=2, bg="#e74c3c", fg="white", command=lambda: self.salir())
        self.btn.pack(pady=20)


    
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
