SELECT
    f.name,
    c_counted.city_count,
    c_capital.capital_name,
    c_capital.capital_population,
    CAST(c_capital.capital_population AS FLOAT) / f.population * 100
FROM
    facts as f
    RIGHT JOIN (
        SELECT
            COUNT(c.name) AS city_count,
            c.facts_id
        FROM
            cities as c
        GROUP BY
            c.facts_id
    ) AS c_counted ON f.id = c_counted.facts_id
    RIGHT JOIN (
        SELECT
            c.name AS capital_name,
            c.population AS capital_population,
            c.facts_id
        FROM
            cities as c
        WHERE
            c.capital = 1
    ) AS c_capital ON f.id = c_capital.facts_id;
