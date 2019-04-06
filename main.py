from flask import Flask, abort, render_template, send_file
app = Flask(__name__)

@app.route("/index")
def index():
    return '<h1>Hello World!</h1>'
app.add_url_rule('/', 'index', index)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)