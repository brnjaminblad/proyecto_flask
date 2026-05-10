from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')



# .::EJERCICIO 1::.


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    resultado = None

    if request.method == 'POST':

        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        resultado = {
            'promedio': round(promedio, 1),
            'estado': estado
        }

    return render_template('ejercicio1.html', resultado=resultado)



# .:: EJERCICIO 2 ::.

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    resultado = None

    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        nombre_largo = max(nombres, key=len)

        cantidad = len(nombre_largo)

        resultado = {
            'nombre': nombre_largo,
            'cantidad': cantidad
        }

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)