from flask import Flask,render_template

myapp=Flask(__name__)

@myapp.route("/")

def index():
    return render_template("templ.html")

if    __name__ == "__main__":
    myapp.run(debug=True)
