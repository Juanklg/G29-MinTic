from flask import Flask, render_template
import funciones as fn
# import dev as fn
fn.isLogin("Login")
## solo se ejecuta esto si el usuario es = 'Login'
print("Inicia la App".center(50,'-'))
#-----------------------------------------------------------------
app = Flask(__name__)
# inicia servicios-------------------------------------------------------------
@app.route("/")
def hello_world():
    return "<p>Hola Grupo 29</p>"

@app.route("/index")
def index():
    return render_template("index.html")
# terminan servicios----------------------------------------------------------------
print("Esto es la dunder name = ",__name__)
if __name__=="__main__":
    app.run(debug=True)    