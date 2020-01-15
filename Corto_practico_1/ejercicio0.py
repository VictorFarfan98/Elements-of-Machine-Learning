unidades = {
    0: "",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve"
}

decenas = {
    0: "",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    20: "veinte",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa"
}

cientos = {
    0: "",
    100: "ciento",
    200: "doscientos",
    300: "trescientos",
    400: "cuatrocientos",
    500: "quinientos",
    600: "seiscientos",
    700: "setecientos",
    800: "ochocientos",
    900: "novecientos"
}


def number_to_letters(n):
    centena = 0
    decena = 0
    unidad = 0
    if n > 1000:
        return "Out of range"
    elif n == 1000:
        return "mil"
    elif n == 0:
        return "cero"
    elif 1 <= n <= 9:
        return unidades[n]
    elif n >= 100:
        # Sacar la centena
        if n == 100:
            return "cien"
        centena = n - (n % 100)
        n = n % 100
    if n >= 10:
        # Sacar la decena
        if 10 <= n <= 15:
            decena = n
        else:
            decena = n - (n % 10)
            n = n % 10

            # Sacar la unidad
            unidad = n
    if 10 <= n <= 15:
        return "{} {} {}".format(
            cientos[centena],
            decenas[decena],
            unidades[unidad]
        )
    else:
        return "{} {} y {}".format(
            cientos[centena],
            decenas[decena],
            unidades[unidad]
        )


n = int(input("Ingrese el numero a convertir: "))
print(number_to_letters(n))
