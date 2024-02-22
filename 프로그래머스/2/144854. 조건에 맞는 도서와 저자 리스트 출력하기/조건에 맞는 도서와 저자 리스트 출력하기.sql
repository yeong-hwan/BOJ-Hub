-- 코드를 입력하세요
SELECT
    b.book_id AS BOOK_ID,
    a.author_name AS AUTHOR_NAME,
    DATE_FORMAT(b.published_date, "%Y-%m-%d") AS PUPLISHED_DATE
FROM
    BOOK AS b
    LEFT OUTER JOIN
    AUTHOR AS a
    ON b.author_id = a.author_id
WHERE
    b.category = "경제"
ORDER BY
    b.published_date ASC;