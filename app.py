from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "secreto123"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tomasgiovanardi@gmail.com'   
app.config['MAIL_PASSWORD'] = 'qcyh ksfn zdtf zlvb'        
app.config['MAIL_DEFAULT_SENDER'] = 'tomasgiovanardi@gmail.com'

mail = Mail(app)


info_evento = {
    1: {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades: 30km y 80km.",
        "fecha": "24 de Octubre de 2025",
        "horario": "8:00 AM",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB Rural",
        "modalidad_costo": {
            1: {"nombre": "Corta", "valor": "100"},
            2: {"nombre": "Larga", "valor": "200"}
        },
        "Auspiciantes": ["Scott", "TREK"]
    }
}

@app.route("/")
def index():
    return render_template("index.html", info_evento=info_evento)

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        modalidad = request.form.get("modalidad")

        if not nombre or not email or not modalidad:
            flash("⚠️ Faltan datos en el formulario.")
            return redirect(url_for("registration"))

        
        msg = Message(
            subject="Nueva inscripción - Rally MTB 2025",
            recipients=["tomasgiovanardi@gmail.com"],
            body=f"Nombre: {nombre}\nCorreo: {email}\nModalidad: {modalidad}"
        )
        mail.send(msg)

        
        confirmacion = Message(
            subject="Confirmación de inscripción - Rally MTB 2025",
            recipients=[email],
            body=f"Hola {nombre}, tu inscripción fue registrada.\n"
                 f"Modalidad elegida: {modalidad}.\n"
                 "¡Gracias por participar!"
        )
        mail.send(confirmacion)

        flash("✅ Inscripción enviada y confirmación enviada al correo.")
        return redirect(url_for("index"))

    return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)