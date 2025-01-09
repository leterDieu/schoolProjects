SELECT
    c.name,
    c.population
FROM
    cities as c
ORDER BY
    c.population DESC
LIMIT
    20
