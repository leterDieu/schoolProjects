DROP VIEW v;

SELECT
    *
FROM
    sqlite_master
WHERE
    type = 'table';
