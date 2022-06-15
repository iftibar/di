from flask import  Flask, render_template, url_for
app = Flask(__name__)

app.route('/')
def home():
    return render_template('index.html')


app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return "form submitted"