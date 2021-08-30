def main():
    # escribe tu código abajo de esta línea
    SaldoAnterior = float(input("Dame la cantidad de los ingresos mensuales anteriores: "))
    Ingresos = float(input("Dame la cantidad de ingresos: "))
    Egresos = float(input("Dame el valor de los egresos: "))
    Cheque = float(input("Dame el la cantidad de cheques expedidos: "))

    Total = (SaldoAnterior + Ingresos) - (Egresos + (Cheque*13))
    SaldoTotal = Total - (Total*0.075)

    print("El saldo total que tienes es:", SaldoTotal)
    
if __name__ == '__main__':
    main()
