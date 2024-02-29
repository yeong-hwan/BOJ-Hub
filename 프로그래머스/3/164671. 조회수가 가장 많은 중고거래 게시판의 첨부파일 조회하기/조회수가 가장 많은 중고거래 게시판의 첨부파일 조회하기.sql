-- 코드를 입력하세요
SELECT
    CONCAT("/home/grep/src", "/", b.board_id, "/", f.file_id, f.file_name, f.file_ext) AS FILE_PATH
    # *
FROM
    USED_GOODS_BOARD AS b
    RIGHT OUTER JOIN
    USED_GOODS_FILE AS f
    ON b.board_id = f.board_id

WHERE b.views = (SELECT MAX(views) FROM USED_GOODS_BOARD)

ORDER BY
    b.views DESC,
    f.file_id DESC