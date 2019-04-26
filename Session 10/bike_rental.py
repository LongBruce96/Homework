#1

from flask import Flask, render_template, request, url_for
from bike_db import all_bikes, add_bike

app = Flask(__name__)

@app.route('/new_bike')
def get_bike_rental():
    return render_template('bike_rental.html', data = all_bikes())


@app.route('/new_bike',methods = ['POST'])
def post_bike_rental():
    bike_model = request.form.get('model')
    bike_price = request.form.get('price')
    bike_image = request.form.get('image_url')
    bike_year = request.form.get('year')
    add_bike(bike_model, bike_price, bike_image, bike_year)

    return render_template('bike_rental.html', data = all_bikes())
    

if __name__ == '__main__':
    app.run(host ='127.0.0.1', port=8000, debug=True)
 