-- 코드를 작성해주세요
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S
ON S.CATEGORY = 'Front End'
WHERE D.SKILL_CODE & S.CODE = S.CODE
ORDER BY D.ID