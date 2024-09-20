-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID,DATE_FORMAT(START_DATE,'%Y-%m-%d')as START_DATE, DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE,
case
when DATEDIFF(END_DATE,START_DATE)+1>= 30 then '장기 대여'
else '단기 대여'
end as RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE "2022_09%"
ORDER BY HISTORY_ID DESC

