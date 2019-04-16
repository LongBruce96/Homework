from flask import Flask

app = Flask(__name__)
@app.route('/user/<username>')

def index(username):
  Users = {
  "huy":    {
            "name" : "Nguyen Quang Huy",
            "age" : 29
            },
  "tuananh":{
            "name" : "Huynh Tuan Anh",
            "age" : 22
            },
  "long":   {
            "name" : "Nguyen Viet Long",
            "age" : 23
            }
}
  if username in Users:
    a = Users[username]
    for k,v in a.items():
      return k+":", v
  else:
    return "User's name not found"

if __name__ == '__main__':
  app.run(debug=True)