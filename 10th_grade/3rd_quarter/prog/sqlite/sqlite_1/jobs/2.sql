SELECT
    Major,
    (1 - ShareWomen) * 100
FROM
    recent_grads
GROUP BY
    Major;
