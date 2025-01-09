SELECT
    c.population / (
        SELECT
            SUM(c.population)
        from
            cities as c
    ) as Population_percantage
FROM
    cities as c;
