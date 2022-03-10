from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddSaleForm(FlaskForm):
    emp_id = StringField('Employee id')
    item_code = StringField('Choose the product')
    sale_week = IntegerField('Week of the year')
    sale_year = IntegerField('Enter the year')
    quantity = IntegerField('Quantity of sale')
    submit = SubmitField('add sale')

class DelForm(FlaskForm):
    hist_data_id = IntegerField('Enter id of sale to remove: ')
    submit = SubmitField('Remove sale')
