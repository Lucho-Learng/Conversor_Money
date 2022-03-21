def conversor(Tipo_de_pesos, valor_dolar):
    Pesos = input("Cuantos pesos " + Tipo_de_pesos + " tienes?: ")
    Pesos = float(Pesos)
    dolares = Pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 

1} Pesos Colombianos
2} Pesos Mexicanos
3} Pesos Argentinos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 4000)
elif opcion == 2:
    conversor("Mexicanos", 30)
elif opcion == 3:
    conversor("Argentinos", 70)
else:
    print("Ingresa una opcion correcta por favor")
