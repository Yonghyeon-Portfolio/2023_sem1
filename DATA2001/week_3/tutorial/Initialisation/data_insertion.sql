SET search_path to NSWFuel;

DELETE FROM Prices;
COPY Prices 
	FROM '/Users/Public/SQL_DATA/DATA2001/tutorial_3/Prices.csv' 
	DELIMITER ',' CSV HEADER;

DELETE FROM Observations;
COPY Observations 
	FROM '/Users/Public/SQL_DATA/DATA2001/tutorial_3/Observations.csv' 
	DELIMITER ',' CSV HEADER;

DELETE FROM Stations;
COPY Stations 
	FROM '/Users/Public/SQL_DATA/DATA2001/tutorial_3/Stations.csv' 
	DELIMITER ',' CSV HEADER;

DELETE FROM Companies;
COPY Companies 
	FROM '/Users/Public/SQL_DATA/DATA2001/tutorial_3/Companies.csv' 
	DELIMITER ',' CSV HEADER;
	
DELETE FROM Fuel;
COPY Fuel 
	FROM '/Users/Public/SQL_DATA/DATA2001/tutorial_3/Fuel.csv' 
	DELIMITER ',' CSV HEADER;
	