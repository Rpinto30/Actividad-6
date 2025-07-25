
def entry_nums():
    while True:
        n = input("\n>  Ingrese una cantidad de números: ")
        if not n.isdigit():
            print("\n>  Lo siento, intentelo de nuevo")
        else:
            break
    nums = []
    for i in range(int(n)):
        num = int(input(f"{i + 1}) Ingresa numero: "))
        nums.append(num)
    return nums

#FUNCIONES
def total_sum(list_num):
    s = 0
    for i in list_num: s+=i
    return s

def average(list_num):
    return total_sum(list_num)/len(list_num)


def pos_negt(list_num):
    pos, neg = 0,0
    for i in list_num:
        if i>=0: pos+=1
        else: neg +=1
    print(f"\n>  La cantidad de positivos es {pos} y de negativos es {neg}\n")

def triangle_area(base,height):
    return base*height/2

def pairnum(num):
    if num %2 == 0: print(f"El numero {num} es par")
    else: print(f"\n>  El numero {num} es impar")

def mayor_minus():
    num_list = entry_nums()
    mayor = num_list[0]
    minus = num_list[0]
    for l in num_list:
        if l >= mayor: mayor = l
        if l <= minus: minus = l
    print(f"\n>  El número mayor es {mayor}, el número menor es {minus}")

while True:
    print("-" * 10 + "Bienvenido" + "-" * 10)
    print("1) Ingresar n números\n2) Calcular el area de un triangulo\n3) Verificar si un número es par\n4) Calcular el promedio de n calificaciones\n5) Ingresar n números y mostrar mayor y menor\n6) Salir")
    op_main = input("Ingrese una de las opciones: ")
    match op_main:
        case '1':
            nums = entry_nums()
            print("-"*30)
            while True:
                print("-"*25)
                print("  1) Suma total\n  2) El promedio\n  3) cantidad de positivos y negativos\n  4) Salir")
                op_op1 = input("Ingresa una de las opciones: ")
                match op_op1:
                    case '1': print(f"\n>  La suma total es {total_sum(nums)}\n")
                    case '2': print(f"\n>  El promedio es {average(nums)}\n")
                    case '3': pos_negt(nums)
                    case '4': break
                    case _: print("\n>  Lo siento, vuevlva a intentarlo\n")
        case '2':
            base = int(input("\nIngrese la base de su traingulo: "))
            height = int(input("Ingrese la altura de su traingulo: "))
            print(f"\n>  El area de su triangulo es: {triangle_area(base,height)}\n")
        case '3':
            n = int(input("Ingrese un número: "))
            pairnum(n)
        case '4':
            nums = entry_nums()
            print(f"\n>  El promedio de las calificaciones ingresadas es: {average(nums)}\n")
        case '5': mayor_minus()
        case '6': break
        case _: print("\n>  Lo siento, vuevlva a intentarlo\n")

print("\nHasta pronto!")
print("Inge no me regañe :c no fue mi culpa, fue culpa del bus")