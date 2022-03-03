from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<contactoID>/edit")
def editarContactos(contactoID):
    suma = 2+2
    return render_template('contactos/editar.html',
    contactoID = contactoID,
    suma=suma
    )

app.run(debug=True)