import os

class Config(object):
    # needed for CRSV which is used for forms
    SECRET_KEY = os.urandom(32) 
    UPLOAD_FOLDER = "uploads"