"""Solution tests for the domain-analysis exercises."""

import unittest

from solutions.domain_analysis import (
    ad_conversion_rates,
    aggregate_domain_visits,
    longest_contiguous_history,
)


class DomainVisitsTest(unittest.TestCase):
    def test_aggregates_all_parent_domains(self):
        visits = [
            "900 discuss.leetcode.com",
            "50 leetcode.com",
            "1 com",
            "5 mail.google.com",
        ]
        self.assertEqual(
            {
                "discuss.leetcode.com": 900,
                "leetcode.com": 950,
                "mail.google.com": 5,
                "google.com": 5,
                "com": 956,
            },
            aggregate_domain_visits(visits),
        )

    def test_supports_single_component_domain(self):
        self.assertEqual({"localhost": 7}, aggregate_domain_visits(["7 localhost"]))

    def test_supports_original_pdf_comma_format(self):
        self.assertEqual(
            {"mail.yahoo.com": 60, "yahoo.com": 60, "com": 60},
            aggregate_domain_visits(["60,mail.yahoo.com"]),
        )

    def test_empty_input(self):
        self.assertEqual({}, aggregate_domain_visits([]))


class ContiguousHistoryTest(unittest.TestCase):
    def test_finds_longest_shared_run(self):
        first = [
            "/start", "/green", "/blue", "/pink", "/register", "/orange",
            "/one/two",
        ]
        second = ["/start", "/pink", "/register", "/orange", "/red", "a"]
        self.assertEqual(
            ["/pink", "/register", "/orange"],
            longest_contiguous_history(first, second),
        )

    def test_empty_and_single_item_matches(self):
        self.assertEqual(
            [], longest_contiguous_history(["/start"], ["/different"])
        )
        self.assertEqual(["a"], longest_contiguous_history(["a"], ["x", "a"]))


class AdConversionTest(unittest.TestCase):
    def test_counts_purchasing_clicks_and_all_clicks(self):
        purchasers = ["3123122444", "234111110", "8321125440", "99911063"]
        clicks = [
            "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
            "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
            "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
            "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
            "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
            "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
        ]
        user_ips = [
            "2339985511,122.121.0.155", "234111110,122.121.0.1",
            "3123122444,92.130.6.145", "8321125440,82.1.106.8",
            "99911063,92.130.6.144",
        ]
        self.assertEqual(
            {
                "2017 Pet Mittens": (1, 2),
                "The Best Hollywood Coats": (0, 1),
                "Buy wool coats for your pets": (3, 3),
            },
            ad_conversion_rates(purchasers, clicks, user_ips),
        )


if __name__ == "__main__":
    unittest.main()
