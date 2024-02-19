SELECT a.CATEGORY, a.PRICE AS MAX_PRICE, a.PRODUCT_NAME
FROM FOOD_PRODUCT a
WHERE 
    a.PRICE = (SELECT MAX(b.PRICE) FROM FOOD_PRODUCT b WHERE a.CATEGORY = b.CATEGORY)
    AND a.CATEGORY IN ("과자", "국", "김치", "식용유")
ORDER BY MAX_PRICE DESC;