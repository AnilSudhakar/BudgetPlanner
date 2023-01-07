import os
import boto3
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pymysql import connections

from config import *

UPLOAD_FOLDER = '/home/anilkaiyambally/Uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bucket = custombucket
region = customregion

output = {}
table = 'expenditure'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('addExpenditure.html')


@app.route("/addexpenditure", methods=['POST'])
def addExpenditure():
    date = request.form['date']
    main_category = request.form['main_category']
    sub_category = request.form['sub_category']
    amount = request.form['amount']
    receipt_path = None
    if request.method == 'POST':
        receipt = request.files['formFile']
        if receipt and allowed_file(receipt.filename):
            filename = secure_filename(receipt.filename)
            #receipt.save(UPLOAD_FOLDER + filename)
            receipt_path = UPLOAD_FOLDER + filename

    print("date: ", date, "Category: ", main_category, "Sub-category: ", sub_category, "Expenditure: ", amount, "euros")
    return render_template('getAddedExpenditure.html', date=date, category=main_category, sub_category=sub_category,
                           amount=amount, filename=receipt_path)


if __name__ == '__main__':
    app.run(debug=True)
