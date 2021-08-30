def main():
    # escribe tu código abajo de esta línea
    Paginas = float(input("Dame el numero de paginas que quieres publicar: "))
    NumeroPalabras = float(input("Indica cual es el numero de palabras que quieres incluir en tu publicacion: "))

    Coste = NumeroPalabras * 60
    preciototal = Coste - (Coste * 0.10)

    if NumeroPalabras >= 475:
        print('Podemos considerar la pagina')
    else:
        print('Estatus: Pagina no a considerar')

    print('El total de coste por pagina en tu publicacion es:', preciototal)

if __name__ == '__main__':
    main()
