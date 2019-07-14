from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '6127f1ba5f868bdb1bf50b7d63531766'

posts = [
		{
			'author':'Saravanan',
			'title':'Blog Post 1',
			'content':'This is my new blog',
			'date':'July'
		},
		{
			'author':'Manoharan',
			'title':'Blog Post 2',
			'content':'This is my blog post 2',
			'date':'Aug'
		}
	]

@app.route("/")
def home():
    return render_template('home.html',posts = posts,title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html',title = "About")

@app.route("/register", methods = ['GET','POST'])
def register():
 form = RegistrationForm()
 if form.validate_on_submit():
	 flash(f'Account created succesfully for {form.username.data}','success')
	 return redirect(url_for('home'))
 return render_template('register.html',title = 'Register',form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
 form = LoginForm()
 if form.validate_on_submit():
	 if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
	 	flash(f'You have been logged in!','success')
	 	return redirect(url_for('home'))
	 else:
 		flash(f'Login unsuccessful. Please check in username or password','danger')
 return render_template('login.html',title = "Login",form=form)

if __name__ == "__main__":
    app.run(debug=True)
