-- 코드를 입력하세요
SELECT 
    SUBSTR(product_code, 1, 2) AS CATEGORY,
    COUNT(product_id) AS PRODUCTS
FROM
    PRODUCT

GROUP BY
    category
ORDER BY
    category ASC;