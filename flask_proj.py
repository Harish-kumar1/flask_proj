from flask import Flask, render_template, url_for, flash
from entry_values import item_values

app = Flask(__name__)

app.config["SECRET_KEY"] = 'bbc13112232fa4c77becbd0d799e40d5'

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    form = item_values()
    
    return render_template('index.html', form = form)
 

if __name__ == '__main__':
 app.run(debug = True)

