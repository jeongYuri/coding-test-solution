WITH RECURSIVE generation_cte AS (
    SELECT
        ID,
        1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT
        e.ID,
        gc.GENERATION + 1
    FROM ECOLI_DATA e
    JOIN generation_cte gc ON e.PARENT_ID = gc.ID
),

no_child_ecoli AS (
    SELECT
        g.ID,
        g.GENERATION
    FROM generation_cte g
    LEFT JOIN ECOLI_DATA c ON g.ID = c.PARENT_ID
    WHERE c.ID IS NULL
)

SELECT
    COUNT(*) AS COUNT,
    GENERATION
FROM no_child_ecoli
GROUP BY GENERATION
ORDER BY GENERATION;
