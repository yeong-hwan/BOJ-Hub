-- 코드를 입력하세요
SELECT
    u.USER_ID,
    u.NICKNAME,
    SUM(b.PRICE) AS TOTAL_SALES
FROM
    USED_GOODS_USER AS u
    RIGHT OUTER JOIN
    USED_GOODS_BOARD AS b
    ON u.user_id = b.writer_id
    
WHERE
    b.status = "DONE"
    
GROUP BY
    u.USER_ID

HAVING
    TOTAL_SALES >= 700000

ORDER BY
    TOTAL_SALES ASC