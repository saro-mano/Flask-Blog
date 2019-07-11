from flask import Flask, render_template
app = Flask(__name__)

posts = [
		{
			'author':'Saravanan',
			'title':'Blog Post 1',
			'content':'This is my new blog',
			'date':'July'
		}
	]

@app.route("/")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
