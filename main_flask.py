from flask import Flask, render_template, request, session, redirect, url_for, g
#from flask_sqlalchemy import SQLAlchemy
#import dao_user, dao_task, models, model_todo
import dao_user, dao_task, model_todo, models
#from models import db

app = Flask(__name__)
app.secret_key = 'qAz90CoNuSuvivaf8PkebdDFFRg9q9+8NYvzdObZBUU='
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pirple@localhost/flask_pirple'
#sdb = SQLAlchemy(app)
models.db.init_app(app)

@app.before_request
def before_first_request():
    g.userid = None
    g.username = None
    if 'userid' and 'username' in session:
        g.userid = session['userid']
        g.username = session['username']

@app.route('/', methods=['GET'])
def home():
    if 'userid' and 'username' in session:
        g.userid = session['userid']
        g.username = session['username']
        message = 'Login successful! Welcome ' + g.username
        return render_template('dashboard.html', message = message)

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    #if (request.method == 'POST'):
        session.pop('userid', None)
        session.pop('username', None)
        email = request.form['email']
        password = request.form['pass']
        login = dao_user.check_pw(email, password)
        if login is not None:
            session['userid'] = login.id
            session['username'] = login.name
            return redirect(url_for('home'))
        else:
            error_message = 'Wrong password or email.'
            return render_template('index.html', message = error_message)
    #return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/signup', methods=['GET','POST'])
def sigunp():
    if (request.method == 'GET'):
        message = 'Please sign up!'
        return render_template('signup.html', message = message)
    else:
        user = models.Users()
        user.email = request.form['email']
        user.passwd = request.form['pass']
        user.name = request.form['name']
        user.address = request.form['address']
        

        message = dao_user.create_user(user)
        return render_template('index.html', message = message)

@app.route('/new_task', methods=['GET','POST'])
def new_task():
    if (request.method == 'GET'):
        return render_template('new_task.html')
    else:
        task = models.Todo()
        task.user_id = g.userid
        task.from_date = request.form['from_date']
        task.task = request.form['task']
        
        message = dao_task.create_task(task)

        return render_template('dashboard.html', message = message)

@app.route('/logout')
def logout():
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run( debug = True )
