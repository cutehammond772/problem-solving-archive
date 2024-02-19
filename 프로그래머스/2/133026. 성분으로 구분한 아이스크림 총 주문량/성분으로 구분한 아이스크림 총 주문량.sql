SELECT 
    b.INGREDIENT_TYPE, 
    SUM(a.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF a, ICECREAM_INFO b
WHERE a.FLAVOR = b.FLAVOR
GROUP BY b.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;