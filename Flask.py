from flask import Flask, request
app = Flask(__name__)

@app.route("/123")
def hello():
    return "Hello World!"

@app.route("/postmethod", methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    print(jsdata)

if __name__ == "__main__":
    app.run(debug=True)

