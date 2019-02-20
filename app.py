from flask import Flask,render_template, request
import config
import os
from werkzeug.wrappers import Request, Response
from werkzeug.utils import secure_filename


app = Flask(__name__ , static_url_path = "", static_folder = "static",template_folder="templates" )
app.config.from_object(config)
app.debug = True
@app.route('/')
def index():
    # return "hellow"
    return render_template("index.html")




if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0',port=5000,debug=True)#
