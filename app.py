from flask import Flask, render_template, request, redirect, url_for 
import requests 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/elegir_categoria', methods=['GET', 'POST'])
def eleccion():
    if request.method == 'POST':
        categoria_elegida = request.form['categoria']
        return redirect(url_for('opciones_de_juego', categoria=categoria_elegida))
    return render_template('elegir_categoria.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/opciones_de_juego', methods=['GET', 'POST'])
def opciones_de_juego():
    # Obtener la categoria a la que corresponde 
    try: 
        categoria = request.args['categoria']
    except: 
        print ('No se tiene una categoria valida')

    # Obtener la url del juego
    url_nuestro = redireccionar_al_juego(categoria)
    
    return render_template('opciones_de_juego.html', url_juego=url_nuestro, url_crear=url_for('crear_juego', categoria=categoria)) 

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

def redireccionar_al_juego(categoria): 
    # Redireccionar a la pagina que correspodnda 
    if categoria == 'castellano': 
        url_nuestro = url_for('static', filename='game1/index.html')
    elif categoria == 'matematicas': 
        url_nuestro = url_for('static', filename='game2/index.html')
    elif categoria == 'gestion_emocional': 
        url_nuestro = url_for('static', filename='game3/index.html')

    return url_nuestro

if __name__ == '__main__':
    app.run(debug=True)      

