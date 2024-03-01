-- 코드를 입력하세요
SELECT
    i.ANIMAL_ID,
    i.NAME
FROM
    ANIMAL_INS AS i
    LEFT OUTER JOIN
    ANIMAL_OUTS AS o
    ON i.animal_id = o.animal_id
ORDER BY
    DATEDIFF(o.datetime, i.datetime) DESC
    LIMIT 2