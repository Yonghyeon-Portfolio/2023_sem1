CREATE SCHEMA IF NOT EXISTS NSWFuel;
SET search_path to NSWFuel;

DROP TABLE IF EXISTS Prices;
CREATE TABLE Prices(
   Observation INTEGER,
   FuelCode VARCHAR(3),
   Price NUMERIC
);

DROP TABLE IF EXISTS Observations;
CREATE TABLE Observations(
   ServiceStation INTEGER,
   ObservationNo INTEGER,
   PriceDate DATE,
   PriceTime TIME,
   PRIMARY KEY (ServiceStation, ObservationNo)
);

DROP TABLE IF EXISTS Stations;
CREATE TABLE Stations(
   ServiceStationNo INTEGER PRIMARY KEY,
   ServiceStationName VARCHAR(100),
   Address VARCHAR(100),
   Suburb VARCHAR(50),
   Postcode INTEGER,
   Company VARCHAR(50)
);

DROP TABLE IF EXISTS Companies;
CREATE TABLE Companies(
   Company VARCHAR(50) PRIMARY KEY,
   Founded INTEGER,
   HQCountry VARCHAR(50),
   Source VARCHAR(100)
);

DROP TABLE IF EXISTS Fuel;
CREATE TABLE Fuel(
   Fuel VARCHAR(3) PRIMARY KEY,
   Name VARCHAR(50),
   MainComponent VARCHAR(50)
);