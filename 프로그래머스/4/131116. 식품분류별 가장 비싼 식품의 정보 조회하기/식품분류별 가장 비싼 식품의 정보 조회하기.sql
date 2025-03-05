-- 코드를 입력하세요

SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE, (SELECT PRODUCT_NAME FROM FOOD_PRODUCT B WHERE A.CATEGORY = B.CATEGORY ORDER BY PRICE DESC LIMIT 0, 1) AS PRODUCT_NAME
FROM FOOD_PRODUCT A
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
ORDER BY 2 DESC;