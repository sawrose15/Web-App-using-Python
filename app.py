# from flask import Flask,render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     headline = "Hello World!"
#     return render_template("index.html", headline=headline)

# @app.route('/bye')
# def bye():
#     headline = "Goodbye!"
#     return render_template("index.html", headline=headline)


# if __name__ == '__main__':
#     app.run(debug= True)


import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    return render_template('new_year_index.html',new_year = new_year)