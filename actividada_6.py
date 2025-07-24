print("Commit")
print("-"*10+"Bienvenido"+"-"*10)

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
    print(f"La cantidad de positivos es {pos} y de negativos es {neg}")

def triangle_area(base,height):
    return base*height/2

def pairnum(num):
    if num %2 == 0: print(f"El numero {num} es par")
    else: print(f"El numero {num} es impar")

def mayor_minus():
    while True:
        nums_range = input("Ingrese una cantidad de números: ")
        if nums_range.isdigit(): break
        else: print("\nLo siento, intente nuevamente")
    num_list = []
    for k in range(int(nums_range)+1):
        num_inp = int(input(f"{k+1}) Ingrese un número: "))
        num_list.append(num_inp)
    mayor = num_list[0]
    minus = num_list[0]
    for l in num_list:
        if l >= mayor: mayor = i
        if l <= minus: minus = i
    print(f"El número mayor es {mayor}, el número menor es {minus}")


while True:
    print("1) Ingresar n números\n2) Calcular el area de un triangulo\n3) Verificar si un número es par\n4) Calcular el promedio de n calificaciones\n Ingresar n números y mostrar mayor y menor\n 6) Salir")
    op_main = input("Ingrese una de las opciones: ")
    match op_main:
        case '1': #TODO ESTO ES LA OPCION 1
            while True:
                n = input("Ingrese una cantidad de números: ")
                if not n.isdigit(): print("Lo siento, intentelo de nuevo")
                else: break
            nums = []
            for i in range(int(n)):
                num = int(input(f"{i+1}) Ingresa numero: "))
                nums.append(num)
            print("-"*30)
            while True:
                print("  1) Suma total\2  2) El promedio\n  3) cantidad de positivos y negativos\n  4) Salir")
                op_op1 = input("Ingresa una de las opciones")
                match op_op1:
                    case '1': print(f"La suma total es {total_sum(nums)}")
                    case '2': print(f"El promedio es {average(nums)}")
                    case '3': pos_negt(nums)
                    case '4': break
                    case _: print("\nLo siento, vuevlva a intentarlo")

        case _: print("\nLo siento, vuevlva a intentarlo")