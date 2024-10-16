# Telefonico

def cifradoTelefonico(pTexto):
    dicTelefono = {
        "A": 21, "B": 22, "C": 23,
        "D": 31, "E": 32, "F": 33,
        "G": 41, "H": 42, "I": 43,
        "J": 51, "K": 52, "L": 53,
        "M": 61, "N": 62, "O": 63,
        "P": 71, "Q": 72, "R": 73, "S": 74,
        "T": 81, "U": 82, "V": 83,
        "W": 91, "X": 92, "Y": 93, "Z": 94
        } # crear diccionario
    resultado = ""
    pTexto = pTexto.upper()
    for caracter in pTexto:
        if (caracter.isalpha()):
            numero = dicTelefono[caracter]
            resultado += (str(numero) +" ")
        else:
            resultado += "* "
    return resultado

# print(cifradoTelefonico("tarea programada de criptografia de datos zygalski Henryk"))