from flask import Flask, jsonify, render_template

app = Flask(__name__)
filminhos = { '1': {'id': '1', 'titulo': 'One piece'}, 
            '2': { 'id': '2', 'titulo': 'Motoqueiro Fantasma '},
            '3': { 'id': '3', 'titulo': 'Scarface', 'diretor': 'Brian De Palma', 'genero': 'Crime / Drama',
                 'poster': '/static/posteres/scarface-2.jpg', 'ano': 1983 }, 
            '4': { 'id': '4', 'titulo': 'Os Bons Companheiros', 'diretor': 'Martin Scorsese', 'genero': 'Crime / Biografia / Drama',
                 'poster': '/static/posteres/l_54529_0099685_307a5bd2.jpg', 'ano': 1990 } 
        }


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', filmes=filminhos)

@app.route('/filmes', methods = ['GET'])
def filmes(filminhos = filminhos):
    return jsonify(filminhos)

if __name__ == '__main__':
    app.run(debug=True)