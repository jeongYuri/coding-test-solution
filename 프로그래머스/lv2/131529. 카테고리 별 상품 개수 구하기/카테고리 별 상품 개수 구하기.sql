-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE, 2) AS CATEBORY , COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEBORY
ORDER BY CATEBORY ASC