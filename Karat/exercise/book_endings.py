"""Choose-your-own-adventure ending exercises."""

from __future__ import annotations

import collections


def find_story_ending(
    endings: list[int], choices: list[list[int]], option: int
) -> int:
    """Follow one fixed option through a choose-your-own-adventure book.

    Reading starts at page 1. Normally the next page is ``page + 1``. Each
    choice is ``[page, option_1, option_2]``. Always select ``option`` (1 or 2).
    Return the ending reached, or ``-1`` if reading enters a loop.

    Complexity variable: ``n`` pages represented by endings and choices.
    """

    endings_set = set(endings)
    choices_dict = collections.defaultdict(list)

    for page, option_1, option_2 in choices:
        choices_dict[page].append(option_1)
        choices_dict[page].append(option_2)

    visited = set()
    page = 1

    while page not in endings_set:
        if page in visited: return -1

        visited.add(page)

        if page in choices_dict:
            page = choices_dict[page][option - 1]
        else:
            page += 1

    return page


def find_good_story_endings(
    good_endings: list[int],
    bad_endings: list[int],
    choices: list[list[int]],
) -> list[int]:
    """Return all good endings reachable from page 1.

    A normal page advances to ``page + 1``; each ``[page, option1, option2]``
    branches to either option. Good and bad endings are terminal. Handle loops
    safely and return reachable good endings sorted.
    """
    good = set(good_endings)
    terminal = good | set(bad_endings)
    choice_by_page = {
        page: (option_one, option_two)
        for page, option_one, option_two in choices
    }
    all_targets = {
        target
        for targets in choice_by_page.values()
        for target in targets
    }
    highest_known = max(
        terminal | set(choice_by_page) | all_targets,
        default=1,
    )
    reachable_good = set()
    visited = set()
    stack = [1]

    while stack:
        page = stack.pop()
        if page in visited:
            continue
        visited.add(page)
        if page in good:
            reachable_good.add(page)
        elif page in terminal or page > highest_known:
            continue
        elif page in choice_by_page:
            stack.extend(choice_by_page[page])
        else:
            stack.append(page + 1)

    return sorted(reachable_good)
