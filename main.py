from src.backend.ArbolB.ArbolB import ArbolB


def main() -> None:
    print("Hola, mundo!")

    arbolB: ArbolB = ArbolB(5);
    arbolB.insertar_clave(5);
    arbolB.insertar_clave(6);
    arbolB.insertar_clave(4);
    arbolB.insertar_clave(2);
    arbolB.insertar_clave(7);
    arbolB.insertar_clave(9);
    arbolB.insertar_clave(10);
    arbolB.insertar_clave(3);

    arbolB.insertar_clave(1);

    arbolB.insertar_clave(12);

    arbolB.insertar_clave(0);
    print(arbolB.imprimir_usuario());


if __name__ == "__main__":
    main()