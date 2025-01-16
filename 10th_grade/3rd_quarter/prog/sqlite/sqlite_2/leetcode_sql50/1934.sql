SELECT
    s.user_id,
    ROUND(ifnull (ccc.confirmation_rate, 0), 2) AS confirmation_rate
FROM
    Signups AS s
    LEFT JOIN (
        SELECT
            cc.user_id AS user_id,
            AVG(cc.confirmation_rate) AS confirmation_rate
        FROM
            (
                SELECT
                    c.user_id AS user_id,
                    c.action = "confirmed" AS confirmation_rate
                FROM
                    Confirmations AS c
            ) AS cc
        GROUP BY
            cc.user_id
    ) AS ccc ON s.user_id = ccc.user_id;
