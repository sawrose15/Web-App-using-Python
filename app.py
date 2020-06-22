
#Use of headline in Flask to show data
# from flask import Flask,render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     headline = "Hello World!"
#     return render_template("head_index.html", headline=headline)

# @app.route('/bye')
# def bye():
#     headline = "Goodbye!"
#     return render_template("head_index.html", headline=headline)


# if __name__ == '__main__':
#     app.run(debug= True)



##New Year using conditional Functions
# import datetime

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     now = datetime.datetime.now()
#     new_year = now.month == 1 and now.day == 1
#     return render_template('new_year_index.html',new_year = new_year)


# use Looping 
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     names = ["ALice", "John", "Carlie"]
#     return render_template("loop_index.html", names=names)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/more')
# def more():
#     return render_template("more.html")



#New App Development
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEM_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return 'BlogPost ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')
