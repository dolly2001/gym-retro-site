from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/gym')
def gym():
    return render_template("gym.html")

@app.route('/athletes')
def athletes():
    return render_template("athletes.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)