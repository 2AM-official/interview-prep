# Part 1 — paste this in Codespaces

Dining: `MCC == 5812` → 3× `floor(TRAN_AMT)`, else 1×.
Skip duplicate `TRANSACTION_ID`. Query alias must be `total_points`.

Real `InterviewTest` expects:

| Test | Assertion |
|---|---|
| `transactions_inserted_to_db` | user **6** = `1968L` |
| `dining_multipliers_applied` | user **1** = `903L`, user **39** = `268L` |
| `point_balance_query_returns_user_total` | insert 10 + 7 → `17L` |
| `calculate_points_persists_transactions` | `COUNT(*) > 0` |

Practice CSV uses smaller totals. Run `./run-part1-tests.sh`.
