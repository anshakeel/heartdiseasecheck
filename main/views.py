from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,cross_val_score
# Create your views here.
def home(request):

    return render(request,"main.html")
def result(request):
    plist = []

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        sex = request.POST.get('sex')
        cp = request.POST.get('cp')
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST.get('restecg')
        thalach = request.POST['thalach']
        exang = request.POST.get('exang')
        oldpeak = request.POST['oldpeak']
        slope = request.POST.get('slope')
        ca = request.POST['ca']
        thal = request.POST['thal']
        print(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        plist = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print(plist)
        resoponse =predict(plist)
        print(resoponse)
        # if resoponse == 1:
        #     message1 = "YES"
        return render(request,"result.html", {"res" : resoponse[0], "name": name})

    return render(request,"main.html")
def predict(pred):
    df = pd.read_csv("heart-disease.csv")
    X = df.drop("target", axis=1)
    Y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    elf = LogisticRegression(C=0.20433597178569418,
                             solver="liblinear"
                             )

    elf.fit(X_train, y_train)
    res=elf.predict([pred])
    return res

