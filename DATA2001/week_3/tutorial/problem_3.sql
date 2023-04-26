SET search_path TO NSWFuel;

/* a. List all observations made between 2am and 3am */
SELECT * FROM Observations
	WHERE pricetime BETWEEN '02:00:00' AND '03:00:00';

/* b. Of stations in the suburbs you investigate in Q1_A,
	what was the earlist and latest time for which 
	observations were made? */
SELECT
	MIN(pricetime) AS "earliest observation in the time range", 
	MAX(pricetime) AS "latest observation in the time range"
FROM Observations
	LEFT JOIN Stations ON (ServiceStation = ServiceStationNo)
	WHERE postcode between 2014 AND 2018;

/* c. For these stations and for an arbitary fuel type,
	list all observations in ascending order of price,
	with a column indicating whether each observation
	was made on a weekday or weekend. */

SELECT servicestationname AS "station", suburb,
	name AS "fuel name", price,
	CASE
		WHEN EXTRACT(ISODOW FROM pricedate) IN (6, 7)
			THEN 'Weekend'
		ELSE 'Weekday'
	END AS "week - day/end"
FROM Observations
	JOIN Stations ON (servicestation = ServiceStationNo)
	JOIN Prices ON (ObservationNo = Observation)
	JOIN Fuel ON (FuelCode = Fuel)
WHERE postcode BETWEEN 2014 AND 2018
ORDER BY fuel, price DESC;

