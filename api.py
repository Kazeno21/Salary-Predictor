from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def makecalc():
    j_data = request.get_json()
    print(j_data)
    gender = 0
    sscp = j_data['sscp']
    sscb = 0
    hscp = j_data['hscp']
    hscb = 0
    hscs = 0
    ugp = j_data['ugp']
    ugt = 0
    workex = 0
    etest = j_data['etest']
    spec = 0
    mbap = j_data['mbap']
    if(j_data['gender']) == 'Male':
        gender = 1
    if(j_data['sscb']) == 'Others':
        sscb = 1
    if(j_data['hscb']) == 'Others':
        hscb = 1
    if(j_data['hscs']) == 'Science':
        hscs = 2
    if(j_data['hscs']) == 'Commerce':
        hscs = 1
    if(j_data['ugt']) == 'Science & Tech':
        ugt = 2
    if(j_data['ugt']) == 'Others':
        ugt = 1
    if(j_data['workex']) == 'Yes':
        workex = 1
    if(j_data['spec']) == 'Marketing & HR':
        spec = 1

    details = [gender, sscp, sscb, hscp, hscb, hscs,
               ugp, ugt, workex, etest, spec, mbap]
    print(details)
    prediction = model.predict(np.asanyarray([details]))
    prediction /= 12
    print(prediction)
    return jsonify({'prediction': str(prediction)})


@app.route('/job', methods=['POST'])
def makepredic():
    j_data = request.get_json()
    jobdescription = j_data['JobDescription']

    jobdescription = [jobdescription]
    prediction = model1.predict(vec.transform(jobdescription))

    salary = j_data['salary']

    if float(salary) >= float(prediction):
        return jsonify({'placed': 'Placed', "salary": str(salary), "predicted": str(prediction)})
    else:
        return jsonify({'placed': 'Not Placed', "salary": str(salary), "predicted": str(prediction)})


if __name__ == '__main__':
    modelfile = 'xgbrpredict.pickle'
    model = p.load(open(modelfile, 'rb'))
    modelfile1 = 'model.pickle'
    model1 = p.load(open(modelfile1, 'rb'))
    vecfile = 'vec.pickle'
    vec = p.load(open(vecfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
