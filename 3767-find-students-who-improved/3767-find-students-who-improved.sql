# Write your MySQL query statement below
WITH CTE AS(
    SELECT student_id, subject,
    FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date) AS first_score,
    FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score
    FROM Scores
)

SELECT DISTINCT *
FROM CTE
WHERE latest_score > first_score