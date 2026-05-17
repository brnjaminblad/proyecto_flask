from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    resultado = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        precio = 9000
        total = tarros * precio

        descuento = 0

        # DESCUENTOS
        if edad >= 18 and edad <= 30:
            descuento = 0.15

        elif edad > 30:
            descuento = 0.25

        total_pagar = total - (total * descuento)

        resultado = {
            "nombre": nombre,
            "total": total,
            "descuento": int(descuento * 100),
            "final": int(total_pagar),
        }


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    mensaje = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
