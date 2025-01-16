SELECT
    f.name,
    f.population,
    c_summed.city_population,
    CAST(c_summed.city_population AS FLOAT) / f.population * 100
FROM
    facts as f
    RIGHT JOIN (
        SELECT
            SUM(c.population) AS city_population,
            c.facts_id
        FROM
            cities as c
        GROUP BY
            c.facts_id
    ) AS c_summed ON f.id = c_summed.facts_id;
