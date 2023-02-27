from flask import Flask, render_template, request, redirect, url_for 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/elegir_categoria', methods=['GET', 'POST'])
def eleccion():
    if request.method == 'POST':
        categoria_elegida = request.form['categoria']
        return redirect()
    return render_template('eleccion.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/opciones_de_juego')
def opciones_de_juego():
    return render_template('opciones_de_juego.html')

if __name__ == '__main__':
    app.run(debug=True)