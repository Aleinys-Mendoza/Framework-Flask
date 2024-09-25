"""Ejercico 1:crea una aplicacion web basica con flask que, 
 al ser ejecutada, inicia un servidor local en el puerto 5000,
 cuando  visita la ruta principal (http://127.0.0.1:5000) ,
 el servidor respondera con un mensaje HTML aque dice hello,word Flask"""

#Se importa el modulo Flak desde el paquete flask

from flask import Flask

#Crea una instacia de la clase Flask
"""El argumento __name__ le dice a flask
que utilice el nombre del archivo actual main.py"""
app = Flask(__name__)

#Este es un decorador que define la ruta correspondiente a la pagina
@app.route('/')

#Cuando alguien visita app (por ejempo, http://localhost:5000/)
#la funcion hello () sera ejecutada
def hello():
    return "¡Hola, mundo!"

#Solo se ejecute si el archivo es ejecutado directamente 
#aracando la aplicacion de flask en odo de depuracion (debug=true)
if __name__ == '__main__':
    app.run(debug=True,port=5000)
