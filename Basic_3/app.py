from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')
@app.route('/home')

def home_page():
    return render_template('home.html',name="Sagnik")

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Smart Phone', 'barcode': '3334453464', 'price': 10000},
        {'id': 2, 'name': 'Gaming Laptop', 'barcode': '12534546473165', 'price': 90000},
        {'id': 3, 'name': 'Light Keyboard', 'barcode': '345345323546', 'price':1600}  ]
    return render_template('market.html', items=items)

app.run(host='0.0.0.0', port=8080)