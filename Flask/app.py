from flask import Flask, render_template, jsonify, request, redirect
from products import products


# Creamos el objeto de flask
app = Flask(__name__)


"""jsonify nos permite regresar valores en formato JSON"""


# Definición de rutas
@app.route('/')
def index():
    # Renderizamos el fichero de tipo php para nuestra ruta raiz
    return render_template('index.html')


# Ruta que retorna la documentación del web server
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
        product for product in products if product['type'] == product_name
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


# Ruta para agregar información por medio del metodo post
# Desde el formulario recibira una serie de valores y para esto es necesario
# que los inputs del formulario tengan los siguientes "name"
# - type -> para el tipo de producto
# - price -> para el precio del producto
# - quantity -> para la cantidad del producto
# - brand -> para la marca del producto
@app.route('/add_products', methods=['POST'])
def addItem():
    if request.method == 'POST':
        name = request.form['type']
        pice = request.form['price']
        quantity = request.form['quantity']
        brand = request.form['brand']
        # Agregamos lo nuevos valores a nuestra base de datos
        products.append(
            {
                "type": name,
                "price": pice,
                "quantity": quantity,
                "brand": brand
            }
        )
        # La retornamos a nuestro servidor
    return redirect('http://127.0.0.1/exampleRest/')


"""
if __name__ == "__main__":
    app.run(debug=True, port=8000)
"""
