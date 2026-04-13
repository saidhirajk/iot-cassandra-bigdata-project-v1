from cassandra.cluster import Cluster
import pandas as pd

cluster = Cluster(["127.0.0.1"])
session = cluster.connect("iot_sensors")

# latest data
rows = session.execute("SELECT * FROM sensor_latest")
df = pd.DataFrame(list(rows))

print("\nLatest Sensor Readings:\n")
print(df)

# one sensor data
rows = session.execute("""
SELECT * FROM sensor_readings
WHERE sensor_id='sensor-001'
LIMIT 10
""")

print("\nSample Sensor Data:\n")
for r in rows:
    print(r)

cluster.shutdown()