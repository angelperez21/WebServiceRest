from flask import Flask, render_template, jsonify
from products import products


# Creamos el objeto de flask
app = Flask(__name__)


# jsonify nos permite regresar valores en formato JSON

# Definición de rutas
@app.route('/')
def index():
    # Renderizamos el fichero de tipo php para nuestra ruta raiz
    return render_template('index.html')


@app.route('/documentacion')
def documentacion():
    return render_template('documentacion.html')


# Por defecto el servidor realiza llamadas por medio de GET
@app.route('/products')
def getProducts():
    return jsonify(products)


# Definimos una ruta que recibe una variable de tipo string por medio de get
# tambien de podría poner de la siguiente manera
# @app.route('/products/<tipo_de_dato:nombre_de_la_variable>', methods=['GET])
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # obtenemos solo el producto solicitado
    product_found = [
        product for product in products if product['name'] == product_name
    ]
    # Si el tamaño de la lista es mayor a 0 entonces existen productos
    if (len(product_found) > 0):
        # Retornamos el producto o productos encontrados
        return jsonify(
            product_found
        )
    return jsonify([
            {
                "product": "Producto no encontrado"
            }
        ]
    )


# Ruta de ejemplo en caso de no colocar el tipo de dato se asignara solo por
# defecto
@app.route('/ejemplo/<string:name>')
def ejemplo(name):
    return jsonify(
        {
            'menssge': f'Hola {name} como estas'
        }
    )

