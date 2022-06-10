from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello and welcome to my shop!!"


@app.route("/products")
def products():
    return render_template()
    

