def main():
    # escribe tu código abajo de esta línea
    JuegosNuevos = float(input("Dame la cantidad de juegos nuevos: "))
    JuegosViejos = float(input("Dame la cantidad de juegos usados: "))
    CostoNuevos = JuegosNuevos*1000
    CostoViejos = JuegosViejos*350
    CostoTotal = CostoNuevos + CostoViejos
    print("El total de la compra es:", CostoTotal)


if __name__ == '__main__':
    main()
