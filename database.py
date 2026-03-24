import sqlite3

def init_db():
    conn = sqlite3.connect('irrigation_system.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY,
            soil_moisture REAL,
            temperature REAL,
            humidity REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_sensor_data(soil_moisture, temperature, humidity):
    conn = sqlite3.connect('irrigation_system.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO sensor_data (soil_moisture, temperature, humidity)
        VALUES (?, ?, ?)
    ''', (soil_moisture, temperature, humidity))
    conn.commit()
    conn.close()

init_db()
