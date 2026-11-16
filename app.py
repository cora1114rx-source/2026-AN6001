#web app
from flask import Flask,render_template,request
import joblib

model  = joblib.load("dbs.pkl")

app = Flask(__name__)

@app.route("/",methods=["Get","Post"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["Get","Post"])
def main():
    q = request.form.get("q")
    return(render_template("main.html"))

@app.route("/dbs",methods=["Get","Post"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/dbsResult",methods=["Get","Post"])
def dbsResult():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    return(render_template("dbsResult.html",r=r[0][0]))

if __name__ == "__main__":
    app.run()