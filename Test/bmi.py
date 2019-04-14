from math import sqrt

from flask import Flask, request

app = Flask(__name__)
@app.route('/bmi/weight/height(in centimeter)')

def index():
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    bmi = int(weight / (height/100)**2)
    
    if bmi < 16:
        return "you're: Severely Underweight"
    elif bmi < 18.5:
        return "you're: Underweight"
    elif bmi < 25:
        return "you're: Normal"
    elif bmis < 30:
        return "you're: Overweight"
    else:
        return "you're: Obese"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
