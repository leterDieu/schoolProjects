SELECT
    salary,
    LAG (salary) OVER ()
FROM
    employees;
