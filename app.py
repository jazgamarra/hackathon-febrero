from flask import Flask, render_template, request, redirect, url_for 
import requests 

app = Flask(__name__)

# Funcion para obtener el diccionario de las URL de los juegos 
def obtener_url_juegos(categoria): 
    url = {
        'castellano': url_for('static', filename='game1/index.html'), 
        'matematicas1': url_for('static', filename='game2/index.html'),  # fracciones 
        'matematicas2': url_for('static', filename='game3/index.html'), # operaciones basicas 
        'gestion_emocional': url_for('static', filename='game4/index.html'), 
        'crear_juego': '#'
    }
    return url[categoria]

# Funcion para obtener el diccionario de las URL de los manuales 
def obtener_url_manuales():
    url = {
        'castellano': url_for('castellano'), 
        'matematicas1': url_for('matematicas1'),
        'matematicas2' : url_for('matematicas2'),
        'gestion_emocional': url_for('gestion_emocional'),
        'crear_juego': url_for('manual_crear_juego')
    }
    return url

# Ruta de la pagina principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta de la pagina de eleccion de categoria
@app.route('/elegir_categoria', methods=['GET', 'POST'])
def eleccion():
    return render_template('elegir_categoria.html', url=obtener_url_manuales())

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

@app.route('/matematicas1')
def matematicas1():
    return render_template('manuales/matematicas1.html', url=obtener_url_juegos('matematicas1')) 

@app.route('/matematicas2')
def matematicas2():
    return render_template('manuales/matematicas2.html', url=obtener_url_juegos('matematicas2'))

@app.route('/gestion_emocional')
def gestion_emocional():
    return render_template('manuales/gestion_emocional.html', url=obtener_url_juegos('gestion_emocional'))

@app.route('/castellano')
def castellano():
    return render_template('manuales/castellano.html', url=obtener_url_juegos('castellano'))

@app.route('/manual_crear_juego')
def manual_crear_juego():
    return render_template('manuales/manual_crear_juego.html', url=obtener_url_juegos('crear_juego'))

if __name__ == '__main__':
    app.run(debug=True)      


