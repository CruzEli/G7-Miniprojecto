import tkinter as tk
from tkinter import messagebox
import random
import time

# Diccionario de preguntas y respuestas
preguntas_respuestas = {
    'Arte': {
        'Fácil': [
            ("¿Quién pintó la Mona Lisa?", "Leonardo da Vinci"),
            ("¿Cuál es la capital del arte renacentista?", "Florencia")
        ],
        'Medio': [
            ("¿En qué año nació Pablo Picasso?", "1881"),
            ("¿Qué movimiento artístico lideró Salvador Dalí?", "Surrealismo")
        ],
        'Difícil': [
            ("¿Quién es conocido como el padre del impresionismo?", "Claude Monet"),
            ("¿En qué museo se encuentra 'La noche estrellada' de Van Gogh?", "MoMA")
        ]
    },
    # Agregar más categorías y preguntas aquí
}

class PreguntadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Preguntados")
        self.jugadores = 1
        self.categoria = ""
        self.nivel = ""
        self.puntuaciones = []
        self.respuestas_consecutivas = []
        self.current_player = 0
        self.current_question = None
        self.start_time = None

        self.create_home_page()

    def create_home_page(self):
        self.clear_window()
        tk.Label(self.root, text="Bienvenido a Preguntados!").pack()
        tk.Button(self.root, text="Jugar Solo", command=lambda: self.start_game(1)).pack()
        tk.Button(self.root, text="Jugar con Amigos", command=self.select_players).pack()

    def select_players(self):
        self.clear_window()
        tk.Label(self.root, text="¿Cuántos jugadores?").pack()
        self.players_entry = tk.Entry(self.root)
        self.players_entry.pack()
        tk.Button(self.root, text="Confirmar", command=self.confirm_players).pack()

    def confirm_players(self):
        self.jugadores = int(self.players_entry.get())
        self.start_game(self.jugadores)

    def start_game(self, jugadores):
        self.jugadores = jugadores
        self.puntuaciones = [0] * jugadores
        self.respuestas_consecutivas = [0] * jugadores
        self.select_category()

    def select_category(self):
        self.clear_window()
        tk.Label(self.root, text="Elige una categoría").pack()
        for categoria in preguntas_respuestas.keys():
            tk.Button(self.root, text=categoria, command=lambda c=categoria: self.select_level(c)).pack()

    def select_level(self, categoria):
        self.categoria = categoria
        self.clear_window()
        tk.Label(self.root, text="Elige un nivel de dificultad").pack()
        for nivel in preguntas_respuestas[categoria].keys():
            tk.Button(self.root, text=nivel, command=lambda n=nivel: self.start_questions(n)).pack()

    def start_questions(self, nivel):
        self.nivel = nivel
        self.current_player = 0
        for i in range(3):

            self.ask_question()

    def ask_question(self):
        if self.current_player >= self.jugadores:
            self.show_scores()
            return

        self.clear_window()
        self.current_question, self.correct_answer = self.select_question()
        tk.Label(self.root, text=f"Jugador {self.current_player + 1}, tu pregunta es:").pack()
        tk.Label(self.root, text=self.current_question).pack()
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()
        tk.Button(self.root, text="Responder", command=self.check_answer).pack()
        self.start_time = time.time()

    def select_question(self):
        return random.choice(preguntas_respuestas[self.categoria][self.nivel])

    def check_answer(self):
        elapsed_time = time.time() - self.start_time
        respuesta = self.answer_entry.get()

        if elapsed_time > 100:
            messagebox.showinfo("Tiempo agotado", "¡Tiempo agotado!")
            self.respuestas_consecutivas[self.current_player] = 0
        elif respuesta.lower() == self.correct_answer.lower():
            messagebox.showinfo("Correcto", "¡Correcto!")
            puntos = max(10 - int(elapsed_time), 1)
            self.puntuaciones[self.current_player] += puntos
            self.respuestas_consecutivas[self.current_player] += 1
            self.puntuaciones[self.current_player] += self.respuestas_consecutivas[self.current_player]
        else:
            messagebox.showinfo("Incorrecto", f"Incorrecto. La respuesta correcta era: {self.correct_answer}")
            self.respuestas_consecutivas[self.current_player] = 0

        self.current_player += 1
        self.ask_question()

    def show_scores(self):
        self.clear_window()
        for j in range(self.jugadores):
            tk.Label(self.root, text=f"Jugador {j + 1}, tu puntuación final es: {self.puntuaciones[j]}").pack()
        tk.Button(self.root, text="Volver a Jugar", command=self.create_home_page).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PreguntadosApp(root)
    root.mainloop()