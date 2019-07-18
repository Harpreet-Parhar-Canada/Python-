from flask import Flask, request,render_template,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/load",methods=['GET'])
def files():
    import pandas as pd
    wb = pd.ExcelFile('Invoice-Example.xls')
    sheets = pd.read_excel('Invoice-Example.xls', sheet_name=wb.sheet_names)
    print(sheets['Clients'])
    return render_template("load.html",client=sheets['Clients'])


@app.route('/clients')
def clients():
    import pandas as pd
    sheets = []
    jsonfileconver = []
    wb = pd.ExcelFile('Invoice-Example.xls')
    sheets = pd.read_excel('Invoice-Example.xls', sheet_name=wb.sheet_names, encoding='utf-8')
    for i in wb.sheet_names:
        jsonfileconver.append(sheets[i].to_json(orient='records'))
    return jsonfileconver[0]
@app.route('/inventory/')
def inventory(invoice=None):
    import pandas as pd
    sheets = []
    jsonfileconver = []
    wb = pd.ExcelFile('Invoice-Example.xls')
    sheets = pd.read_excel('Invoice-Example.xls', sheet_name=wb.sheet_names, encoding='utf-8')
    for i in wb.sheet_names:
        jsonfileconver.append(sheets[i].to_json(orient='records'))
    return jsonfileconver[1]



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
