SELECT
    *,
    RANK() OVER (
        ORDER BY
            salary DESC
    ) AS rank
FROM
    employees;
