-- 01_join_points.sql
-- Return one row per transaction, ordered by transactions.id:
--   user_id, merchant_code, category, base_points, final_points
--
-- Rules (same as the Java screen):
--   LEFT JOIN merchants on merchant_name, TRIM + case-insensitive
--   no match → merchant_code and category = 'UNKNOWN'
--   TRIM category when present
--   base_points = FLOOR(amount)
--   Restaurant (trim, case-insensitive) → 3x else 1x
--
-- BUGS in this starter: INNER JOIN, exact name match, ROUND, no UNKNOWN,
-- exact 'Restaurant' (misses 'restaurant' and padded '  Restaurant  ').

SELECT
    t.user_id,
    COALESCE(m.merchant_code, 'UNKNOWN') AS merchant_code,
    COALESCE(m.category, 'UNKNOWN') AS category,
    FLOOR(t.amount) AS base_points,
    CASE
        WHEN LOWER(TRIM(m.category)) = 'restaurant' THEN FLOOR(t.amount) * 3
        ELSE FLOOR(t.amount)
    END AS final_points
FROM transactions t
LEFT JOIN merchants m ON LOWER(TRIM(t.merchant_name)) = LOWER(TRIM(m.merchant_name))
ORDER BY t.id;

