CREATE TABLE countries(
	country_id SMALLINT NOT NULL PRIMARY KEY,
	country_name varchar(40) NOT NULL UNIQUE /*My solution:*/ CHECK (country_name = 'Italy' or country_name = 'India' or country_name = 'China'),
	/*Better solution: CHECK (country_name in ('Italy', 'India', 'China'))*/
	region_id SMALLINT
);