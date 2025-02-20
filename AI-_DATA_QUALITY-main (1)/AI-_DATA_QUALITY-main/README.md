# Real-Time Quality Validation for Streaming Data Using AI

This project demonstrates real-time quality validation for streaming data using AI. It simulates a stream of sensor data, detects anomalies using an Isolation Forest model, and visualizes the results.

## Features

- **Data Simulation**: Generates synthetic sensor data with occasional anomalies.
- **Anomaly Detection**: Uses an Isolation Forest model to detect anomalies in real-time.
- **Visualization**: Plots the sensor data with anomalies highlighted.

## Requirements

### To run this project, you need the following Python libraries:

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`

# You can install the required libraries using pip:

```bash
pip install numpy pandas scikit-learn matplotlib

Usage
Clone the repository:

bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Run the main.py script:

bash
python main.py

How It Works
Data Simulation:

The script simulates a stream of sensor data with a 10% chance of generating anomalies.

Each data point includes a timestamp and a value.

Anomaly Detection:

An Isolation Forest model is trained on normal data.

The model predicts whether each new data point is an anomaly.

Real-Time Processing:

The script processes data in real-time, printing whether each data point is valid or an anomaly.

Visualization:

The script plots the sensor data over time, highlighting anomalies in red.

Example Output
Console Output:

{'timestamp': '2023-10-01 12:00:00', 'value': 45.67}
Valid data: {'timestamp': '2023-10-01 12:00:01', 'value': 47.89}
Anomaly detected: {'timestamp': '2023-10-01 12:00:02', 'value': 250.12}

Plot:

A time series plot showing sensor data with anomalies highlighted.
