SELECT
    album.title,
    artist.name,
    summed_quantity
FROM
    album
    LEFT JOIN artist ON album.artist_id = artist.artist_id
    LEFT JOIN (
        SELECT
            i_summed.summed_quantity as summed_quantity,
            t.album_id AS tt
        FROM
            (
                SELECT
                    i.track_id,
                    SUM(i.quantity) AS summed_quantity
                FROM
                    invoice_line AS i
                GROUP BY
                    track_id
            ) AS i_summed
            LEFT JOIN track AS t ON i_summed.track_id = t.track_id
        GROUP BY
            t.album_id
    ) ON album.album_id = tt;
