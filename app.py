from flask import Flask
from flask import request  # For Input

app = Flask(__name__)

# 1. Home Page
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# 2. Extra Routes 
@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

# 3. Logic Test (Calculation)
@app.route("/test")
def test():
    a = 5+6
    return "this is my function to run app {}".format(a)

# 4. Input Test (Taking Data From URL)
@app.route("/test2/test2")
def test2():
    data = request.args.get('x') 
    return "this is a data input form my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")