from cassandra.cluster import Cluster
import random
from datetime import datetime, timedelta
from tqdm import tqdm

cluster = Cluster(["127.0.0.1"])
session = cluster.connect("iot_sensors")

sensors = [f"sensor-{i:03d}" for i in range(1, 11)]
start = datetime.now()

for i in tqdm(range(200)):
    ts = start + timedelta(seconds=i)

    for s in sensors:
        temp = random.uniform(20, 40)
        if random.random() < 0.05:
            temp = random.choice([
                random.uniform(45, 60),  # high anomaly
                random.uniform(5, 15)    # low anomaly
            ])
        hum = random.uniform(30, 80)
        pres = random.uniform(900, 1100)

        session.execute("""
            INSERT INTO sensor_readings (sensor_id, event_time, temperature, humidity, pressure)
            VALUES (%s, %s, %s, %s, %s)
        """, (s, ts, temp, hum, pres))

        # update latest
        session.execute("""
            INSERT INTO sensor_latest (sensor_id, event_time, temperature, humidity, pressure)
            VALUES (%s, %s, %s, %s, %s)
        """, (s, ts, temp, hum, pres))

print("Data inserted successfully!")
cluster.shutdown()