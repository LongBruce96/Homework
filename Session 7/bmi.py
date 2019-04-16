# from math import sqrt

# from flask import Flask, request

# app = Flask(__name__)
# @app.route('/bmi/<weight>/<height>')
# def index(weight, height):
#     # weight = request.args.get('weight', type=float)
#     # height = request.args.get('height', type=float)
#     bmi = int(weight / (height/100)**2)
    
#     if bmi < 16:
#         return "you're: Severely Underweight"
#     elif bmi < 18.5:
#         return "you're: Underweight"
#     elif bmi < 25:
#         return "you're: Normal"
#     elif bmis < 30:
#         return "you're: Overweight"
#     else:
#         return "you're: Obese"

# if __name__ == '__main__':
#   app.run(debug=True)

from math import sqrt

from flask import Flask, request

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def index(weight, height):
    # weight = request.args.get('weight', type=float)
    # height = request.args.get('height', type=float)
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