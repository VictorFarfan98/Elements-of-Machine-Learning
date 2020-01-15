def reverse(number):
    return int(''.join(reversed(str(number))))


def is_palindrome(number):
    return int(''.join(reversed(str(number)))) == number


def is_lychrel(number):
    attempts = 0
    while not is_palindrome(number) and attempts < 50:
        number += reverse(number)
        attempts += 1
        if is_palindrome(number):
            return False
    if is_palindrome(number):
        return False
    else:
        return True


cont = 0
for i in range(10000):
    if is_lychrel(i):
        cont += 1

print(cont)
# print(is_lychrel(196))
