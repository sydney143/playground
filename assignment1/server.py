from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template("index.html")

@app.route("/play/(x)")
def playx():
    return render_template("index2.html")

@app.route("/play/(x)/(color)")
def playcolor():
    return render_template("index3.html")

if __name__=="__main__":
    app.run(debug=True)