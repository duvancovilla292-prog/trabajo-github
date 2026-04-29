def n():
    try:
        u = int(input("ingrese cantidad: "))
    except Exception:
        print("tiene que ser un numero ")
    z = input("ingrese cosa a colocar: ")
    for n in range(u+1):
        print(F"{z}"*n)

def num_phi():
    print((1+ 5**(1/2))/2)

n()
num_phi()