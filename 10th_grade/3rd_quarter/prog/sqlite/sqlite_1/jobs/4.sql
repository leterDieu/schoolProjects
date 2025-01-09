SELECT
    Major
FROM
    recent_grads
WHERE
    (ShareWomen > 0.5)
    OR (Major_category = 'Engineering');
