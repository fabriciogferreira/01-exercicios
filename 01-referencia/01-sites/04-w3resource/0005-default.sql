CREATE TABLE jobs(
	job_id INT PRIMARY KEY,
	job_title CHAR(50) NOT NULL DEFAULT '',
	min_salary FLOAT DEFAULT 8000,
	max_salary FLOAT
);