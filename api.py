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
    status = 0
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
        hscs = 2
    if(j_data['ugt']) == 'Others':
        hscs = 1
    if(j_data['workex']) == 'Yes':
        workex = 1
    if(j_data['spec']) == 'Marketing & HR':
        spec = 1
    if(j_data['status']) == 'Placed':
        status = 1

    details = [gender, sscp, sscb, hscp, hscb, hscs,
               ugp, ugt, workex, etest, spec, mbap, status]
    print(details)
    prediction = model.predict(np.asanyarray([details]))
    print(prediction)
    return jsonify({'prediction': str(prediction)})


if __name__ == '__main__':
    modelfile = 'xgbrpredict.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
