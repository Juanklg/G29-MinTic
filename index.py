from flask import Flask, render_template
# import funciones as fn
import dev as fn
fn.isLogin("Login")
## solo se ejecuta esto si el usuario es = 'Login'
print("Inicia la App".center(50,'-'))
#-----------------------------------------------------------------
app = Flask(__name__)
# inicia servicios-------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proy")
def proyJuan():
    cte=fn.consultarConstantes()
    print('Ejecutando este evento'.center(50,'-'))
    redes = fn.consultarRedes()
    print(type(redes))
    # return render_template("index.html")
    return render_template("index.html",usuario='Wendy',proyecto='proyecto palabras',data=redes,cte=cte)

@app.route("/proy/<usuario>")
def proy(usuario):
    proyecto = fn.consultarProyecto(usuario)
    print('Ejecutando este evento'.center(50,'-'))
    return render_template("index.html",usuario=usuario,proyecto=proyecto)

@app.route("/doc")
def doc():
    print('Ejecutando el doc'.center(50,'-'))
    return render_template("doc/scripts.html")
# terminan servicios----------------------------------------------------------------
print("Esto es la dunder name = ",__name__)
if __name__=="__main__":
    app.run(debug=True)