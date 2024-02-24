from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/welcome")
def welcome():
    return "<h1>Welcome to ABC Corporation</h1>"

@app.route("/")
def company_details():
    company_name = "ABC Corporation"
    location = "India"
    contact_detail = "999-999-9999"
    return f"""
    <h3>Company Name: {company_name}<br>
    Location: {location}<br>
    Contact Detail: {contact_detail}</h3>
    """

@app.route("/test")
##to run this url https://green-butcher-ultsx.pwskills.app:5000/test?x=datascience
def test():
    data =  request.args.get('x')
    return "This is data input from my url {}".format(data)   


@app.route("/test1")
def test1():
    a = 4+9
    return "This is my function to run app {}".format(a)   

if __name__=="__main__":
    app.run(host="0.0.0.0")
