from flask import Flask, render_template
from database import DB

app = Flask(__name__, template_folder="templates", static_folder="static")
db = DB()

@app.route("/students")
def students():
    return db.run_query("SELECT * FROM students")

@app.route("/")
def hello():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)