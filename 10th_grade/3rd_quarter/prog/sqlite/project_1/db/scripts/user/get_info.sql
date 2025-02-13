SELECT
    name,
    lastname,
    middlename,
    ticket
FROM
    users
WHERE
    user_id = ?;
