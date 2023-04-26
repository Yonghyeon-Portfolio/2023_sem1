SET search_path to NSWFuel;

-- SELECT * FROM Prices;
-- COPY Prices(Observation, FuelCode, Price)
-- FROM 'C:Users/yongh/learn/2023_sem1/DATA2001/week_3/tutorial'
-- DELIMITER ','
-- CSV HEADER;

COPY Prices FROM 'Prices.csv' DELIMITER ',' CSV
