"""Reference solutions for choose-your-own-adventure endings."""

from __future__ import annotations


def find_story_ending(
    endings: list[int], choices: list[list[int]], option: int
) -> int:
    """Follow a fixed choice option and return its ending, or -1 on a loop."""
    terminal_pages = set(endings)
    choice_by_page = {
        page: (option_one, option_two)
        for page, option_one, option_two in choices
    }
    visited: set[int] = set()
    page = 1

    while page not in terminal_pages:
        if page in visited:
            return -1
        visited.add(page)
        page = choice_by_page.get(page, (page + 1, page + 1))[option - 1]
    return page


def find_good_story_endings(
    good_endings: list[int],
    bad_endings: list[int],
    choices: list[list[int]],
) -> list[int]:
    """Return all good endings reachable from page 1, safely handling loops."""
    good = set(good_endings)
    terminal = good | set(bad_endings)
    choice_by_page = {
        page: (option_one, option_two)
        for page, option_one, option_two in choices
    }
    highest_known_page = max(
        terminal | set(choice_by_page) | {target for pair in choice_by_page.values() for target in pair},
        default=1,
    )
    reachable_good: set[int] = set()
    visited: set[int] = set()
    stack = [1]

    while stack:
        page = stack.pop()
        if page in visited:
            continue
        visited.add(page)
        if page in good:
            reachable_good.add(page)
        elif page in terminal or page > highest_known_page:
            continue
        elif page in choice_by_page:
            stack.extend(choice_by_page[page])
        else:
            stack.append(page + 1)

    return sorted(reachable_good)
