# Bilt SQL practice

Same rewards rules as the Java screen. Edit the `0*.sql` files, not `setup.sql` or `test_sql.py`.

```bash
cd sql
./run-sql-tests.sh
```

Run one file:

```bash
./run-sql-tests.sh 01
./run-sql-tests.sh fill
./run-sql-tests.sh daily
./run-sql-tests.sh unique
```

| File | Task |
|---|---|
| `01_join_points.sql` | Fix a buggy join query (UNKNOWN, 3× restaurant, FLOOR, trim/case) |
| `02_fill_in.sql` | Fill in `____` — same output as 01 |
| `03_daily_utc.sql` | Sum final points by **UTC** date, not `SUBSTR` of the timestamp |
| `04_unique_merchants.sql` | Distinct normalized merchant codes, first-seen order |

Expected on a fresh checkout: all four fail.
