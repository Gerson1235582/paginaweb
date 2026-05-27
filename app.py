from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
app = Flask(__name__)
app.secret_key = 'clave_secreta_exclusiva_xstore'
USUARIO_CORRECTO = "gersiton123"
PASSWORD_CORRECTO = "petoto1126"

@app.route('/')
def tienda():
    if 'usuario' in session and session['usuario'] == USUARIO_CORRECTO:
        return render_template('tienda.html')
    return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'intentos' not in session:
        session['intentos'] = 0

    restantes = 3 - session['intentos']
    if session['intentos'] >= 3:
        return redirect(url_for('bloqueado'))
    error = None
    if request.method == 'POST':
        usuario = request.form['username']
        password = request.form['password']
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
            session['usuario'] = usuario
            session['intentos'] = 0  
            return redirect(url_for('tienda'))
        else:
            session['intentos'] += 1
            restantes = 3 - session['intentos']
        
            if session['intentos'] >= 3:
                return redirect(url_for('bloqueado'))
            else:
                error = f"Credenciales incorrectas."

    return render_template('login.html', error=error, restantes=restantes)
@app.route('/bloqueado')
def bloqueado():
    return render_template('bloqueado.html')
@app.route('/contacto')
def contacto():
    if 'usuario' in session and session['usuario'] == USUARIO_CORRECTO:
        return render_template('contacto.html')
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
@app.route("/css/login.css")
def login_css():
    return send_from_directory("css", "login.css")
@app.route("/css/tienda.css")
def tienda_css():
    return send_from_directory("css", "tienda.css")
@app.route("/css/contacto.css")
def contacto_css():
    return send_from_directory("css", "contacto.css")
@app.route("/css/bloqueado.css")
def bloqueado_css():
    return send_from_directory("css", "bloqueado.css")
@app.route("/img/br3.jpg")
def img1():
    return send_from_directory("", "img/br3.jpg")
@app.route("/img/ds2.jpg")
def img2():
    return send_from_directory("", "img/ds2.jpg")
@app.route("/img/l2d4.jpg")
def img3():
    return send_from_directory("", "img/l2d4.jpg")
@app.route("/img/rdr2.jpg")
def img4():
    return send_from_directory("", "img/rdr2.jpg")
@app.route("/img/re7.jpg")
def img5():
    return send_from_directory("", "img/re7.jpg")
@app.route("/img/sl.jpg")
def img6():
    return send_from_directory("", "img/sl.jpg")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)