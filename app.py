from flask import Flask, render_template, request, redirect
import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    calculator = main.Currency_Calculator()
    calculator.get_rates()
    if request.method == 'GET':
        items = []
        for element in calculator.rates:
            items.append(element['code'])

        return render_template('form.html', items=items)

    elif request.method == 'POST':
        return redirect('/rate')
        
@app.route('/rate', methods=['POST'])
def rates():
    calculator = main.Currency_Calculator()
    calculator.get_rates()
    data = request.form
    currency_code = data.get('currency')
    quantity = data.get('quantity')
    for element in calculator.rates:
        if currency_code == element['code']:
            code=element['code']
            value = round(float(quantity)*element['bid'],2)
    return render_template('form.html', value=value, code=code, quantity=quantity)
    
