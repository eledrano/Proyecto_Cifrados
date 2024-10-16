# Palabra Inversa

def cifrarMensajeInverso(pTexto):
    resultado = ""
    while (pTexto != ""):
        resultado = pTexto[0] + resultado
        pTexto = pTexto[1:]
    return resultado

def cifrarPalabraInversa(pTexto):
    resultado = ""
    pInversa = ""
    for caracter in pTexto:
        if (caracter.isalpha()== True):
            pInversa += caracter
        else:
            pInversa = cifrarMensajeInverso(pInversa)
            resultado += pInversa + caracter
            pInversa = ""
    resultado += cifrarMensajeInverso(pInversa)
    return resultado

# print(cifrarPalabraInversa("esto es un secreto no lo puedo decir, aserpros"))