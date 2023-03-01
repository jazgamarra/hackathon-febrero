from flask import Flask, render_template, request, redirect, url_for 
import qrcode
from PIL import Image

app = Flask(__name__)

# Funcion para obtener el diccionario de las URL de los juegos 
def obtener_url_juegos(categoria): 
    url = {
        'castellano': url_for('static', filename='game1/index.html'), 
        'matematicas1': url_for('static', filename='game2/index.html'),  # fracciones 
        'matematicas2': url_for('static', filename='game3/index.html'), # operaciones basicas 
        'gestion_emocional': url_for('static', filename='game4/index.html'), 
        'crear_juego': url_for('static', filename='game1/index.html')
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
    return render_template('crear_juego.html', url=obtener_url_juegos('crear_juego'))

@app.route('/idiomas')
def idiomas():
    return render_template('idiomas.html')  

def qr_generator(url): 
    # Pasamos el logo que vamos a utilizar en el qr code como una imagen
    logo_link = './static/images/abrazo.png'
    logo = Image.open(logo_link)

    # Pasamos los parametros de tamaño y color para nuestro codigo QR
    basewidth = 100
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    # Creamos una variable para almacenar el codigo de error en caso de que al generar el QR ocurra un errors
    Qrcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Generamos la ruta a la que nuestro codigo QR va a redireccionar
    Qrcode.add_data(url)
    # Generamos el codigo QR
    qrcode.make()

    # Pasamos los parametros de color y posicion de nuestro logo, tambien definimos el color que tendra nuestro QR
    qrcolor = 'Black'
    qrimg = Qrcode.make_image(fill_color=qrcolor, back_color="orange").convert('RGB')
    pos = ((qrimg.size[0] - logo.size[0]) // 2, (qrimg.size[1] - logo.size[1]) // 2)
    qrimg.paste(logo, pos)
    # Guardamos nuestro codigo QR generado como una imagen
    qrimg.save(f'static/jaggy.png')
    # Mostramos un texto una vez que el codigo QR haya sido generado con exito
    print('Codigo QR generado con exito') 

@app.route('/generar_qr')
def generar_qr(): 
    ip = '192.168.100.130:8080'
    url = 'http://'+ip+'/static/game2/index.html'
    qr_generator (url)
    imagen = '/static/jaggy.png'
    return render_template('visualizar_qr.html', imagen=imagen)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080) 