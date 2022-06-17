import boto3
from flask import Flask, render_template, request
from pymysql import connections

from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

# db_conn = connections.Connection(
#     host=customhost,
#     port=3306,
#     user=customuser,
#     password=custompass,
#     db=customdb
#
# )
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

    # insert_sql = "INSERT INTO expenditure VALUES (%s, %s, %s, %s, %s)"
    # cursor = db_conn.cursor()
    #
    # if emp_image_file.filename == "":
    #     return "Please select a file"
    #
    # try:
    #
    #     cursor.execute(insert_sql, (main_category, sub_category, amount))
    #     db_conn.commit()
    #     emp_name = "" + main_category + " " + main_category + " " + str(amount)
    #     # Upload image file in S3 #
    #     exp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
    #     s3 = boto3.resource('s3')
    #
    #     try:
    #         print("Data inserted in MySQL RDS... uploading image to S3...")
    #         s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)
    #         bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
    #         s3_location = (bucket_location['LocationConstraint'])
    #
    #         if s3_location is None:
    #             s3_location = ''
    #         else:
    #             s3_location = '-' + s3_location
    #
    #         object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
    #             s3_location,
    #             custombucket,
    #             emp_image_file_name_in_s3)
    #
    #     except Exception as e:
    #         return str(e)
    #
    # finally:
    #     cursor.close()
    print("date: ", date, "Category: ", main_category, "Sub-category: ", sub_category, "Expenditure: ", amount, "euros")
    return render_template('getAddedExpenditure.html')


if __name__ == '__main__':
    app.run(debug=True)
