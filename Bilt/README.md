# Bilt Java practice

You do **not** need Maven. This machine also did not have a JDK; install Java 17 first:

```bash
brew install openjdk@17
echo 'export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Then from this folder:

```bash
./run-part1-tests.sh   # Codespaces PointService / InterviewTest
./run-tests.sh         # RewardsService debug-the-tests drill
./run-csv-tests.sh     # CSV import + retries
```

## Part 1 — PointService (Codespaces)

Matches the live screen: CSV → `card_transaction`, MCC `5812` is 3×, `floor` amount, skip duplicate `TRANSACTION_ID`, `SUM(points) AS total_points WHERE user_id = ?`.

```bash
./run-part1-tests.sh
```

| Test | Real CSV | Practice CSV |
|---|---|---|
| `transactions_inserted_to_db` | user 6 = 1968 | user 6 = 253 |
| `dining_multipliers_applied` | user 1 = 903, user 39 = 268 | user 1 = 95, user 39 = 21 |
| `point_balance_query_returns_user_total` | insert 10 + 7 → 17 | same |
| `calculate_points_persists_transactions` | `COUNT(*) > 0` | same |

Fix `src/main/java/bilt/part1/PointService.java` and the query in `PointRepository`.

## RewardsService — failing unit tests

Fix `src/main/java/bilt/RewardsService.java` only.

Round 1 (`processRewards`) should already be green. Round 2 methods are **intentionally buggy** — same style as the original screen.

| Test | What it checks |
|---|---|
| `calculatesTriplePointsForRestaurants` | Restaurant is 3× after trim + case-insensitive match; other/null category is 1× |
| `returnsUnknownForNullBlankOrWhitespaceMerchantCode` | `null` / blank / whitespace → `UNKNOWN`; otherwise trim; keep input order |
| `aggregatesPointsByUtcCalendarDate` | Bucket by **UTC** calendar date, not the date prefix in the ISO string |
| `handlesEmptyInput` | Empty list → empty codes and empty daily map |
| `keepsMerchantCodesInInputOrder` | Mixed valid / UNKNOWN codes stay in input order |
| `treatsBlankCategoryAsOneTimesPoints` | `""` / whitespace category is 1×, not restaurant |
| `matchesRestaurantInAllCaps` | `RESTAURANT` is still 3× |
| `normalizesTabOnlyMerchantToUnknown` | Tab-only merchant code → `UNKNOWN` |
| `mergesSeveralTxsOnSameUtcDay` | Several txs on the same UTC day sum |
| `appliesRestaurantMultiplierOnUtcDay` | 3× points land on the UTC date, not the local date |
| `treatsZAndPlusZeroOffsetAsSameInstant` | `Z` and `+00:00` are the same UTC instant |
| `handlesZeroAmount` | Amount 0 stays 0 even for restaurants |
| `uniqueMerchantsNormalizesAndKeepsFirst` | Unique codes: UNKNOWN/trim, first wins, input order |
| `uniqueMerchantsTreatsTrimmedDupesAsOne` | `"  CHIPOTLE  "` and `"CHIPOTLE"` are one merchant |
| `capsEachUtcDayIndependently` | Cap is per UTC day, not a grand total |
| `capDoesNotChangeDaysUnderTheLimit` | Days under the cap stay unchanged |
| `subtractsRefundsUsingSameRules` | Refunds subtract from the same UTC day |
| `refundCannotDriveADayNegative` | Net points for a day cannot go below 0 |
| `restaurantRefundSubtractsTriplePoints` | Restaurant refund subtracts 3× amount |
