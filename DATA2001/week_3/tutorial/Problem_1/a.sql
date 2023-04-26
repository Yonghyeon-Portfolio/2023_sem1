-- List all recorded stations in surrounding suburbs of Redfern 
-- Redfern's surrounding suburbs have postcodes 2014 ~ 2018.
SET search_path TO NSWFuel;

SELECT * FROM Stations
	WHERE postcode BETWEEN 2014 AND 2018;
	