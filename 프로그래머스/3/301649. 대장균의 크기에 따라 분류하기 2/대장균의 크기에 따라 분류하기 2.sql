-- 코드를 작성해주세요
SELECT ID, CASE
            WHEN row_number() over (order by SIZE_OF_COLONY DESC) <= (SELECT COUNT(*) FROM ECOLI_DATA) / 4 THEN 'CRITICAL'
            WHEN row_number() over (order by SIZE_OF_COLONY DESC) <= (SELECT COUNT(*) FROM ECOLI_DATA) / 4 * 2 THEN 'HIGH'
            WHEN row_number() over (order by SIZE_OF_COLONY DESC) <= (SELECT COUNT(*) FROM ECOLI_DATA) / 4 * 3 THEN 'MEDIUM'
            WHEN row_number() over (order by SIZE_OF_COLONY DESC) <= (SELECT COUNT(*) FROM ECOLI_DATA) THEN 'LOW'
            END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID