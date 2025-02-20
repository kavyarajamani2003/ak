from sklearn.ensemble import IsolationForest
import numpy as np
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

def generate_sensor_data():
    """Simulate sensor data with occasional anomalies."""
    timestamp = pd.Timestamp.now()
    value = random.uniform(0, 100)  # Normal range
    if random.random() < 0.1:  # 10% chance of anomaly
        value = random.uniform(200, 300)  # Anomalous range
    return {"timestamp": timestamp, "value": value}

# Simulate a stream of data
for _ in range(20):
    data = generate_sensor_data()
    print(data)
    time.sleep(1)  # Simulate real-time delay

# Train a anomaly detection model
X_train = np.random.rand(100, 1) * 100  # Normal data
model = IsolationForest(contamination=0.1)  # 10% anomalies
model.fit(X_train)

def detect_anomaly(value):
    """Detect if a value is an anomaly."""
    return model.predict([[value]])[0] == -1

for _ in range(20):
    data = generate_sensor_data()
    is_anomaly = detect_anomaly(data["value"])
    if is_anomaly:
        print(f"Anomaly detected: {data}")
    else:
        print(f"Valid data: {data}")
    time.sleep(1)



timestamps = []
values = []
anomalies = []

for _ in range(50):
    data = generate_sensor_data()
    is_anomaly = detect_anomaly(data["value"])
    timestamps.append(data["timestamp"])
    values.append(data["value"])
    anomalies.append(is_anomaly)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(timestamps, values, label="Sensor Data")
plt.scatter(timestamps, values, c=anomalies, cmap="cool", label="Anomalies")
plt.title("Real-Time Quality Validation")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()