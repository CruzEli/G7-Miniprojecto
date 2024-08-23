import tkinter as tk

class Jugador:
    def __init__(self):
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_subir_nivel = 100
        
    
    def ganar_xp(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= self.experiencia_subir_nivel:
            self.subir_nivel()

    def subir_nivel(self, cantidad):
        self.nivel += 1
        self.experiencia -= self.experiencia_subir_nivel
        self.experiencia_subir_nivel *= 1.5
    
    def perdiste(self):
        if self.nivel < 5:
            return 'PERDISTE :('
        

class Juego_Preguntados:
    def __init__(self):
        self.ventana = ventana
        self.jugador = Jugador()
        self.resolucion = ventana.geometry('1166x718')
        self.color = ventana.config(bg='#ffcc99')


        self.label_nivel = tk.Label(self.ventana, text=f"Nivel: {self.jugador.nivel}", font=('Times new roman', 25), bg='#ff7a33')
        self.label_nivel.pack(pady=10)

        self.label_experiencia = tk.Label(self.ventana, text=f"Experiencia: {self.jugador.experiencia}", font=('Times new roman', 25), bg='#ff7a33')
        self.label_experiencia.pack(pady=10)



if __name__ == "__main__":
    ventana = tk.Tk()
    juego = Juego_Preguntados()
    ventana.mainloop()