SELECT e4.employee_id, e4.department_id FROM
(SELECT e3.employee_id, department_id, MIN(e3.rownum)
FROM
(SELECT ROW_NUMBER () OVER (
        ORDER BY e2.employee_id) rownum, e2.employee_id, e2.department_id
FROM (SELECT e1.employee_id, e1.department_id
FROM Employee AS e1
ORDER BY e1.employee_id, e1.primary_flag) AS e2) AS e3
GROUP BY e3.employee_id) AS e4
