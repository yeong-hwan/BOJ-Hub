-- 코드를 입력하세요
SELECT
    f.flavor AS FLAVOR
FROM
    FIRST_HALF AS f
    LEFT OUTER JOIN
    JULY AS j
    ON f.flavor = j.flavor
GROUP BY
    f.flavor
ORDER BY
    (SUM(f.total_order) + SUM(j.total_order)) DESC
LIMIT 3;