-- 코드를 입력하세요
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(start_date, "%Y-%m-%d") AS START_DATE,
    DATE_FORMAT(end_date, "%Y-%m-%d") AS END_DATE,  
    CASE
        WHEN DATEDIFF(end_date, start_date) +1 >= 30 THEN '장기 대여'
        ELSE '단기 대여' 
    END AS RENT_TYPE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE
#     YEAR(start_date) = 2022
#     AND
#     MONTH(start_date) = 9
    
WHERE  START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY
    history_id DESC;