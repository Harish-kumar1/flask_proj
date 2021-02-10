#importing necessary packages
from flask import Flask, render_template, url_for, flash

#importing item_values class from the user-defined module entry_values
from entry_values import item_values

#creating an instance for Flask
app = Flask(__name__)


'''
creation of csrf token to facilitate valid client request and to reject the request if the token is invalid or missing

'''
app.config["SECRET_KEY"] = 'bbc13112232fa4c77becbd0d799e40d5'

#assigning url to the app instance

'''

since a redirect url is not specified in html forms GET and POST has been provided as methods to methods argument, so that this page can receive and send requests avoiding POST error 405

'''
@app.route("/", methods = ['GET', 'POST']) 
def hello_world():
    #creating an instance for the class item_values                         
    form = item_values()
    
    return render_template('index.html', form = form)

