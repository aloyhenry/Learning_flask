from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'Name': 'phone', 'Barcode': '893212299897', 'Price': 500},
         {'id': 2, 'Name': 'laptop', 'Barcode': '8345212299897', 'Price': 900},
          {'id': 3, 'Name': 'Keyboard', 'Barcode': '832212299897', 'Price': 150},
    ]
    return render_template('market.html', items= items)

