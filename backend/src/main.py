#!/usr/bin/env python3

import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename


import sys
import json
from excel_file import ExcelFile
from save_excel import SaveExcel

UPLOAD_FOLDER = '/tmp/excel-to-mongo'
ALLOWED_EXTENSIONS = {'xlsx'}


def save_file_xls(file_name):
    #file_name = sys.argv[1]
    excel = ExcelFile(file_name)
    exceldb = SaveExcel(excel_file=excel)
    exceldb.save()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/save', methods=['POST'])
def save_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        print(request.files)
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path_name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path_name)
        save_file_xls(path_name)
        return json.dumps(dict(msg="File Saved"))
    

@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ == "__main__":
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    # session.init_app(app)

    app.debug = True
    app.run(host='0.0.0.0', port=8080)