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
    
@app.route("/registro")
def acercade():
    return render_template("registro.html")

@app.route("/registrame", methods=("GET", "POST"))
def registrame():
    error = None
    if request.method == "POST":

        nombre= request.form["nombre"]
        Apellido = request.form["apellido"]
        genero = request.form["genero"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        confirmContraseña = request.form["confirmContraseña"]
        

if __name__ == "__main__":
    app.run(debug=True)

