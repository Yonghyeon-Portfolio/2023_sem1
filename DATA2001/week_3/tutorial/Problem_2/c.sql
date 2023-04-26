SET search_path TO NSWFuel;

-- of these fuel codes, how many times were each recorded 
-- above the price?
SELECT fuelcode, COUNT(fuelcode) 
FROM Prices
	WHERE price > 235
	GROUP BY fuelcode;