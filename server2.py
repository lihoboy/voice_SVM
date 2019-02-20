from __future__ import print_function
import time
from flask_uploads import UploadSet, IMAGES, AUDIO, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template, jsonify
from flask_cors import CORS
import os
# d: \anaconda3\python.exe | d: \anaconda3\lib\site-packages\wfastcgi.py


import pandas as pd
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
import sys, os
import subprocess
import shlex
import sklearn

def voice_SVM():
    print("start svm")
    df = pd.read_csv("voice.csv")
    df = sklearn.utils.shuffle(df)
    clf = svm.SVC(gamma='scale')

    '''Read testdata'''
    td = pd.read_csv("Output.csv")
    cols = [0, 1, 2, 3, 16]
    td.drop(td.columns[cols], axis=1, inplace=True)

    '''Split X y'''
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    gender_encoder = LabelEncoder()
    y = gender_encoder.fit_transform(y)

    '''scaler'''
    X = X.append(td)
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    td = X[-1:]
    X=X[:-1]

    '''------------'''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
    svc = SVC()  # Default hyperparameters
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    '''---------------'''
    # td = scaler.transform(td)
    td_pred = svc.predict(td)

    return int(td_pred[0])
app = Flask(__name__, static_url_path = "", static_folder = "static",template_folder="templates")
CORS(app)
app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
print(app.config['UPLOADED_PHOTO_DEST'])
app.config['UPLOADED_PHOTO_ALLOW'] = AUDIO

# @app.route('/')
# def index():
#     # return "hellow"
#     return render_template("index.html")
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    print('hii')
    wav = request.files['file']
    wav.save('user_voice.wav')
    time.sleep(1)
    subprocess.getoutput("test.bat")
    o = voice_SVM()
    print(type(o))
    str = ''
    if o > 0:
        print("你是男森 !")
        str = "你是男森 !"
    else:
        print("你是女森 !")
        str = "你是女森 !"

    # print("Out_put = ",voice_SVM())
    subprocess.getoutput("del Output.csv")
    subprocess.getoutput("del user_voice.wav")




    return str

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
