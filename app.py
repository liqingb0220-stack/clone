from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    r = request.form.get("q")
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/DbsPrediction", methods=["GET","POST"])
def DbsPrediction():
    q = float(request.form.get("q"))
    model = joblib.load('dbs.jl')
    r = model.predict([[q]])
    return(render_template("DbsPrediction.html",r=r[0][0]))

@app.route("/credit", methods=["GET","POST"])
def credit():
    return(render_template("credit.html"))

@app.route("/creditPrediction", methods=["GET","POST"])
def creditPrediction():
    q = float(request.form.get("q"))
    model = joblib.load("credit_model.pkl")
    r = model.predict([[q]])
    if r == 1:
        r = "Approved"
    else:
        r = "Not Approved"
    return(render_template("creditPrediction.html",r=r))
                           
if __name__ == "__main__":
    app.run()