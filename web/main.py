from flask import Flask, request, jsonify, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

#porcatroia

app = Flask(__name__)
data = pd.DataFrame(columns=['timestamp', 'voltage', 'current'])

@app.route('/data', methods=['POST'])
def receive_data():
    global data
    new_data = request.get_json()
    timestamp = pd.Timestamp.now()
    new_data['timestamp'] = timestamp
    data = data.append(new_data, ignore_index=True)
    return jsonify({"status": "success"})

@app.route('/')
def index():
    global data
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot della tensione
    ax[0].plot(data['timestamp'], data['voltage'], label='Voltage (V)')
    ax[0].set_title('Voltage over Time')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Voltage (V)')
    ax[0].legend()
    
    # Plot della corrente
    ax[1].plot(data['timestamp'], data['current'], label='Current (A)')
    ax[1].set_title('Current over Time')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Current (A)')
    ax[1].legend()
    
    # Salva i grafici in formato PNG
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    return render_template('index.html', image_base64=image_base64)

@app.route('/update', methods=['GET'])
def update():
    global data
    # Aggiorna la pagina con i dati più recenti
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
