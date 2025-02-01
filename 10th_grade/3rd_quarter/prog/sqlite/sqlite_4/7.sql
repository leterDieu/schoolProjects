-- note: another (more logical in my opinion, bt not expected) solution is commented out
-- if u'r goin to use that one, comment out 11th and 27th lines
WITH
    genre_count_CTE (actor, genre_count) AS (
        SELECT
            p.name AS actor,
            -- 1 + LENGTH (GROUP_CONCAT (DISTINCT gt.genre_name)) - LENGTH (
            --     REPLACE (GROUP_CONCAT (DISTINCT gt.genre_name), ',', '')
            -- ) AS genre_count
            1 + LENGTH (GROUP_CONCAT (gt.genre_name)) - LENGTH (GROUP_CONCAT (gt.genre_name, '')) AS genre_count
        FROM
            titles AS t
            LEFT JOIN crew AS c ON t.title_id = c.title_id
            LEFT JOIN people AS p ON c.person_id = p.person_id
            LEFT JOIN film_genres AS fg ON t.title_id = fg.title_id
            LEFT JOIN genre_types AS gt ON fg.genre_id = gt.id
        GROUP BY
            p.name
        HAVING
            genre_count > 100
    )
SELECT
    t2.title,
    t2.premiered,
    r2.rating,
    -- GROUP_CONCAT (DISTINCT gt2.genre_name),
    GROUP_CONCAT (gt2.genre_name),
    COUNT(DISTINCT actor) AS actors_count,
    GROUP_CONCAT (DISTINCT actor)
FROM
    genre_count_CTE
    LEFT JOIN people AS p2 ON genre_count_CTE.actor = p2.name
    LEFT JOIN crew AS c2 ON p2.person_id = c2.person_id
    LEFT JOIN titles AS t2 ON c2.title_id = t2.title_id
    LEFT JOIN rating AS r2 ON t2.title_id = r2.title_id
    LEFT JOIN film_genres AS fg2 ON t2.title_id = fg2.title_id
    LEFT JOIN genre_types AS gt2 ON fg2.genre_id = gt2.id
GROUP BY
    t2.title
HAVING
    actors_count >= 2
ORDER BY
    actors_count;
