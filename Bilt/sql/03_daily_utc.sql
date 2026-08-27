-- 03_daily_utc.sql
-- Sum final_points by UTC calendar date (YYYY-MM-DD).
-- Use the same join / 3x / FLOOR / UNKNOWN rules as 01.
-- Offset timestamps like 2024-01-15T23:30:00-05:00 belong on 2024-01-16.
--
-- BUG: substr() takes the date prefix in the string, not UTC.
-- Also: no merchant join, so restaurant 3x is missing, and GROUP BY is incomplete.

SELECT
    SUBSTR(transacted_at, 1, 10) AS day,
    SUM(amount) AS points
FROM transactions
GROUP BY user_id
ORDER BY day;
