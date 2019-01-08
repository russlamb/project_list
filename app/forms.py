from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, length


class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired(), length(max=50)])
    description = TextAreaField('Project Description', validators=[DataRequired(), length(max=500)])
    is_live = BooleanField("Is It Live?")
    submit = SubmitField("Submit")

class DeleteProjectForm(FlaskForm):
    delete = SubmitField("Delete")