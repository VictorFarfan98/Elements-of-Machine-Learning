def suma(x, y):
    return x+y
 
def resta(x, y):
    return x-y
 
def multi(x, y):
    return x*y
 


switcher = {
    1: suma,
    2: resta,
    3: multi
}

print("1. Suma")
print("2. Resta")
print("3. Multiplicar")
op = int(input("Escoga una opcion: "))
# Get the function from switcher dictionary

if op not in [1,2,3]:
    print("Invalid option")
else:
    func = switcher.get(op, lambda: "Invalid option")

    n1 = int(input("Ingreser el primer numero: "))
    n2 = int(input("Ingrese un segundo numero: "))

    # Execute the function
    print func(n1,n2)
