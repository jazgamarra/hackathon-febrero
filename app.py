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

    # Redireccionar a la pagina que correspodnda 
    if categoria == 'castellano': 
        url_nuestro = url_for('static', filename='game1/index.html')
    elif categoria == 'matematicas': 
        url_nuestro = url_for('static', filename='game2/index.html')
    elif categoria == 'gestion_emocional': 
        url_nuestro = url_for('static', filename='game3/index.html')
    
    return render_template('opciones_de_juego.html', url_juego=url_nuestro) 

@app.route('/crear_juego')
def crear_juego():
    if request.method == 'POST':
        request.form['pregunta']
        request.form['respuesta']
        request.form['incorrecta1']
        request.form['incorrecta2']

        print ('La pregunta es: ', request.form['pregunta'])
        print ('La respuesta es: ', request.form['respuesta'])
        print ('La incorrecta1 es: ', request.form['incorrecta1'])
        print ('La incorrecta2 es: ', request.form['incorrecta2'])
    
    return render_template('crear_juego.html')

if __name__ == '__main__':
    app.run(debug=True)      