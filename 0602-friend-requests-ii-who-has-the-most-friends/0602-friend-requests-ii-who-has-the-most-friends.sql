# Write your MySQL query statement below
WITH friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
cnt AS (
    SELECT id, COUNT(*) AS num
    FROM friends
    GROUP BY id
)
SELECT id, num
FROM cnt
ORDER BY num DESC
LIMIT 1;