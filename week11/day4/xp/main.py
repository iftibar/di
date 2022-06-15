from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('template.html')


@app.route("/products")
def products():
    return render_template("")


@app.route("/products/<product_id>")
def product(product_id):
    return render_template("", product_id=product_id)


if __name__ == "__main__":
    app.run(debug=True)