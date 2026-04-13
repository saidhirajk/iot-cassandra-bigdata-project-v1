# IoT Sensor Data Analysis using Cassandra

## Overview
This project demonstrates a scalable IoT data storage and analysis system using Apache Cassandra.

## Features
- Distributed Cassandra cluster (Docker)
- Time-series data storage
- Data generation using Python
- Visualization and anomaly detection
- Machine learning (Isolation Forest)

## Technologies
- Cassandra
- Python
- Pandas, Matplotlib
- Scikit-learn

## How to Run
1. Start Cassandra:
   docker compose up -d

2. Apply schema:
   Get-Content schema.cql | docker exec -i cassandra-node1 cqlsh

3. Run data generation:
   python generate_data.py

4. Open notebook:
   analyze_visualize.ipynb