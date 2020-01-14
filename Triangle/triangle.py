def triangle(n):
    triangle = ""
    maxx = n * 2
    for i in range(1, n+1):
        cur = ""
        for j in range(i):
            cur += "*"
            cur += " "
        suma = (maxx-len(cur))/2
        cur = " "*suma + cur
        triangle += cur + "\n"
    return triangle

print(triangle(4))


def cuadrado(n):
    return n*n 

result = map(cuadrado, list(range(1, 101)))
print(result)