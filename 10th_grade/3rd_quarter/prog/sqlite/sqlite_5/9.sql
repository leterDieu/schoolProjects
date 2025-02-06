CREATE VIEW v2 AS
SELECT
    emp_id,
    emp_name,
    ROW_NUMBER() OVER (
        ORDER BY
            salary DESC
    )
FROM
    employees;

SELECT
    *
FROM
    v2;
