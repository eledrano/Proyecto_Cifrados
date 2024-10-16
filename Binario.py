# Binario

def cifradoBinario(pTexto):
    dicBinario = {
        "A": "00000", "B": "00001", "C": "00010",
        "D": "00011", "E": "00100", "F": "00101",
        "G": "00110", "H": "00111", "I": "01000",
        "J": "01001", "K": "01010", "L": "01011",
        "M": "01100", "N": "01101", "O": "01110",
        "P": "01111", "Q": "10000", "R": "10001", "S": "10010",
        "T": "10011", "U": "10100", "V": "10101",
        "W": "10110", "X": "10111", "Y": "11000", "Z": "11001"
    } # Crear diccionario
    resultado = ""
    pTexto = pTexto.upper()
    for caracter in pTexto:
        if (caracter.isalpha() == True):
            pBinario = dicBinario[caracter]
            resultado += pBinario + " "
        else:
            resultado += "* "
    return resultado

print(cifradoBinario("tarea programada de criptografia datos zygalski Henryk"))