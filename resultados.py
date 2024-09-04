import tkinter as tk


class Resultados():
    def __init__(self, vent):
        self.vent = vent
        self.vent.state('zoomed')
        self.vent.resizable(False, False)
        self.vent.config(bg="#ffcc99")
        self.label = tk.Label(self.vent, text="Resultados")
        self.label.pack()
        
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
