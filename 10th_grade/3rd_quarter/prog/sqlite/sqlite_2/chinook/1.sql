SELECT
    i.invoice_id,
    t.track_id,
    t.name,
    m.name,
    i.quantity,
    i.unit_price
FROM
    invoice_line AS i
    LEFT JOIN track AS t on i.track_id = t.track_id
    LEFT JOIN media_type AS m on t.media_type_id = m.media_type_id;
