"""Reference solutions for the domain-analysis exercises."""

from __future__ import annotations

from collections import defaultdict


def aggregate_domain_visits(visits: list[str]) -> dict[str, int]:
    """Aggregate visits for each domain and each of its parent domains."""
    totals: dict[str, int] = defaultdict(int)
    for visit in visits:
        count_text, domain = visit.replace(",", " ", 1).split(maxsplit=1)
        components = domain.split(".")
        for index in range(len(components)):
            totals[".".join(components[index:])] += int(count_text)
    return dict(totals)


def longest_contiguous_history(first: list[str], second: list[str]) -> list[str]:
    """Return the longest contiguous sequence shared by both histories.

    Equal-length matches are resolved in favor of the earliest start in
    ``first``.
    """
    previous = [0] * (len(second) + 1)
    best_length = 0
    best_start = 0

    for first_index, first_page in enumerate(first, start=1):
        current = [0] * (len(second) + 1)
        for second_index, second_page in enumerate(second, start=1):
            if first_page == second_page:
                current[second_index] = previous[second_index - 1] + 1
                length = current[second_index]
                start = first_index - length
                if length > best_length or (
                    length == best_length and start < best_start
                ):
                    best_length = length
                    best_start = start
        previous = current

    return first[best_start : best_start + best_length]


def ad_conversion_rates(
    completed_user_ids: list[str],
    ad_clicks: list[str],
    user_ips: list[str],
) -> dict[str, tuple[int, int]]:
    """Return each ad's purchasing-user click count and total click count."""
    purchasers = set(completed_user_ids)
    purchaser_ips = {
        ip
        for user_id, ip in (entry.split(",", 1) for entry in user_ips)
        if user_id in purchasers
    }
    counts: dict[str, list[int]] = {}

    for click in ad_clicks:
        ip, _timestamp, ad = click.split(",", 2)
        purchasing, total = counts.setdefault(ad, [0, 0])
        counts[ad] = [purchasing + (ip in purchaser_ips), total + 1]

    return {ad: (purchasing, total) for ad, (purchasing, total) in counts.items()}
