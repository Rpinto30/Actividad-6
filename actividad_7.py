#Reutilizados del ejercicio no.6
def entry_nums(only_integers=False):
    while True:
        n = input("\n>  Ingrese una cantidad de valores: ")
        if not n.isdigit(): print("\n>  Lo siento, intentelo de nuevo\n")
        else: break
    nums = []
    for i in range(int(n)):
        while True:
            try:
                if only_integers:  num = int(input(f"{i + 1}) Ingresa numero: ")) #SOLO PIDE ENTEROS Y NO ADMITE FLOTANTES
                else:
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
    if minus: print(f">  Hay {neg} {txt} menores a {mayor}")
    else:print(f">  Hay {pos} {txt} mayores a {mayor}")

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
            if num%i == 0:
                print(f"\n>  El número {num} no es primo\n")
                break
        else: print(f"\n>  El número {num} es primo\n")

def mayor_minus(num_list,mayor_option):
    mayor = num_list[0]
    minus = num_list[0]
    for l in num_list:
        if mayor_option:
            if l >= mayor: mayor = l
        else:
            if l <= minus: minus = l
    if mayor_option: return mayor
    else: return minus

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
                    case '4':
                        if mult_3(nums) == 1: print(f"\n>  Existe 1 numero multiplo de 3")
                        else: print(f"\n>  Existen {mult_3(nums)} numeros multiplos de 3")
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
                    case '1': mayor_that(values, 85, 'notas', False)
                    case '2': mayor_that(values, 60, 'notas', True)
                    case '3': break
                    case _: print("\n>  Entrada no valida, intente nuevamente")
        case '5':
            nums_list = entry_nums(True)
            while True:
                print("-" * 15 + f"Lista de números: {nums_list}" + "-" * 15)
                print("  1) Mostrar número mayor\n  2) Mostar número menor\n  3) Cuantos se repiten\n  4) Salir")
                op_5 = input("Ingrese una de las opciones: ")
                match op_5:
                    case '1': print(f">  El número mayor es: {mayor_minus(nums_list, True)}")
                    case '2':print(f">  El número menor es: {mayor_minus(nums_list, False)}")
                    case '3': repeat_on_list(nums_list)
                    case '4': break
                    case _: print("\n>  Entrada no valida, intente nuevamente")
        case '6':
            while True:
                try:
                    n1 = float(input("Ingrese un número: "))
                    n2 = float(input("Ingrese otro número: "))
                    break
                except ValueError: print("\n>  Lo siento, intente nuevamente")

            while True:
                print("-" * 15 + f"Calculadora con números {n1} y {n2}" + "-" * 15)
                print("  1) Sumar\n  2) Restar\n  3) Multiplicar\n  4) Divirir\n  5) Salir")
                op_6 = input("Ingrese una de las opciones: ")
                match op_6:
                    case '1': print(f">  La suma entre {n1} y {n2} es {sum_nums(n1,n2)}")
                    case '2': print(f">  La resta entre {n1} y {n2} es {dif_nums(n1,n2)}")
                    case '3': print(f">  La multiplicacion entre {n1} y {n2} es {mult_nums(n1,n2)}")
                    case '4':
                        if div_nums(n1,n2) == 0: print(">  la division por 0 no e6stá definida")
                        else: print(f">  La division entre {n1} y {n2} es {div_nums(n1,n2)}")
                    case '5': break
                    case _: print("\n>  Entrada no valida, intente nuevamente")
        case '7':
            print("\nHasta pronto!")
            break
        case _: print("\n>  Entrada no valida, intente nuevamente")