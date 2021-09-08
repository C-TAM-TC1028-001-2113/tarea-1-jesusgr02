def main():
    # escribe tu código abajo de esta línea
    mensajes = float(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = float(input("Dame el número de minutos: "))

    CostoMen = mensajes*0.80
    CostoMeg = megas*0.80
    CostoMin = minutos*0.80

    CostoTotal = CostoMen + CostoMeg + CostoMin
    print("EL costo mensual es:", CostoTotal)

if __name__ == '__main__':
    main()
