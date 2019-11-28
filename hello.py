from flask import Flask, request, jsonify, render_template
from joblib import dump, load
import numpy as np
import json
import os
from builtins import print
app = Flask(__name__)

knn = load('knn.pkl')

@app.route('/')
def hello_world():
    print('hi')
    return '<h1>Hello, my very best friend!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % (username)

@app.route('/iris/<param>')
def iris(param):

    param = param.split(',')
    param = [float(num) for num in param]
    param = np.array(param).reshape(1, -1)
    predict = knn.predict(param)
    return str(predict)

# @app.route('/iris_post', methods=['POST'])
# def add_message():
#     content = request.json
#     # print(str(content))
#     # ast.literal_eval(json.loads(request.data)['flower'])
#     content = json.loads(request.data)['flower']
#     print(str(content))
#     # a = 10
#     # return str(a)
#     # print(content)
#     # content = {'flower': '1,2,3,7'}
#     # param = content['flower'].split(',')
#     # param = [float(num) for num in param]
#     # param = np.array(param).reshape(1, -1)
#     # predict = knn.predict(param).tolist()
#     # return jsonify(predict)

from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired 
from werkzeug.utils import secure_filename

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField()

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():

        f = form.file.data
        filename = 'other.txt'
        f.save(os.path.join(
            filename
        ))

        return str(form.name)
    return render_template('submit.html', form=form)
