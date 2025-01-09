SELECT
    *
FROM
    cities
WHERE
    (name IS NULL)
    OR (population IS NULL)
    OR (capital IS NULL);
