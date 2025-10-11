from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/vehiculos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/maravillass")
def maravillass():
    return render_template("maravillass.html")


@app.route("/acercade")
def acercade():
    return render_template("acercade.html")

if __name__ == "__main__":
    app.run(debug=True)

