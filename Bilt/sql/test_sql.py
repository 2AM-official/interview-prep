#!/usr/bin/env python3
"""Run the Bilt SQL practice queries against setup.sql."""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_setup(conn: sqlite3.Connection) -> None:
    conn.executescript((ROOT / "setup.sql").read_text())


def run_query(conn: sqlite3.Connection, sql: str) -> list[tuple]:
    if "____" in sql:
        raise AssertionError("query still has ____ blanks to fill in")
    cur = conn.execute(sql)
    rows = cur.fetchall()
    return [tuple(normalize(v) for v in row) for row in rows]


def normalize(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def assert_rows(actual, expected):
    if actual != expected:
        raise AssertionError(f"expected {expected!r} but was {actual!r}")


def test_01_join_points(conn):
    sql = (ROOT / "01_join_points.sql").read_text()
    actual = run_query(conn, sql)
    expected = [
        (1, "CHIPOTLE", "Restaurant", 10, 30),
        (1, "UNKNOWN", "UNKNOWN", 5, 5),
        (1, "WHOLE_FOODS", "Grocery", 8, 8),
        (2, "CHIPOTLE", "Restaurant", 10, 30),
        (2, "SHAKE_SHACK", "restaurant", 10, 30),
        (2, "SWEETGREEN", "Restaurant", 4, 12),
        (1, "CHIPOTLE", "Restaurant", 10, 30),
    ]
    assert_rows(actual, expected)


def test_02_fill_in(conn):
    sql = (ROOT / "02_fill_in.sql").read_text()
    actual = run_query(conn, sql)
    expected = [
        (1, "CHIPOTLE", "Restaurant", 10, 30),
        (1, "UNKNOWN", "UNKNOWN", 5, 5),
        (1, "WHOLE_FOODS", "Grocery", 8, 8),
        (2, "CHIPOTLE", "Restaurant", 10, 30),
        (2, "SHAKE_SHACK", "restaurant", 10, 30),
        (2, "SWEETGREEN", "Restaurant", 4, 12),
        (1, "CHIPOTLE", "Restaurant", 10, 30),
    ]
    assert_rows(actual, expected)


def test_03_daily_utc(conn):
    sql = (ROOT / "03_daily_utc.sql").read_text()
    actual = run_query(conn, sql)
    expected = [
        ("2024-01-15", 43),
        ("2024-01-16", 102),
    ]
    assert_rows(actual, expected)


def test_04_unique_merchants(conn):
    sql = (ROOT / "04_unique_merchants.sql").read_text()
    actual = run_query(conn, sql)
    expected = [
        ("CHIPOTLE",),
        ("UNKNOWN",),
        ("WHOLE_FOODS",),
        ("SHAKE_SHACK",),
        ("SWEETGREEN",),
    ]
    assert_rows(actual, expected)


TESTS = [
    ("01_join_points", test_01_join_points),
    ("02_fill_in", test_02_fill_in),
    ("03_daily_utc", test_03_daily_utc),
    ("04_unique_merchants", test_04_unique_merchants),
]


def main() -> int:
    names = [a.lower() for a in sys.argv[1:]]
    passed = failed = 0
    for name, fn in TESTS:
        if names and not any(n in name.lower() for n in names):
            continue
        conn = sqlite3.connect(":memory:")
        try:
            load_setup(conn)
            fn(conn)
            passed += 1
            print(f"PASS  {name}")
        except Exception as exc:
            failed += 1
            print(f"FAIL  {name}")
            print(f"      {exc}")
            print()
        finally:
            conn.close()
    print()
    print(f"{passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
