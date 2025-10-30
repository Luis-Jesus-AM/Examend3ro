from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_seguridad'

@app.route("/tmb", methods=['GET', 'POST'])
def formulario_y_calculo():
    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso', 0))
            altura = float(request.form.get('altura', 0))
            edad = float(request.form.get('edad', 0))
            genero = request.form.get('genero')
            actividad = request.form.get('actividad')

            if not all([peso, altura, edad, genero, actividad]):
                return render_template("forma.html", error="Por favor, completa todos los campos.")

            if genero.lower() == 'hombre':
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
            elif genero.lower() == 'mujer':
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
            else:
                return render_template("forma.html", error="Género inválido.")

            factores = {
                'sedentario': 1.2,
                'ligera': 1.375,
                'moderada': 1.55,
                'alta': 1.725
            }

            factor_actividad = factores.get(actividad.lower())
            if factor_actividad is None:
                return render_template("forma.html", error="Nivel de actividad inválido.")

            get_total = tmb * factor_actividad

            return render_template(
                "re.html",
                tmb=f"{tmb:.2f}",
                get_total=f"{get_total:.2f}",
                peso=peso,
                altura=altura,
                edad=edad,
                genero=genero,
                actividad=actividad
            )

        except ValueError:
            return render_template("forma.html", error="Introduce valores numéricos válidos en Peso, Altura y Edad.")
        except Exception:
            return render_template("forma.html", error="Ocurrió un error inesperado. Asegúrate de que los valores sean positivos.")

    return render_template("forma.html", error=None)

if __name__ == "__main__":
    app.run(debug=True)
