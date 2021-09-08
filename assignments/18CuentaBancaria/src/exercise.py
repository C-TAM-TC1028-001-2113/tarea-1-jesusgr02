def main():
    # escribe tu código abajo de esta línea
    SaldoAnterior = float(input("Dame el saldo del mes anterior: "))
    Ingresos = float(input("Dame los ingresos: "))
    Egresos = float(input("Dame los egresos: "))
    Cheque = float(input("Dame el número de cheques: "))

    Total = (SaldoAnterior + Ingresos) - (Egresos + (Cheque*13))
    SaldoTotal = Total - (Total*0.075)

    print("El saldo final de la cuenta es:", SaldoTotal)
    
if __name__ == '__main__':
    main()
