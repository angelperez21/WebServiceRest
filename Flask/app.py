from flask import Flask, render_template, jsonify
from products import products
app = Flask(__name__)


# Definición de rutas
@app.route('/')
def index():
    return render_template('index.php')


@app.route('/ping')
def ping():
    return jsonify(
        {
            'message': 'Pong'
        }
    )


@app.route('/products')
def getProducts():
    return jsonify(products)


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    product_found = [
        product for product in products if product['name'] == product_name
    ]
    if (len(product_found) > 0):
        return jsonify(
            {
                "product": product_found[0]
            }
        )
    return jsonify(
        {
            "product": "Producto no encontrado"
        }
    )
