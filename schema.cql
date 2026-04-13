CREATE KEYSPACE IF NOT EXISTS iot_sensors
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};

USE iot_sensors;

CREATE TABLE IF NOT EXISTS sensor_readings (
    sensor_id text,
    event_time timestamp,
    temperature double,
    humidity double,
    pressure double,
    PRIMARY KEY (sensor_id, event_time)
) WITH CLUSTERING ORDER BY (event_time DESC);

CREATE TABLE IF NOT EXISTS sensor_latest (
    sensor_id text PRIMARY KEY,
    event_time timestamp,
    temperature double,
    humidity double,
    pressure double
);