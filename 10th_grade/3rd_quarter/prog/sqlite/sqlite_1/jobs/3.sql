SELECT
    Major
FROM
    recent_grads
WHERE
    ShareWomen BETWEEN 0.5 AND 0.8
ORDER BY
    ShareWomen DESC
LIMIT
    10;
