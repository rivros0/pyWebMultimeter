import machine
import network
import urequests
import utime

# Configura la connessione WiFi
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Connection successful')
print(station.ifconfig())

# Configura i pin
adc = machine.ADC(0)

# Funzioni per leggere tensione e corrente
def read_voltage():
    # Lettura dal pin analogico e conversione a tensione
    value = adc.read()
    voltage = value * (3.3 / 1024)  # Calibra in base al partitore di tensione
    return voltage

def read_current():
    # Lettura dal pin analogico e conversione a corrente
    value = adc.read()
    current = (value - 512) * (5.0 / 1024)  # Calibra in base al sensore ACS712
    return current

# Invia i dati al server web
while True:
    voltage = read_voltage()
    current = read_current()
    data = {
        'voltage': voltage,
        'current': current
    }
    response = urequests.post('http://YOUR_SERVER_IP:5000/data', json=data)
    print(response.text)
    utime.sleep(10)  # Invia ogni 10 secondi
