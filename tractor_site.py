import os
from forms import AddSaleForm,DelForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# SQL DATABASE SECTION #

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:1957Chevy22@localhost/tractor'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# MODELS #

class sale_data(db.Model):

    __tablename__ = 'hist_data'
    hist_data_id = db.Column(db.Integer,primary_key=True)
    emp_id = db.Column(db.Text)
    item_code = db.Column(db.Text)
    sale_week = db.Column(db.Integer)
    sale_year = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self,emp_id,item_code,sale_week,sale_year,quantity):
        
        self.emp_id = emp_id
        self.item_code = item_code
        self.sale_week = sale_week
        self.sale_year =sale_year
        self.quantity = quantity

    def __repr__(self):
            return f"{self.emp_id} sold {self.quantity} of {self.item_code} in week {self.sale_week} of {self.sale_year}"




# VIEW FUNCTIONS #
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_sale',methods=['GET','POST'])
def add_sale():

    form = AddSaleForm()

    if form.validate_on_submit():

        emp_id = form.emp_id.data
        item_code = form.item_code.data
        sale_week = form.sale_week.data
        sale_year = form.sale_year.data
        quantity = form.quantity.data

        new_sale = sale_data(emp_id,item_code,sale_week,sale_year,quantity)
        db.session.add(new_sale)
        db.session.commit()

        return redirect(url_for('list_sales'))

    return render_template('add_sale.html',form=form)


@app.route('/list')
def list_sales():

    sales = sale_data.query.all()
    return render_template('list_sales.html',sales=sales)

@app.route('/delete',methods=['GET','POST'])
def del_sale():

    form = DelForm()

    if form.validate_on_submit():

        hist_data_id = form.hist_data_id.data
        value = sale_data.query.get(id)
        db.session.delete(value)
        db.session.commit()

        return redirect(url_for('list_sales'))
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
