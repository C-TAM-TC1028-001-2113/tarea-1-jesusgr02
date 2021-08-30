def main():
    # escribe tu código abajo de esta línea
    mensajes = float(input("Dame el numero de mensajes enviados: "))
    megas = float(input("Dame la cantidad de megas gastados: "))
    minutos = float(input("Dame el tiempo invertido en minutos: "))

    CostoMen = mensajes*0.80
    CostoMeg = megas*0.80
    CostoMin = minutos*0.80

    CostoTotal = CostoMen + CostoMeg + CostoMin
    print("EL costo total es:", CostoTotal)

if __name__ == '__main__':
    main()
