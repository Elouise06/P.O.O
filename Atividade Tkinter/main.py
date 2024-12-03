# main.py

from tkinter import Tk
from sistema import SistemaBiblioteca
from interface import BibliotecaApp

if __name__ == "__main__":
    root = Tk()
    sistema = SistemaBiblioteca()  # Instância do sistema
    app = BibliotecaApp(root, sistema)  # Conecta a interface com o sistema
    root.mainloop()
