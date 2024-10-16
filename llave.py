# Función para convertir letra a número (a = 1, b = 2, ..., z = 26)
def convertirLetraNumero(pLetra):
    return ord(pLetra.lower()) - 96

# Función para convertir número a letra (1 = a, 2 = b, ..., 26 = z)
def convertirNumeroLetra(pNumero):
    # Ajustamos si el número excede 26 o es menor que 1 (módulo 26 para el alfabeto)
    if (pNumero > 26):
        pNumero -= 26
    elif (pNumero < 1):
        pNumero += 26
    return chr(pNumero + 96)

# Cifrado llave
def cifrarLlave(pTexto, clave):
    pTexto = pTexto.lower()  # Convertimos a minúsculas
    clave = clave.lower()  # Convertimos la clave a minúsculas
    resultado = ""  # Donde se almacenará el texto cifrado
    letrasEnClave = len(clave)  # Longitud de la clave
    indice = 0  # Índice para recorrer la clave

    # Recorremos cada carácter del texto
    for letra in pTexto:
        if (letra.isalpha()):  # Procesamos solo las letras (ignoramos espacios)
            pValorLetra = convertirLetraNumero(letra)  # Convertimos la letra a número
            
            # Aseguramos que el índice de la clave no exceda su longitud
            pValorClave = convertirLetraNumero(clave[indice % letrasEnClave])  # Valor de la letra de la clave

            # Sumamos los valores para cifrar y ajustamos con módulo 26
            letraCifrada = (pValorLetra + pValorClave - 1) % 26 + 1
            
            # Convertimos el valor resultante a letra y lo añadimos al resultado
            resultado += convertirNumeroLetra(letraCifrada)

            indice += 1  # Avanzamos en la clave
        else:
            # Si es un espacio, lo mantenemos como está y reiniciamos el índice de la clave
            resultado += letra
            indice = 0  # Reiniciamos la clave al encontrar un espacio

    return resultado

# Descifrado llave
def descifrarLlave(pTexto, clave):
    pTexto = pTexto.lower()  # Convertimos a minúsculas
    clave = clave.lower()  # Convertimos la clave a minúsculas
    resultado = ""  # Donde se almacenará el texto descifrado
    letrasEnClave = len(clave)  # Longitud de la clave
    indice = 0  # Índice para recorrer la clave

    # Recorremos cada carácter del texto
    for letra in pTexto:
        if (letra.isalpha()):  # Procesamos solo las letras (ignoramos espacios)
            pValorLetra = convertirLetraNumero(letra)  # Convertimos la letra a número
            
            # Aseguramos que el índice de la clave no exceda su longitud
            pValorClave = convertirLetraNumero(clave[indice % letrasEnClave])  # Valor de la letra de la clave

            # Restamos los valores para descifrar y ajustamos con módulo 26
            letraDescifrada = (pValorLetra - pValorClave + 26 - 1) % 26 + 1
            
            # Convertimos el valor resultante a letra y lo añadimos al resultado
            resultado += convertirNumeroLetra(letraDescifrada)

            indice += 1  # Avanzamos en la clave
        else:
            # Si es un espacio, lo mantenemos como está y reiniciamos el índice de la clave
            resultado += letra
            indice = 0  # Reiniciamos la clave al encontrar un espacio

    return resultado

# Ejemplos de uso
# print(cifrarLlave("tarea programada de codificacion", "tango"))
# print(descifrarLlave("nbflp jscngunokp xf wprpucdojxio", "tango"))