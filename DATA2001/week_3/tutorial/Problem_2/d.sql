SET search_path TO NSWFuel;

-- While excluding premium fuels, list the 
-- 10 most expensive occurences of fuel prices.
SELECT fuelcode, price, name
FROM Prices INNER JOIN Fuel 
	ON (fuelcode = fuel)
WHERE price > 235
	AND name NOT LIKE '%Premium%'
ORDER BY price DESC
	LIMIT 10;
