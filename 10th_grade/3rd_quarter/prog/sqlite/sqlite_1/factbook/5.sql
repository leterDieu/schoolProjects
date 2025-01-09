SELECT
    ROUND(
        100 * population / (
            SELECT
                SUM(population)
            FROM
                cities
        ),
        10
    ) AS Population_percantage
FROM
    cities;
