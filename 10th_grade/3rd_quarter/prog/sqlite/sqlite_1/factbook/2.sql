SELECT
    c.name,
    c.population
FROM
    cities as c
LIMIT
    10;

SELECT
    f.name,
    f.area
FROM
    facts as f
LIMIT
    10;

SELECT
    s.name,
    s.seq
FROM
    sqlite_sequence as s
LIMIT
    10;
