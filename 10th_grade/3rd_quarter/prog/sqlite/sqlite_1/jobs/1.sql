SELECT
    Major_category
FROM
    recent_grads
GROUP BY
    Major_category
HAVING
    SUM(ShareWomen) > 5;
