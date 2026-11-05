from flask import Flask, render_template
import datetime
app=Flask(__name__)
@app.route("/")
def bonjour():
    return render_template("index.html")
@app.route("/heure")
def heure():
    date_heur= datetime.datetime.now()
    h=date_heur.hour
    m=date_heur.min
    s=date_heur.sec
    print(h,m,s)
    return "heure actuelle"
if __name__=="__main__":
    app.run(debug=True)
