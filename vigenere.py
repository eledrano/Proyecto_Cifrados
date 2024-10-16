def convertirLetraNumero(pLetra):
    return ord(pLetra.lower()) - 96

def convertirNumeroLetra(pNumero):
    if (pNumero > 26):
        pNumero -= 26
    elif (pNumero < 1):
        pNumero += 26
    return chr(pNumero + 96)

def esPar(pNum):
    return pNum % 2 == 0

# Cifrado Vigenere
def cifrarVigenere(pTexto, pCifra):
    contador = 1
    resultado = ""
    for caracter in pTexto:
        if (caracter.isalpha()):
            pValor = convertirLetraNumero(caracter)
            if (esPar(contador)):
                pValor += (pCifra % 10)
            else:
                pValor += (pCifra // 10)
            letraCifrada = convertirNumeroLetra(pValor)
            resultado += letraCifrada
        else:
            resultado += caracter
            contador = 0
        contador += 1
    return resultado

# Descifrado Vigenere
def descifrarVigenere(pTexto, pCifra):
    contador = 1
    resultado = ""
    for caracter in pTexto:
        if (caracter.isalpha()):
            pValor = convertirLetraNumero(caracter)
            if (esPar(contador)):
                pValor -= (pCifra % 10)
            else:
                pValor -= (pCifra // 10)
            letraDescifrada = convertirNumeroLetra(pValor)
            resultado += letraDescifrada
        else:
            resultado += caracter
            contador = 0
        contador += 1
    return resultado

# Ejemplos de uso
# print(cifrarVigenere("tarea programada criptografia de datos, 23"))
# print(descifrarVigenere("vdthc ruqjtdodfd euksvriucikd fh fdvru", 23))