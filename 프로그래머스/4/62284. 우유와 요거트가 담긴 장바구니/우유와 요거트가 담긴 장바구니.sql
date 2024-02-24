SELECT DISTINCT a.CART_ID
FROM 
    CART_PRODUCTS a JOIN CART_PRODUCTS b
    ON a.CART_ID = b.CART_ID
WHERE 
    (a.NAME = "Milk" AND b.NAME = "Yogurt")
    OR
    (b.NAME = "Milk" AND a.NAME = "Yogurt")
ORDER BY a.CART_ID;
