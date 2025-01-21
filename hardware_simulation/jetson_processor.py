import serial

# Connect to the virtual serial port (same as rs232_simulator)
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)

def process_data(data):
    fields = data.strip().split(',')
    weight = fields[0]
    voltages = fields[1:]
    print(f"Processed Data - Weight: {weight} kg, Voltages: {voltages}")
    # Save or pass the processed data to the web application (future steps)

while True:
    if ser.in_waiting:
        raw_data = ser.readline().decode('utf-8')
        process_data(raw_data)
