# Mensaje Inverso

def cifrarMensajeInverso(pTexto):
    resultado = ""
    while (pTexto != ""):
        resultado = pTexto[0] + resultado
        pTexto = pTexto[1:]
    return resultado

# print(cifrarMensajeInverso("Hola mi nombre es Python"))