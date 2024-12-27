from src.backend.ArbolB.ArbolB import ArbolB


def main() -> None:
    print("Hola, mundo!")
    arbolB: ArbolB = ArbolB(5);

    # Insertar claves en el arbol B de grado 5
    arbolB.insertar_valor(1);
    arbolB.insertar_valor(2);
    arbolB.insertar_valor(3);
    arbolB.insertar_valor(4);
    arbolB.insertar_valor(5);
    arbolB.insertar_valor(6);
    arbolB.insertar_valor(7);
    arbolB.insertar_valor(8);
    arbolB.insertar_valor(9);
    arbolB.insertar_valor(10);
    arbolB.insertar_valor(11);
    arbolB.insertar_valor(12);
    arbolB.insertar_valor(13);
    arbolB.insertar_valor(14);
    arbolB.insertar_valor(15);
    arbolB.insertar_valor(16);
    arbolB.insertar_valor(17);


    # Generar el código Graphviz
    graphviz: str = arbolB.generar_graphviz();
    print(graphviz);

if __name__ == "__main__":
    main()