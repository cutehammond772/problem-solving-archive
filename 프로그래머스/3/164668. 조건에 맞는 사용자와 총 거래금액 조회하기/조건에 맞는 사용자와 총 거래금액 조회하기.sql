SELECT 
    b.USER_ID, b.NICKNAME,
    SUM(a.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD a, USED_GOODS_USER b
WHERE 
    a.WRITER_ID = b.USER_ID
    AND a.STATUS = "DONE"
GROUP BY b.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC;