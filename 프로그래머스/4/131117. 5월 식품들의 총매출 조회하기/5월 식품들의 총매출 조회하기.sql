-- 코드를 입력하세요
SELECT
    p.PRODUCT_ID,
    p.PRODUCT_NAME,
    SUM(o.amount * p.price) AS TOTAL_SALES
FROM
    FOOD_PRODUCT AS p
    LEFT OUTER JOIN
    FOOD_ORDER AS o
        ON p.product_id = o.product_id
WHERE
    YEAR(o.produce_date) = 2022
    AND
    MONTH(o.produce_date) = 5
GROUP BY
    p.PRODUCT_ID
ORDER BY
    TOTAL_SALES DESC,
    p.product_id ASC;