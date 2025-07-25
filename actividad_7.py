#Reutilizados del ejercicio no.6
def entry_nums():
    while True:
        n = input("\n>  Ingrese una cantidad de números: ")
        if not n.isdigit(): print("\nLo siento, intentelo de nuevo")
        else: break
    nums = []
    for i in range(int(n)):
        while True:
            try:
                num = int(input(f"{i + 1}) Ingresa numero: "))
                break
            except: print("\nLo siento, intentelo de nuevo")
        nums.append(num)
    return nums

def total_sum(list_num):
    s = 0
    for i in list_num: s+=i
    return s

def average(list_num):
    return total_sum(list_num)/len(list_num)

def mayor_that(list_num, mayor, txt):
    pos, neg = 0,0
    for i in list_num:
        if i>=mayor: pos+=1
        else: neg +=1
    print(txt)

#FUNCIONES EXCLUSIVAS DEL EJERCICIO 7
def mult_3(list_num):
    m3 = 0
    for i in list_num:
        if i%3==0: m3 +=1
    return m3

def rect_area(base, height):
    return base*height

def rect_perimet(x,y):
    return 2*(x+y)

def prime_number(num):
    if num <= 1 or int(num) != num: print("\nSolo pueden ser considerados primero los enteros positivos mayores que 1")
    else:
        for i in range(2,num):
            print(i)
            if num%i == 0:
                print(f"\nEl número {num} no es primo")
                break
        else: print(f"\nEl número {num} es primo")

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

    print(f"{'Repetidos':<15}{'Frecuencia'}")
    for j in repeat: print(f"{j:<15}{repeat[j]}")



while True:
    print("-"*20+"Bienvenido"+"-"*20)
    break