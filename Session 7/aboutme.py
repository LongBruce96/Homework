from flask import Flask, redirect

app = Flask(__name__)
@app.route('/aboutme')
def about_me():
    return """
    <html>
    <h1>Long (Bruce) Nguyen Viet</h1>
    <img width ="360" height="360" src='https://scontent.fhan2-1.fna.fbcdn.net/v/t1.0-9/52013981_1880000785442360_256671716669915136_n.jpg?_nc_cat=102&_nc_oc=AQlKU_XxzVN_btZjY3tgbOlA9CtL-VvapBe9uWpTZaBjvGouYbRgnWlgHdU7sp0xBSo&_nc_ht=scontent.fhan2-1.fna&oh=1fc06e0bd165ea075fb94ce469f9bb46&oe=5D34D79E'>
    </br>
    <p><strong>A member or <a href='http://techkids.vn '>Mindx</a></strong></p>
    <div style = 'width: 360px'>
    <p style = 'text-align: justify'>Hi, my name is Long. I'm 23 years old and I'm working at Foxconn Vietnam. In my free time, I often access Youtube to watch videos or sometimes, I go out with friends. I have many crushes but none of them become my lover :((<p>
    </div>
    <p><strong>Thank you for reading!</p>
    """


@app.route('/school')

def link():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)