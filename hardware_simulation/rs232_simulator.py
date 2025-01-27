import random
import serial
import time

# Configure virtual serial port
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Replace COM3 with your system port

def generate_data():
    weight = random.randint(1000, 5000)  # Random weight
    voltages = [round(random.uniform(0, 5), 2) for _ in range(8)]  # Random voltages
    return f"{weight},{','.join(map(str, voltages))}\n"

while True:
    data = generate_data()
    print(f"Sending: {data.strip()}")
    ser.write(data.encode())  # Send data via RS232
    time.sleep(1)