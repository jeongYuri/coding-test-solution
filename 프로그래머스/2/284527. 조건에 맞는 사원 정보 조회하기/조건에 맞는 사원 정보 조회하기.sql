SELECT 
    SUM(C.SCORE) AS SCORE, 
    C.EMP_NO, 
    B.EMP_NAME, 
    B.POSITION, 
    B.EMAIL
FROM 
    HR_EMPLOYEES B
INNER JOIN 
    HR_GRADE C ON B.EMP_NO = C.EMP_NO
GROUP BY C.YEAR, C.EMP_NO
HAVING C.YEAR = '2022'
ORDER BY 
    1 DESC
LIMIT 1;