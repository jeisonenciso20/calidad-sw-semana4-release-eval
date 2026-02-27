from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

DATA_PATH = "data\\appointments.json"

ADMIN_USER = "admin"
ADMIN_PASS = "admin"

def load_appointments():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_appointments(appts):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(appts, f)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login():
    data = request.json or {}
    if data.get("user") != ADMIN_USER:
        return {"error": "Usuario no existe"}, 401
    if data.get("password") != ADMIN_PASS:
        return {"error": "Contraseña incorrecta"}, 401
    return {"message": "login ok", "token": "STATIC"}, 200

@app.get("/appointments")
def list_appointments():
    return jsonify(load_appointments())

@app.post("/appointments")
def create_appointment():
    appts = load_appointments()
    data = request.json or {}

    dt = datetime.strptime(data["date"] + " " + data["time"], "%Y-%m-%d %H:%M")

    new_id = max([a["id"] for a in appts]) + 1
    appts.append({
        "id": new_id,
        "patient": data["patient"],
        "date": data["date"],
        "time": data["time"],
        "doctor": data["doctor"]
    })
    save_appointments(appts)
    return {"id": new_id}, 201

if __name__ == "__main__":
    app.run(debug=True)