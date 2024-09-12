import tkinter as tk
import pandas as pd
import time
from resultados import Resultados

class InterfazPreguntas(tk.Frame):
    def __init__(self, vent, preguntas):
        self.preguntas = preguntas
        self.vent = vent
        self.vent.state('zoomed')
        self.vent.resizable(False, False)
        self.vent.config(bg="#ffcc99")
        
        self.crear_widgets()
        
        self.time_limit = 60    # Tiempo limite para responder
        self.countdown()
        self.contador = 0
        self.correctas = 0
        self.incorrectas = 0
        self.set_preguntas()
    
    def crear_preguntas(df, categoria):
        preguntas = []
        df_filtrado = df[df["Categoría"] == categoria]

        for fila in df_filtrado.iterrows():
            pregunta = Preguntas(
                fila["Categoría"],
                fila["Pregunta"],
                fila["Opción A"],
                fila["Opción B"],
                fila["Opción C"],
                fila["Opción D"],
                fila["Correcta"]
            )
            preguntas.append(pregunta)
        return preguntas

    def crear_widgets(self):
        self.frame_1 = tk.Frame(self.vent)
        self.frame_1.place(relx=0.025, rely=0.025,relwidth=0.95, relheight=0.35)
        
        
        self.frame_2 = tk.Frame(self.vent, bg="#ffcc99")
        self.frame_2.place(relx=0.025, rely=0.5,relwidth=0.95, relheight=0.475)
        
        # Variables
        self.txt_categoria = tk.StringVar()
        self.txt_pregunta = tk.StringVar()
        self.txt_opc_a = tk.StringVar()
        self.txt_opc_b = tk.StringVar()
        self.txt_opc_c = tk.StringVar()
        self.txt_opc_d = tk.StringVar()
        
        # Labels
        self.lbl_categoria = tk.Label(self.frame_1, textvariable=self.txt_categoria)
        self.lbl_categoria.pack()
        self.lbl_pregunta = tk.Label(self.frame_1, textvariable=self.txt_pregunta)
        self.lbl_pregunta.pack(expand=True, fill="both")
        self.lbl_reloj = tk.Label(self.vent, text="30")
        self.lbl_reloj.place(relx=0.4, rely=0.4, relwidth=.2, relheight=.075)
        
        # Botones
        self.btn_opcion_A = tk.Button(self.frame_2, textvariable=self.txt_opc_a)
        self.btn_opcion_A.config(command=lambda txt=self.txt_opc_a, btn=self.btn_opcion_A:[self.chequear_preguntas(txt,btn),self.set_preguntas()])
        self.btn_opcion_A.place(relx=0, rely=0, relwidth=1, relheight=.22)
        
        self.btn_opcion_B = tk.Button(self.frame_2, textvariable=self.txt_opc_b)
        self.btn_opcion_B.config(command=lambda txt=self.txt_opc_b, btn=self.btn_opcion_B:[self.chequear_preguntas(txt,btn),self.set_preguntas()])
        self.btn_opcion_B.place(relx=0, rely=.26, relwidth=1, relheight=.22)
        
        self.btn_opcion_C = tk.Button(self.frame_2, textvariable=self.txt_opc_c)
        self.btn_opcion_C.config(command=lambda txt=self.txt_opc_c, btn=self.btn_opcion_C:[self.chequear_preguntas(txt,btn),self.set_preguntas()])
        self.btn_opcion_C.place(relx=0, rely=.52, relwidth=1, relheight=.22 )
        
        self.btn_opcion_D = tk.Button(self.frame_2, textvariable=self.txt_opc_d)
        self.btn_opcion_D.config(command=lambda txt=self.txt_opc_d, btn=self.btn_opcion_D:[self.chequear_preguntas(txt,btn),self.set_preguntas()])
        self.btn_opcion_D.place(relx=0, rely=.78, relwidth=1, relheight=.22)
     
    def set_preguntas(self):
        try:
            qtn = self.preguntas[self.contador]
            self.txt_categoria.set(qtn.categoria)
            self.txt_pregunta.set(qtn.pregunta)
            self.txt_opc_a.set(qtn.opc_a)
            self.txt_opc_b.set(qtn.opc_b)
            self.txt_opc_c.set(qtn.opc_c)
            self.txt_opc_d.set(qtn.opc_d)
            self.contador += 1
        except IndexError:
            self.abrir_resultados()
    
    def chequear_preguntas(self, txt, btn):
        #btn.config(bg="#ffe3c7")
        qtn = self.preguntas[self.contador-1]

        print(f"Correcta: {qtn.opc_correc}")
        print(f"Elegida: {txt.get()}")
        if str(qtn.opc_correc) == txt.get():
            print("Respuesta correcta")
            self.correctas += 1 
            btn.config(bg="green")
        else:
            print("Respuesta incorrecta")
            self.incorrectas += 1
            btn.config(bg="red")
        
        time.sleep(5)
        #
            
    def countdown(self):
        if self.time_limit > 0:
            self.timer = "{:02d}".format(self.time_limit)
            self.lbl_reloj.config(text=self.timer)
            self.time_limit -= 1
            self.lbl_reloj.after(1000, self.countdown)
        else:
            self.abrir_resultados()
    
    def abrir_resultados(self):
        self.vent.destroy()
        ventana = tk.Tk()
        
        Resultados(ventana, self.contador, self.correctas, self.incorrectas)
        ventana.mainloop()
   


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
        

def cargar_preguntas_excel(ruta_excel, categoria):
    df = pd.read_excel(ruta_excel)
    return InterfazPreguntas.crear_preguntas(df, categoria)


def page(ruta_excel, categoria):
    preguntas = cargar_preguntas_excel(ruta_excel, categoria)
    ventana = tk.Tk()
    InterfazPreguntas(ventana, preguntas)
    ventana.mainloop()

if __name__ == "__main__":
    ruta_excel = "data/bbdd_preguntas.xlsx"  
    categoria = "Ciencia"
    page(ruta_excel, categoria)