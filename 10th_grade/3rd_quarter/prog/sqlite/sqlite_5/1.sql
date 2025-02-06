CREATE VIEW v_employee_info AS
SELECT
    e.emp_name,
    e.salary,
    d.dept_name
FROM
    employees AS e
    JOIN departments AS d ON e.dept_id = d.dept_id
WHERE
    e.salary > AVG(e.salary) OVER (
        PARTITION BY
            d.dept_id
    );

SELECT
    *
FROM
    v_employee_info;
