-- 코드를 입력하세요
SELECT
    u.USER_ID,
    u.NICKNAME,
    CONCAT(u.CITY, " ", u.STREET_ADDRESS1, " ",u.STREET_ADDRESS2) AS 전체주소,
    CONCAT(SUBSTR(u.tlno, 1, 3), "-", SUBSTR(u.tlno, 4, 4), "-", SUBSTR(u.tlno, 8, 4)) AS 전화번호
FROM
    USED_GOODS_BOARD AS b
    RIGHT OUTER JOIN
    USED_GOODS_USER AS u
        ON b.WRITER_ID = u.user_id
# GROUP BY
#     b.Writer_id
GROUP BY 1

HAVING
    COUNT(*) >= 3
ORDER BY
    u.user_id DESC