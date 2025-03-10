-- 코드를 입력하세요
WITH MEMBER_REVIEW_CNT AS (
    SELECT COUNT(*) AS CNT, M.MEMBER_ID, M.MEMBER_NAME
    FROM MEMBER_PROFILE M
    JOIN REST_REVIEW R
    ON M.MEMBER_ID = R.MEMBER_ID
    GROUP BY M.MEMBER_ID
    ORDER BY CNT DESC
)

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_REVIEW_CNT C
JOIN REST_REVIEW R
ON C.MEMBER_ID = R.MEMBER_ID
WHERE CNT = (SELECT MAX(CNT) FROM MEMBER_REVIEW_CNT)
ORDER BY REVIEW_DATE, REVIEW_TEXT