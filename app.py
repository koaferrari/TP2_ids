from flask import Flask, render_template

app = Flask(__name__)

# Diccionario con la info del evento
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
        "Auspiciantes": ["Ausp1", "Ausp2", "AuspN"]
    }
}

@app.route("/")
def index():
    # Acá le pasamos el diccionario al template
    return render_template("index.html", info_evento=info_evento)

@app.route("/registration", methods=["GET", "POST"])
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)