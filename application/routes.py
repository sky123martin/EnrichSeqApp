from __future__ import print_function
from application import app

from flask import Flask, render_template, flash, request, redirect, session
import flask
# from application.forms import pairend_reads, single_reads
from application.utility import *
import subprocess
import pandas as pd 
import numpy as np 
import random
import sys
import math
import json

from application import utility

@app.route('/', methods=['GET', 'POST'])
def home(error = ""):
    return render_template("home.html")

@app.route('/EnrichSeq', methods=['GET', 'POST'])
def EnrichSeq(error = ""):
    if flask.request.method == "POST":
        process_id = str(random.randint(0,sys.maxsize))
        files = flask.request.files.getlist("file[]")
        proc = subprocess.check_call("mkdir -p {}/{}".format(app.config['UPLOAD_FOLDER'], process_id), shell=True)
        file_names = []
        for file in files:
            file.save(os.path.join("{}/{}".format(app.config['UPLOAD_FOLDER'], process_id), file.filename)) #app.config['UPLOAD_FOLDER']+"/+"+str(ID)
            file_names.append(file.filename)
        
        print(file_names)

    

        # delete input file once they are handled
        proc = subprocess.check_call("rm -R {}/{}".format(app.config['UPLOAD_FOLDER'], process_id), shell=True)
        

    return render_template("EnrichSeq.html")
