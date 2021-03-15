from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import request

class single_reads(FlaskForm):
    file1 = FileField(validators=[FileRequired(), FileAllowed(['fasta'], 'Fasta files only')])
    
class pairend_reads(FlaskForm):
    file1 = FileField(validators=[FileRequired(), FileAllowed(['fasta'], 'Fasta files only!')])
    file2 = FileField(validators=[FileRequired(), FileAllowed(['fasta'], 'Fasta files only!')])