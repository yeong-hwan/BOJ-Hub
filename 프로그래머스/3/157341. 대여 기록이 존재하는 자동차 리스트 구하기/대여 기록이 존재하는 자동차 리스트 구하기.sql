-- 코드를 입력하세요
SELECT
    DISTINCT(c.CAR_ID)
FROM
    CAR_RENTAL_COMPANY_CAR AS c
    RIGHT OUTER JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY AS h
        ON c.car_id = h.car_id
        
WHERE
    car_type = "세단"
    AND
    MONTH(h.start_date) = 10
ORDER BY
    c.car_id DESC
    