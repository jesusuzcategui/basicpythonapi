import flask
from flask import request, jsonify
from db.conecct import getConection

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello world</h1>'


@app.route('/save', methods=['GET', 'POST'])
def saveCtrl():
    try:
        conx = getConection()
        with conx.cursor() as cursor:
            cursor.execute("INSERT INTO users (email, pasword) VALUES (%s, %s)",
                       ("uzcateguijesusdev@gmail.com", "12345"))
        conx.commit()
        conx.close()
        return jsonify({"message": "OK"})
    except:
        return jsonify({"message": "Error on query"}), 400


@app.route('/list', methods=['GET'])
def listContent():
    try:
        dataReturn = [];
        jsonToRetorno = [];
        conx = getConection()
        with conx.cursor() as cursor:
            cursor.execute("SELECT * from users")
            dataReturn = cursor.fetchmany()
        conx.close()
        for ele in dataReturn:
            jsonToRetorno.append({
                "id": ele[0],
                "email": ele[1],
                "clave": ele[2],
                "estado": ele[3]
            })
        return jsonify(jsonToRetorno)
    except:
        return jsonify([]), 404


app.run()
