def main():
    # escribe tu código abajo de esta línea
    NumeroPalabras = int(input("Dame el número de palabras: "))
    Parte1 = NumeroPalabras/475
    Parte2 = int(Parte1)
    if Parte1 - Parte2 > 0:
        Parte2 = Parte2 + 1

    Precio = Parte2 * 60
    PrecioTotal = Precio - (Precio * 0.10)
    print("El costo de la publicación es: ", PrecioTotal)
    

if __name__ == '__main__':
    main()
