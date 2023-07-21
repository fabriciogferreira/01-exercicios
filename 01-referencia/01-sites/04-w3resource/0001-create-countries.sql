CREATE TABLE countries(
	country_id SMALLINT NOT NULL PRIMARY KEY,
	country_name varchar(40) NOT NULL UNIQUE,
	region_id SMALLINT
);