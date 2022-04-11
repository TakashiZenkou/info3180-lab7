
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Regexp, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Images only!')])
    description = TextAreaField("Description", validators=[InputRequired(),Length(max=255,message=("Exceeded character count (255)"))])