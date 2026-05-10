from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')



# .::EJERCICIO 1::.


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    resultado = None
    error = None

    if request.method == 'POST':

        try:

            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Validaciones
            notas = [nota1, nota2, nota3]

            for nota in notas:
                if nota < 10 or nota > 70:
                    error = "Las notas deben estar entre 10 y 70"

            if asistencia < 0 or asistencia > 100:
                error = "La asistencia debe estar entre 0 y 100"

            if error is None:

                promedio = (nota1 + nota2 + nota3) / 3

                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"

                resultado = {
                    'promedio': round(promedio, 1),
                    'estado': estado
                }

        except ValueError:
            error = "Solo se permiten números enteros"

    return render_template(
        'ejercicio1.html',
        resultado=resultado,
        error=error
    )



# .:: EJERCICIO 2 ::.

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    resultado = None
    error = None

    if request.method == 'POST':

        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]

        # Solo letras y espacios
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$'

        for nombre in nombres:

            if not re.match(patron, nombre):
                error = "Los nombres solo pueden contener letras"

        if error is None:

            nombre_largo = max(nombres, key=len)

            cantidad = len(nombre_largo)

            resultado = {
                'nombre': nombre_largo,
                'cantidad': cantidad
            }

    return render_template(
        'ejercicio2.html',
        resultado=resultado,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)