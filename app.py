from flask import Flask, render_template, request, redirect, url_for 
import requests 

app = Flask(__name__)

# Funcion para obtener el diccionario de las URL de los juegos 
def obtener_urls(): 
    url = {
        'castellano': url_for('static', filename='game1/index.html'), 
        'matematicas1': url_for('static', filename='game2/index.html'),
        'matematicas2': url_for('static', filename='game2/index.html'),
        'gestion_emocional': url_for('static', filename='game3/index.html'), 
        'crear_juego': '#'
    }
    return url 

# Ruta de la pagina principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta de la pagina de eleccion de categoria
@app.route('/elegir_categoria', methods=['GET', 'POST'])
def eleccion():
    return render_template('elegir_categoria.html', url=obtener_urls())

# Ruta de la pagina de manual de usuario
@app.route('/manual')
def manual():
    return render_template('manual.html')

# Ruta de la pagina de crear juego
@app.route('/crear_juego', methods=['GET', 'POST'])
def crear_juego():
    if request.method == 'POST':
        try: 
            categoria = request.args['categoria']
        except: 
            categoria = None 
            print ('No se tiene una categoria valida')
             
        pregunta = request.form['pregunta']
        respuestas = request.form['respuesta']
        incorrecta1 = request.form['incorrecta1']
        incorrecta2 = request.form['incorrecta2']

        print (categoria, pregunta, respuestas, incorrecta1, incorrecta2)

    return render_template('crear_juego.html')

@app.route('/prueba_manual')
def prueba_manual():
    return render_template('prueba_manual.html')

if __name__ == '__main__':
    app.run(debug=True)      

