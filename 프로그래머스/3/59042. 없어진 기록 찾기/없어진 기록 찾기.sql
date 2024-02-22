# SELECT
#     o.ANIMAL_ID,
#     o.NAME
# FROM
#     ANIMAL_INS AS i
#     RIGHT OUTER JOIN
#     ANIMAL_OUTS AS o
#     ON
#         i.ANIMAL_ID = o.ANIMAL_ID

# WHERE
#     i.ANIMAL_ID IS null

SELECT
    ANIMAL_ID,
    NAME
FROM
    animal_outs
WHERE
    animal_id not in (SELECT animal_id FROM animal_ins)
ORDER BY
    animal_id
