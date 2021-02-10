from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

class item_values(FlaskForm):
 add_item = StringField('add_item', validators = [Length(min = 2, max = 30)])
