from math import sqrt

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def index(weight, height):
    # weight = request.args.get('weight', type=float)
    # height = request.args.get('height', type=float)
    bmi = int(weight / (height/100)**2)

    return render_template('bmi_calc.html', bmi=bmi)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)