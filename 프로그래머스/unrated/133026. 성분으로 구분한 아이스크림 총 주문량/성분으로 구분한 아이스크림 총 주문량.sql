-- 코드를 입력하세요
SELECT  i.INGREDIENT_TYPE , SUM(f.total_order) AS TOTAL_ORDER
FROM FIRST_HALF f join ICECREAM_INFO i on f.flavor = i.flavor
group by i.ingredient_type
order by f.total_order ASC;