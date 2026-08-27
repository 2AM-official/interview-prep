-- 02_fill_in.sql
-- Same result as 01_join_points.sql. Replace every ____.
-- Do not leave the underscores in the file.

SELECT
    t.user_id,
    ____ AS merchant_code,
    ____ AS category,
    ____ AS base_points,
    ____ AS final_points
FROM transactions t
____ JOIN merchants m
    ON ____
ORDER BY t.id;
