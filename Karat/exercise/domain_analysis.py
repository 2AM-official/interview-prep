"""Domain-analysis interview exercises."""

from __future__ import annotations

import collections


def aggregate_domain_visits(visits: list[str]) -> dict[str, int]:
    """Aggregate visits for each domain and all of its parent domains.

    Each input has the form ``"<count> <domain>"`` or the PDF's original
    ``"<count>,<domain>"``. For example, ``"900 discuss.leetcode.com"`` adds
    900 visits to
    ``discuss.leetcode.com``, ``leetcode.com``, and ``com``.

    State complexity in terms of n entries and p total domain components.
    """
    result = collections.defaultdict(int)
    for visit in visits:
        count, domain = visit.replace(",", " ", 1).split()
        count = int(count)
        domains = domain.split('.')
        for i in range(len(domains)):
            result['.'.join(domains[i:])] += count
    return result


def longest_contiguous_history(first: list[str], second: list[str]) -> list[str]:
    """Return the longest contiguous sequence shared by two browsing histories.

    If several sequences have the same maximum length, return the one that
    starts earliest in ``first``. Return an empty list when there is no match.

    Complexity variables: ``n`` and ``m`` history lengths.
    """
    
    dp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

    best_length = 0
    best_start = 0

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                current_length = dp[i][j]
                current_start = i - current_length

                if (
                    current_length > best_length
                    or (
                        current_length == best_length
                        and current_start < best_start
                    )
                ):
                    best_length = current_length
                    best_start = current_start
    
    return first[best_start : best_start + best_length]


def ad_conversion_rates(
    completed_user_ids: list[str],
    ad_clicks: list[str],
    user_ips: list[str],
) -> dict[str, tuple[int, int]]:
    """Return ``ad -> (purchasing-user clicks, total clicks)``.

    Click strings are ``"IP,timestamp,ad text"`` and user-IP strings are
    ``"user ID,IP"``. Unknown IPs count only toward total clicks.
    """
    purchasers = set(completed_user_ids)
    purchaser_ips = set()
    for entry in user_ips:
        user_id, ip = entry.split(",", 1)
        if user_id in purchasers:
            purchaser_ips.add(ip)

    counts = {}
    for click in ad_clicks:
        ip, _timestamp, ad = click.split(",", 2)
        purchasing, total = counts.get(ad, (0, 0))
        if ip in purchaser_ips:
            purchasing += 1
        counts[ad] = (purchasing, total + 1)
    return counts
