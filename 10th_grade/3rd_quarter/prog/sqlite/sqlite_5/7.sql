SELECT
    *,
    d.dept_name,
    AVG(e.salary) OVER (
        PARTITION BY
            e.dept_id
    )
FROM
    employees AS e
    JOIN departments AS d ON e.dept_id = d.dept_id;
