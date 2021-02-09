from flask import Flask
from random import random, randint


app = Flask(__name__)

@app.route('/lineal/<int:n>/<int:value>', methods = ['GET'])
def lineal(n, value):
    array = []
    txt = "lista: "
    cont = 0
    for i in range(n):
        array.append(randint(1,n))
        txt += f"{array[i]}. "
    txt += '\n'

    for j in array:
        if j == value:
            txt += f"Felicidades! El numero {value} se ha encontrado en la lista :)"
            return txt
        else:
            cont = cont + 1

    if cont == n:
        txt += "Numero no encontrado :("
        return txt

@app.route('/binaria/<int:n>/<int:value>', methods = ['GET'])
def binaria(n, value):
    array = []
    txt = "No encontrado :("

    for i in range(n):
        array.append(i + 1)
    
    c = 0
    fin = len(array) - 1
    while c <= fin:
        medio = (c + fin) // 2
        print (medio)
        if array[medio] == value:
            txt = f"Felicidades! El numero {value} se ha encontrado en la lista :)"
            return txt
        else:
            if array[medio] > value:
                fin = medio - 1
            else:
                c = medio + 1
    return txt

if __name__ == '__main__':
    app.run(host='localhost', port=5000)