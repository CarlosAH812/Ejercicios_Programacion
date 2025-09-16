def ordersnakecase(text):
    words_list = text.split('-')
    words_list.sort()
    return '-'.join(words_list)

print(ordersnakecase("computer-function-monitor-python-variable"))


#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#   A. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#   B. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”