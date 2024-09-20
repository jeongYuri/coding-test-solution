-- 코드를 입력하세요
SELECT CART_ID
from cart_products
where name in('Yogurt','Milk')
group by CART_ID
HAVING COUNT(DISTINCT NAME) =2
ORDER BY CART_ID
