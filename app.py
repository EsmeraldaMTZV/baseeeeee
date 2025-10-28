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
def registro():
    return render_template("registro.html")

@app.route("/login" , methods=("POST"))
def login():
    if session.get('logueado')==True:
        session.clear()
    return render_template('login.html')

@app.route('/validaLogin', methods=['POST'])
def validaLogin():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    if not email or not password:
        flash ('Por favor, ingresa email y contraseña.', 'error')
    elif email in USUARIOS_REGISTRADOS:
        usuario = USUARIOS_REGISTRADOS[email]
        if usuario['password'] == password:
            session ['usuario_email'] = email 
            session ['usuario'] = usuario['nombre']
            session ['logueado'] = True
            flash(f'¡Bienvenido, {usuario["nombre"]}!', 'success')
            return redirect(url_for('inicio'))
        else:
            flash ('Contraseña incorrecta.', 'error')
    else:
        flash('El correo no está registrado.', 'error')
    return redirect(url_for('login'))
    
@app.route('/cerrarSesion', methods=['POST'])
def cerrar():

@app.route("/registtro", methods= ("POST"))
def sesion():
    error = None
    if request.method == "POST":
        nombre= request.form["nombre"]
        Apellido = request.form["apellido"]
        genero = request.form["genero"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        confirmContraseña = request.form.get["confirmContraseña"]

        if contraseña != confirmContraseña:
            error= "La Contraseña no Coincide"
            
        if error != None:
            flash(error)
            return render_template("registro.html" , request.form)
        else:
            flash(f"¡Registro de usuario: {nombre, Apellido}")
            return render_template ("login.html")
        
    return

if __name__ == "__main__":
    app.run(debug=True)

