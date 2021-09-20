from flask import Flask, request, jsonify,redirect,url_for
import funciones.paginas as page
app = Flask(__name__)

@app.route("/")
def main():
    data = {}
    res = page.returnPaginas('index',data)
    return res

@app.route("/form",methods=['GET','POST'])#PUT,DELETE
def form():
    if request.method == 'POST':
        # return redirect(url_for('main'))
        return jsonify(request.form)
        # request.args
    else:
        data = {}
        res = page.returnPaginas('form',data)
        return res

@app.route("/hola")
def hola():
    return "Hola Grupo desde insopnia"
    
# comandos para trabajar en desarrollo
# export FLASK_ENV=development
# flask run

