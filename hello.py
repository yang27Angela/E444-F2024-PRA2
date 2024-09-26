from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired,ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my pwd'

bootstrap = Bootstrap(app)
moment = Moment(app)

#def validateEmail(form,field):
#    if '@' not in field.data: 
#        raise ValidationError(f'Please include an \'@\' in the email address. \'{field.data}\' is missing a \'@\'')
#    elif 'utoronto' not in field.data: 
#        raise ValidationError(f'Please use UofT email. \'{field.data}\' is missing \'utoronto\'')

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        
        old_email=session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data


        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))
