menu = """
Bienvenido al conversor de monedas 

1- Pesos Colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    Pesos = input("Cuantos pesos colombianos tienes?: ")
    Pesos = float(Pesos)
    valor_dolar = 4000
    dolares = Pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    Pesos = input("Cuantos pesos Mexicanos tienes?: ")
    Pesos = float(Pesos)
    valor_dolar = 30
    dolares = Pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    Pesos = input("Cuantos pesos Argentinos tienes?: ")
    Pesos = float(Pesos)
    valor_dolar = 70
    dolares = Pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingresa una opcion correcta por favor")
