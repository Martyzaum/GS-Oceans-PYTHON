import json
import random
import time
from flask import Flask, jsonify

# Definindo os limites para os valores dos sensores
SENSOR_LIMITS = {
    "ph": (0, 14),
    "turbidity": (0, 1000),
    "water_level": (0, 80),
    "temperature": (-2, 100),
    "total_dissolved_solids": (0, 100)
}

app = Flask(__name__)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    """Rota da API para obter dados do sensor."""
    with open("sensor_data.json", 'r') as f:
        data = json.load(f)
    return jsonify(data)

def generate_sensor_data():
    """Gera dados aleatórios para os sensores."""
    data = {}
    for sensor, (min_val, max_val) in SENSOR_LIMITS.items():
        data[sensor] = random.uniform(min_val, max_val)
    return data

def save_to_json(data, filename="sensor_data.json"):
    """Adiciona os dados a um arquivo JSON existente."""
    try:
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(data)

    with open(filename, 'w') as f:
        json.dump(existing_data, f)

def main():
    """Gera novos dados de sensores a cada 5 segundos e salva em um arquivo JSON."""
    while True:
        sensor_data = generate_sensor_data()
        save_to_json(sensor_data)
        print("Dados salvos:", sensor_data)
        time.sleep(5)

if __name__ == "__main__":
    main()
    app.run(debug=True)
