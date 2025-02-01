SELECT
    t.title
FROM
    titles AS t
    LEFT JOIN film_genres AS fg ON t.title_id = fg.title_id
    LEFT JOIN genre_types AS gt ON fg.genre_id = gt.id
WHERE
    gt.genre_name = 'Comedy'
    AND t.premiered >= 2019
LIMIT
    10;
