from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
app = Flask(__name__)

app.config['SECRET_KEY'] = 'myflaskproject'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sairam1994@localhost/CRUD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

        db.create_all()

@app.route('/')
def index():

    all_data = Data.query.all()

    return render_template('index.html', all_data = all_data)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)

        db.session.add(my_data)
        db.session.commit()

        flash(f'Employee {name} details inserted Successfuly!')
        return redirect(url_for('index'))

@app.route('/update', methods = ['GET','POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']


        db.session.commit()
        flash("Employee Details Updated Successfuly!")

        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET','POST'])
def delete(id):

    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.create_all()
    db.session.commit()
    flash("Employee Details Deleted Successfuly!")

    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
