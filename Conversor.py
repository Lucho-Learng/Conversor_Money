Pesos = input("Cuantos pesos colombianos tienes?: ")
Pesos = float(Pesos)
valor_dolar = 4000
dolares = Pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
