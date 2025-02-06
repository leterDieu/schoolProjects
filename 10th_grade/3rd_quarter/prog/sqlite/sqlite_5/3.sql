CREATE VIEW v_high_salary AS
SELECT
    *
FROM
    employees
WHERE
    salary > 10000;

SELECT
    MIN(salary)
FROM
    v_high_salary;

SELECT
    *
FROM
    v_high_salary;
