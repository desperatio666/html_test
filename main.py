#sample-test

from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route("/")
def bla():
    return "<h3>Greetings, fuckface! You have just lost the game.</h3>"

@app.route('/sum/')
def sum():
    return render_template('sum.html')

@app.route('/sum/result')
def sum_res():
        x = request.args.get('x', type=int)
        y = request.args.get('y', type=int)

        return render_template('result.html', result=x+y)

app.run(debug=True)