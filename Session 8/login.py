from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

acc=[{
  'username':'long',
  'password': 'long96'
},
{
  'username':'quang',
  'password': 'quang96'
},
{
  'username':'hoa',
  'password': 'hoa89'
},
{
  'username':'khanh',
  'password': 'khanh98'
}]
  
@app.route('/')
def index():
    return render_template('login.html', acc=acc)

@app.route('/', methods=['POST'])
def check():
    new_dict={}
    a = request.form.get('ten')
    b = request.form.get('mat_khau')
    new_dict['username'] = a
    new_dict['password'] = b
    if new_dict in acc:
        return """
        <h1> Login Successull!</h1>
        """
    else:
        return """
        <h1> Login Failed! </h1>
        """

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
