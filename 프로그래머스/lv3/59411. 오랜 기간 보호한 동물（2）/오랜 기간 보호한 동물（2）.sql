-- 코드를 입력하세요
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_OUTS B JOIN ANIMAL_INS A ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(B.DATETIME, A.DATETIME) DESC
LIMIT 2