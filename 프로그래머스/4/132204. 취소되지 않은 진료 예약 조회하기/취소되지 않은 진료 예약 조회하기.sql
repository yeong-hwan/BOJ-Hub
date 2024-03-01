-- 코드를 입력하세요
SELECT
    a.APNT_NO,
    p.PT_NAME,
    p.PT_NO,
    d.MCDP_CD,
    d.DR_NAME,
    a.APNT_YMD

FROM
    PATIENT AS p
    RIGHT OUTER JOIN
    APPOINTMENT AS a
        ON p.pt_no = a.pt_no
    LEFT OUTER JOIN
    DOCTOR AS d
        ON a.mddr_id = d.dr_id
WHERE
    a.APNT_YMD LIKE "2022-04-13%"
    AND
    a.APNT_CNCL_YN = "N"
    AND
    a.MCDP_CD = "CS"
ORDER BY
    a.APNT_YMD ASC