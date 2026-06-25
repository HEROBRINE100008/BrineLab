from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def page():
    return render_template("index.html")


@app.route("/recibir", methods=["POST"])
def recibir():
    texto = request.form["xd"]
    print(f"La palabra que dijo el singasumadre del usuario fue:{texto}")
    
    return f"<h1>Entonce dijite {texto}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
