# Cifrado Cesar

def cifrarCesar(pTexto):
    resultado = ""
    for caracter in pTexto:
        if (caracter.isalpha() == True): # Validar que caracter sea una letra
            letraCifrada = ord(caracter) # La funcion ord ubica la letra como un valor numerico

            if (letraCifrada >= 97 and letraCifrada <= 122): # Determinar si la letra es minúscula
                letraCifrada = (letraCifrada - ord("a") + 3) % 26 + ord("a")
            # Se suman 3 de desplazamiento y % 26 por las letras del alfabeto

            elif (letraCifrada >= 65 and letraCifrada <= 90): # Determinar si la letra es mayúscula
                letraCifrada = (letraCifrada - ord("A") + 3) % 26 + ord("A")

            resultado += chr(letraCifrada) # La funcion chr transforma el valor numerico a letra y se suma a resultado
        else:
            resultado += caracter # Si caracter no es una letra solo se suma
    return resultado

# Función para descifrar usando el método César
def descifrarCesar(pTexto):
    resultado = ""
    for caracter in pTexto:
        if (caracter.isalpha() == True): # Validar que caracter sea una letra
            letraCifrada = ord(caracter) # La funcion ord ubica la letra como un valor numerico

            if (letraCifrada >= 97 and letraCifrada <= 122): # Determinar si la letra es minúscula
                letraCifrada = (letraCifrada - ord("a") - 3) % 26 + ord("a")
            # Se restan 3 de desplazamiento y % 26 por las letras del alfabeto

            elif (letraCifrada >= 65 and letraCifrada <= 90): # Determinar si la letra es mayúscula
                letraCifrada = (letraCifrada - ord("A") - 3) % 26 + ord("A")

            resultado += chr(letraCifrada) # La funcion chr transforma el valor numerico a letra y se suma a resultado
        else:
            resultado += caracter # Si caracter no es una letra solo se suma
    return resultado

# Ejemplos de uso
# print(cifrarCesar("Hola Mundo"))
# print(descifrarCesar("Krod Pxqgr"))