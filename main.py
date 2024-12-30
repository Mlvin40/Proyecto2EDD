from src.frontend.Aplicacion import Aplicacion
from tkinter import Tk

def main() -> None:
    root = Tk();
    app = Aplicacion(root);
    root.mainloop();

if __name__ == "__main__":
    main()
