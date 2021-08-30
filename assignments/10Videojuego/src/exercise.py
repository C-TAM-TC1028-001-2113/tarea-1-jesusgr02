def main():
    # escribe tu código abajo de esta línea
    JuegosNuevos = float(input("Dame el numero de juegos nuevos que te llevaras: "))
    JuegosViejos = float(input("Dame el numero de juegos viejos que te llevaras: "))
    CostoNuevos = JuegosNuevos*1000
    CostoViejos = JuegosViejos*350
    CostoTotal = CostoNuevos + CostoViejos
    print("El cosot total a pagar es:", CostoTotal)


if __name__ == '__main__':
    main()
