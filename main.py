from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    resultado = None
    error = None

    if request.method == "POST":
        try:
            nombre = request.form["nombre"].strip()
            edad = int(request.form["edad"])
            tarros = int(request.form["tarros"])

            # .:: validaciones ::.
            if not nombre.replace(" ", "").isalpha():
                error = "El nombre solo puede contener letras"

            elif edad < 1 or edad > 120:
                error = "Ingrese una edad válida"

            elif tarros < 1:
                error = "Debe comprar mínimo 1 tarro"

            if error is None:
                precio = 9000
                total = tarros * precio

                descuento = 0

                if 18 <= edad <= 30:
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

        except ValueError:
            error = "Ingrese datos válidos"

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    mensaje = None

    if request.method == "POST":
        usuario = request.form["usuario"].strip().lower()
        password = request.form["password"]

        # .:: validacion backend ::.
        if not usuario.isalpha():
            mensaje = "Usuario inválido"

        elif usuario == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
