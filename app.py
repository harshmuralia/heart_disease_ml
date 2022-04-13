from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__, template_folder='template')
model = pickle.load(open('heart_1.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':

        age = int(request.form['age'])
        sex = int(request.form['sex'])
        chest_pain = int(request.form['chest_pain'])
        blood_press = int(request.form['blood_press'])
        serum_chol = int(request.form['serum_chol'])
        blood_sugar = int(request.form['blood_sugar'])
        electrocard = int(request.form['electrocard'])
        max_heart_rate = int(request.form['max_heart_rate'])
        induced_ang = int(request.form['induced_ang'])
        oldpeak = float(request.form['oldpeak'])
        peak_st_seg = int(request.form['peak_st_seg'])
        major_ves = int(request.form['major_ves'])
        thal = int(request.form['thal'])

        prediction = model.predict([[age, sex, chest_pain, blood_press, serum_chol, blood_sugar,
                                   electrocard, max_heart_rate, induced_ang, oldpeak, peak_st_seg, major_ves, thal]])
        op1 = prediction[0]
        output = round(prediction[0])

        print(op1)
        
        if output == 1:
            return render_template('index.html', prediction_text="The Person does not have a Heart Disease")
        else:
            return render_template('index.html', prediction_text="The Person has Heart Disease")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
