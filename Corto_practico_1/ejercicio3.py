def is_prime(n):
    if len(get_divisores(n)) == 2:
        return True
    else:
        return False


def get_divisores(n):
    divisores = []
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    print(divisores)
    return divisores


print(is_prime(8))
