-- 04_unique_merchants.sql
-- Distinct normalized merchant_code in first-seen order (min transactions.id).
-- Same join / UNKNOWN / TRIM / case-insensitive name match as 01.
--
-- BUG: INNER JOIN drops unknown merchants; no normalize; order is undefined.

SELECT DISTINCT m.merchant_code
FROM transactions t
INNER JOIN merchants m ON t.merchant_name = m.merchant_name;
