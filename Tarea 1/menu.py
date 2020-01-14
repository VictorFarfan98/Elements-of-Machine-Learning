class Menu:
    def Sumar(self, x, y):
        """Retorna la suma entre 2 numeros. """
        return x+y

    def Restar(self, x, y):
        """Retorna la resta entre 2 numeros. """
        return x-y

    def Multiplicar(self, x, y):
        """Retorna la multiplicacion entre 2 numeros. """
        return x*y

    def binary(self, name, oper):
        print("Bienvenido, hoy vamos a hacer la operacion binaria: {}".format(name))
        first_value = int(input("Ingrese el primer valor: "))
        second_value = int(input("Ingrese el segundo valor: "))
        return oper(first_value, second_value)

    def generateMenu(self, menu):
        """
        Given a Dictionary return and call any menu options.

        Keyword arguments:
        menu -- A dictionary in which key=option and value=function_name
        """
        return '\n'.join(
            [
                '{}. {}'.format(
                    key,
                    menu[key]
                ) for key in menu
            ]
        )


menuActual = {
    "1": "Sumar",
    "2": "Restar",
    "3": "Multiplicar"
}

titulo = input("Ingrese el titulo del programa: ")
print("Bienvenido al programa", titulo)
menu = Menu()

op = input(menu.generateMenu(menuActual)+"\nIngrese una opcion: ")
func = getattr(menu, menuActual[op])
print(menu.binary(menuActual[op], func))
