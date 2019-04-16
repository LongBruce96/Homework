from math import sqrt

from flask import Flask, request

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def index(weight, height):
    
        bmi = int(weight / (height/100)**2)
        # return "Your BMI is:" + str(bmi)

        if bmi < 16:    
                return  "Your BMI is:" + " " + str(bmi) + ", " + "you're: Severely Underweight"
        elif bmi < 18.5:
                return  "Your BMI is:" + " " + str(bmi) + ", " + "you're: Underweight"
        elif bmi < 25:
                return  "Your BMI is:" + " " + str(bmi) + ", " + "you're: Normal"
        elif bmi < 30:
                return  "Your BMI is:" + " " + str(bmi) + ", " + "you're: Overweight"
        else:
                return  "Your BMI is:" + " " + str(bmi) + ", " + "you're: Obese"

if __name__ == '__main__':
    app.run(debug=True)
