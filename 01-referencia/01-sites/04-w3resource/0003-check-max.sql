CREATE TABLE jobs(
	job_id INT PRIMARY KEY,
	job_title CHAR(50) UNIQUE NOT NULL,
	min_salary FLOAT,
	max_salary FLOAT CHECK (max_salary <= 25000),
);