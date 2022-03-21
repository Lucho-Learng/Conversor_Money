# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("!The best!")


# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print("Hola")
    print("como estas")
    print(mensaje)
    print("Que pases bien")


opcion = int(input("Elige la opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegistes la opcion # 1")
elif opcion == 2:
    conversacion("Elegistes la opcion # 2")
elif opcion == 3:
    conversacion("Elegistes la opcion # 3")
else:
    print("Escribe la opcion correcta")
