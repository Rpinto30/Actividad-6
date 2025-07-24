print("Commit")
print("-"*10+"Bienvenido"+"-"*10)
while True:
    print("1) Ingresar n números\n2) Calcular el area de un triangulo\n3) Verificar si un número es par\n4) Calcular el promedio de n calificaciones\n Ingresar n números y mostrar mayor y menor\n 6) Salir")
    op_main = input("Ingrese una de las opciones: ")
    match op_main:
        case _: print("\nLo siento, vuevlva a intentarlo")