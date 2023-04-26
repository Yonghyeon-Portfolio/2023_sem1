SET search_path TO NSWFuel;

-- all occurences where the price exceeded 235 cents / litre
SELECT * FROM Prices
	WHERE price > 235
	ORDER BY price DESC;