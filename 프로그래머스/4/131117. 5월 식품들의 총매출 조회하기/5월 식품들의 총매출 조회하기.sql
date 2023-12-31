SELECT A.PRODUCT_ID, A.PRODUCT_NAME,SUM(A.PRICE * B.AMOUNT)AS TOTLA_SALES
FROM FOOD_PRODUCT A RIGHT JOIN FOOD_ORDER B 
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY A.PRODUCT_ID
ORDER BY TOTLA_SALES DESC, A.PRODUCT_ID ASC