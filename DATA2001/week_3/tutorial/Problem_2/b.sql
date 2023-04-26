SET search_path TO NSWFuel;

-- distinct list of fuel codes that sxceeded this price (235 c/l)
SELECT DISTINCT(fuelcode) FROM Prices
	WHERE price > 235;