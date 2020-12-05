from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# region TODAS LAS FUNCIONES


def suma(num1, num2):
    resultado = num1+num2
    return resultado


def resta(num1, num2):
    resultado = num1-num2
    return resultado


def multiplicacion(num1, num2):
    resultado = num1*num2
    return resultado


def division(num1, num2):
    resultado = num1/num2
    return resultado

# endregion



@app.route('/')
def index():
    return 'Hola Helmer, Iniciando proyecto de finanzas con python!'

@app.route('/hello')
def hello():
    return 'Hello, World'

# a continuacion vemos rutas que reciben parametros
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/calculadora/<int:num1>/<int:num2>/<int:opcion>')
def resultado(num1, num2, opcion):
    # region BUCLE
        res = 0
        if opcion == 1:
            res = suma(num1, num2)
            print(res)
            return("La suma de {0} y {1} es ".format(num1, num2) + " {0}".format(res))
        elif opcion == 2:
            res = resta(num1, num2)
            return("La resta de {0} y {1} es ".format(num1, num2), res)
        elif opcion == 3:
            res = multiplicacion(num1, num2)
            return ("La multiplicación entre {0} y {1} es ".format(num1, num2), escape(res))
        elif opcion == 4:
            res = division(num1, num2)
            print("La división entre {0} y {1}".format(
                num1, num2), "es {0:.2f}".format(res))
        elif opcion == 5:
            return("Has Finalizado.. Gracias.")
        else:
            return("Opción Invalida")

        # endregion





