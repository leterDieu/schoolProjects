CREATE VIEW v AS
SELECT
    *,
    salary * 12 AS yearly_salary
FROM
    employees;

SELECT
    *
FROM
    v;
