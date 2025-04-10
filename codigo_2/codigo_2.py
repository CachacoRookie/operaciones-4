# Estudiante: corrige este código y haz un pull request con la versión corregido.
def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():  # Convertir a minusculas
        if letra in 'aeiou':
            contador += 1
    return contador

print(contar_vocales("Programacion"))
