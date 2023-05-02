### Exceptions Handling ###

numberOne, numberTwo = 5, 1

# numberTwo = "1"

# try except
try:
    print(numberOne+numberTwo)
    print("No se ha producido error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# numberTwo = "1"
# try except else
try:
    print(numberOne+numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua")

numberTwo = "1"
# try except else finally
try:
    print(numberOne+numberTwo)
    print("No se ha producido error")
except:     # el except es obligatorio
    print("Se ha producido un error")
else:       # el else es opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:    # el finally es opcional
    print("la ejecucion continua")

# Excepciones por tipo

try:
    print(numberOne+numberTwo)
    print("No se ha producido error")
except TypeError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")
except ValueError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")

try:
    print(numberOne+numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
