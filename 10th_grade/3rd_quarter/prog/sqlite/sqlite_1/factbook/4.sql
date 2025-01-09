SELECT
    f.name,
    f.area
FROM
    facts as f
ORDER BY
    id DESC
LIMIT
    10
    -- it wasn't specified in the task in which order should be the last 10 records
