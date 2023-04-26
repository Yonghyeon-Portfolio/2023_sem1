-- What fuel types are available in Premium?
SET search_path TO NSWFuel;

SELECT * FROM Fuel
	WHERE name LIKE '%Premium%';