from flask import Flask,render_template,request
import json

app = Flask(__name__)

@app.route('/authenticate_user',methods=["GET","POST"])
def authenticate_user():
    fname = request.form('fname')
    lname = request.form('lname')
    full_name = fname + lname
    import pdb;pdb.set_trace()
    return render_template('test.html',name = full_name)

if __name__=='__main__':
    app.run(port=5500,debug=True)
