#!/usr/bin/env python3

import os
from flask import Flask, flash, request, redirect, url_for, session
from flask_cors import CORS
from werkzeug.utils import secure_filename
from bson import json_util


import sys
import json
from excel_file import ExcelFile
from save_excel import SaveExcel
from lookup_excel import LookupExcel

from consts import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

def save_file_xls(file_name):
    #file_name = sys.argv[1]
    excel = ExcelFile(file_name)
    exceldb = SaveExcel(excel_file=excel)
    exceldb.save()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/search', methods=['GET'])
def search_document():
    text = request.args.get('text', None)
    lookup = LookupExcel()
    result = lookup.lookup(text)
    return json.dumps(result, indent=4, default=json_util.default)

@app.route('/search/line', methods=['GET'])
def search_document_line():
    text = request.args.get('text', None)
    lookup = LookupExcel()
    result = lookup.lookup_line(text)
    return json.dumps(result, indent=4, default=json_util.default)

@app.route('/save', methods=['POST'])
def save_file():
    if 'file' not in request.files:
        flash('No file part')
        print(request.files)
        return redirect(request.url)
    file = request.files['file']
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
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run(host='0.0.0.0', port=8080)