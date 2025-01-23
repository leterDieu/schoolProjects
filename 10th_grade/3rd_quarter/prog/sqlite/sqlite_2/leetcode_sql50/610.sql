SELECT
    x,
    y,
    z,
    IF (
        GREATEST (x, y, z) < x + y + z - GREATEST (x, y, z),
        'Yes',
        'No'
    ) AS triangle
FROM
    Triangle;
