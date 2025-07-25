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

def pos_negt(list_num):
    pos, neg = 0,0
    for i in list_num:
        if i>=0: pos+=1
        else: neg +=1
    print(f"\n>  La cantidad de positivos es {pos} y de negativos es {neg}\n")

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

while True:
    print("-"*20+"Bienvenido"+"-"*20)
    break