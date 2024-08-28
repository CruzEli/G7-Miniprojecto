import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.frames = {}

        self.show_frame(StartPage)  

    def show_frame(self, container):
        frame = self.frames.get(container)

        if frame is None:
            frame = container(self.container, self)
            self.frames[container] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="Página de Inicio")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Ir a la Página 2",
                           command=lambda: controller.show_frame(PageTwo))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="Página 2")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Volver a la Página de Inicio",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
