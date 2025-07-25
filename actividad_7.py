#Reutilizados del ejercicio no.6
def entry_nums():
    while True:
        n = input("\n>  Ingrese una cantidad de valores: ")
        if not n.isdigit(): print("\n>  Lo siento, intentelo de nuevo\n")
        else: break
    nums = []
    for i in range(int(n)):
        while True:
            try:
                num = float(input(f"{i + 1}) Ingresa numero: "))
                if int(num) == num: num = int(num) #SOLO PARA QUE NO SALGA EL .0 CUANDO SON ENTEROS
                break
            except ValueError : print("\n>  Lo siento, intentelo de nuevo\n")
        nums.append(num)
    return nums

def total_sum(list_num):
    s = 0
    for i in list_num: s+=i
    return s

def average(list_num): return total_sum(list_num)/len(list_num)

def mayor_that(list_num, mayor, txt, minus):
    pos, neg = 0,0
    for i in list_num:
        if i>=mayor: pos+=1
        else: neg +=1
    if minus: print(f"Hay {neg} {txt} menores a {mayor}")
    else:print(f"Hay {pos} {txt} mayores a {mayor}")

def pos_neg(list_num):
    zeros, pos, neg = 0,0,0
    for i in list_num:
        if i == 0: zeros+=1
        elif i>=0: pos+=1
        else: neg +=1
    print(f"\n>  La cantidad de positivos es {pos} y de negativos es {neg}")
    print(f">  La cantidad de ceros es: {zeros}\n")

#FUNCIONES EXCLUSIVAS DEL EJERCICIO 7
def mult_3(list_num):
    m3 = 0
    for i in list_num:
        if i%3==0: m3 +=1
    return m3

def rect_area(base, height): return base*height

def rect_perimet(x,y): return 2*(x+y)

def prime_number(num):
    if num <= 1: print("\n>  Solo pueden ser considerados primero los enteros positivos mayores que 1\n")
    else:
        for i in range(2,num):
            print(i)
            if num%i == 0:
                print(f"\n>  El número {num} no es primo\n")
                break
        else: print(f"\n>  El número {num} es primo\n")

def mayor_minus(num_list,txt):
    mayor = num_list[0]
    minus = num_list[0]
    for l in num_list:
        if l >= mayor: mayor = l
        if l <= minus: minus = l
    print(txt)

def repeat_on_list(num_list):
    repeat = {}
    copy = []
    for i in num_list:
        if i not in copy: copy.append(i)
        else:
            if i not in repeat: repeat[i] = 2 #detecta si ya existia uno anterior igual al actual, por eso 2
            else: repeat[i] += 1
    print("")
    print(f"{'Repetidos':<15}{'Frecuencia'}")
    for j in repeat: print(f"{j:<15}{repeat[j]}")

def sum_nums(x,y): return x+y
def dif_nums(x,y): return x-y
def mult_nums(x,y): return x*y
def div_nums(x,y):
    try: return x/y
    except ZeroDivisionError: return 0

while True:
    print("-"*30+"Bienvenido"+"-"*30)
    print("1) Ingresar n números reales\n2) Calcular el perimetro y area de un rectángulo\n3) Verificar si un número es primo\n4) Calcular el promedio de n calificaciones\n5) Ingresar n números enteros\n6) Calculadora\n7) Salir")
    op = input("Ingrese una de las opciones: ")
    match op:
        case '1':
            nums = entry_nums()
            while True:
                print("-"*15+f"Que desea hacer con {nums}?"+"-"*15)
                print("  1) Suma total\n  2) Promedio\n  3) Cantidad de positivos, negativos y ceros\n  4) Cuantos son multiplos de 3\n  5) Salir")
                op_1 = input("Ingrese una de las opciones: ")
                match op_1:
                    case '1': print(f"\n>  La suma total es {total_sum(nums)}")
                    case '2': print(f"\n>  El promedio total es {average(nums)}")
                    case '3': pos_neg(nums)
                    case '4': print(f"\n>  Existen {mult_3(nums)} numeros multiplos de 3")
                    case '5': break
                    case _: print("\n>  Entrada no valida, intente nuevamente\n")
        case '2':
            print("-"*15+"Área y perimetro de un rectangulo"+"-"*15)
            while True:
                try:
                    base = float(input("Ingrese la base de su rectangulo: "))
                    height = float(input("Ingrese la altura de su rectangulo: "))
                    break
                except ValueError: print("Lo siento, vuelva a intentarlo")
            print(f"\n>  El area de su rectangulo es {rect_area(base,height)} y el perimetro es {rect_perimet(base,height)}")
        case '3':
            print("-" * 15 + "Numero primo" + "-" * 15)
            num = int(input("Ingrese un número entero positivo: "))
            prime_number(num)
        case '4':
            values = entry_nums()
            while True:
                print("-" * 15 + f"Calificaciones: {values}/Promedio:{average(values)}" + "-" * 15)
                print("  1) Mostrar notas mayores o iguales a 85\n  2) Mostar nostas en zona de riesgo\n  3) Salir")
                op_4 = input("Ingrese una de las opciones: ")
                match op_4:
                    case '3': break
                    case _: print("\n>  Entrada no valida, intente nuevamente")

        case '7': break
        case _: print("\n>  Entrada no valida, intente nuevamente")