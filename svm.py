from __future__ import print_function

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
    # print(df)
    df = sklearn.utils.shuffle(df)
    # print(df)
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
    # 1 = male, 0 = female
    '''scaler'''
    print(X.shape)
    X = X.append(td)
    print(X.shape)
    print(td)
    print(X[-1:])
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    print(td)
    td = X[-1:]
    print(td)
    X=X[:-1]
    print(td)
    print(X.shape)
    '''------------'''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
    svc = SVC()  # Default hyperparameters
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    print('Accuracy Score:')
    print(metrics.accuracy_score(y_test, y_pred))
    # print(y_pred)

    print(td)
    print(td.shape)
    '''---------------'''

    # td = scaler.transform(td)
    td_pred = svc.predict(td)

    return int(td_pred[0])
if __name__ =="__main__":

    subprocess.getoutput("test.bat")
    o = voice_SVM()
    print(type(o))
    if  o > 0 :
        print("你是男森 !")
    else:
        print("你是女森 !")
    # print("Out_put = ",voice_SVM())
    subprocess.getoutput("del Output.csv")
