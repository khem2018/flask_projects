from flask import Flask,render_template,request
import json

app = Flask(__name__)

@app.route('/authenticate_user',methods=["POST"])
def authenticate_user():
    fname = request.get('fname')
    lname = request.get('lname')
    full_name = fname + lname
    return render_template('test.html',name = full_name)

if __name__=='__main__':
    app.run(host ='0.0.0.0',port='4000',debug=True)
