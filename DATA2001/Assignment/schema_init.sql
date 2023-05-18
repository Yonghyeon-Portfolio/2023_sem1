DROP TABLE IF EXISTS sa2_bounds;
CREATE TABLE sa2_bounds(
    code INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    area_sq_km NUMERIC NOT NULL check(area_sq_km > 0),
    geom GEOMETRY(MULTIPOLYGON, 4326) NOT NULL
);

DROP TABLE IF EXISTS bussiness;
CREATE TABLE bussiness (
    industry_name VARCHAR(100) NOT NULL,
    sa2_code INT NOT NULL,
    total_businesses INT NOT NULL CHECK(total_businesses >= 0),
    PRIMARY KEY(industry_name, sa2_code)
);

DROP TABLE IF EXISTS stops;
CREATE TABLE stops (
    stop_id VARCHAR(20) PRIMARY KEY,
    stop_name VARCHAR(100) NOT NULL,
    stop_loc GEOMETRY(POINT, 4326) NOT NULL
);

DROP TABLE IF EXISTS polls;
CREATE TABLE polls(
    poll_id INT PRIMARY KEY,
    poll_name VARCHAR(100) NOT NULL,
    poll_loc GEOMETRY(POINT, 4326) NOT NULL
);

DROP TABLE IF EXISTS population;
CREATE TABLE population(
    sa2_code INT PRIMARY KEY,
    young_people INT NOT NULL CHECK (young_people >= 0),
    total_people INT NOT NULL CHECK (total_people >= 0)
);

DROP TABLE IF EXISTS income;
CREATE TABLE income(
    sa2_code INT PRIMARY KEY,
    median_income INT NOT NULL CHECK (median_income > 0)
);

DROP TABLE IF EXISTS score_table;
CREATE TABLE score_table(
    sa2_code INT PRIMARY KEY,
    raw_score INT NOT NULL,
    z_score NUMERIC NOT NULL,
    score_desc VARCHAR(32) NOT NULL
);





