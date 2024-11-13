-- 코드를 입력하세요
SELECT MONTH(START_DATE) AS MONTH,CAR_ID,COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE>='2022-08-01' AND START_DATE<='2022-11-01' AND CAR_ID IN(select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where start_date>="2022-08-01" and start_date<"2022-11-01" group by car_id having count(history_id)>4) 
GROUP BY MONTH,CAR_ID
HAVING RECORDS>0
ORDER BY MONTH, CAR_ID DESC