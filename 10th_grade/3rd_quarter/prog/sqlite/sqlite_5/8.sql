SELECT
    *,
    DENSE_RANK() OVER (
        PARTITION BY
            dept_id
        ORDER BY
            salary DESC
    ) AS rank
FROM
    employees;
