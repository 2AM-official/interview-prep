"""Camping-trip interview exercises."""

from __future__ import annotations

import collections


def shopping_savings(
    products: list[list[str]], shopping_list: list[str]
) -> int:
    """Return department visits saved by grouping items by department.

    ``products`` contains ``[product, department]`` pairs. The original visit
    count is the number of contiguous department runs in ``shopping_list``.
    The optimized count is the number of distinct departments represented.

    Complexity variable: ``n`` products.
    """
    grouped = set()
    regular_visit = 0

    product_map = collections.defaultdict(str)

    for product, department in products:
        product_map[product] = department
    
    prev = ""
    
    for product in shopping_list:
        department = product_map[product]
        grouped.add(department)

        if regular_visit == 0:
            prev = department
            regular_visit += 1
        else:
            if department == prev:
                continue
            else:
                prev = department
                regular_visit += 1
        
    
    return regular_visit - len(grouped)


def carpool(
    roads: list[list[str]],
    starts: list[str],
    people: list[list[str]],
) -> list[list[str]]:
    """Assign each person to the first of two cars reaching their location.

    Roads are ``[origin, destination, minutes]`` in an acyclic graph where
    each origin has at most one outgoing road. Cars leave simultaneously.
    A tie may be assigned to either car. Preserve car order from ``starts``
    and person order from ``people``. Omit unreachable people.
    """
    next_road = {}
    for origin, destination, minutes in roads:
        next_road[origin] = (destination, int(minutes))

    arrival_times = []
    for start in starts:
        times = {start: 0}
        location = start
        elapsed = 0

        while location in next_road:
            destination, minutes = next_road[location]
            if destination in times:
                break
            elapsed += minutes
            times[destination] = elapsed
            location = destination

        arrival_times.append(times)

    assignments = [[] for _ in starts]
    for person, location in people:
        best_car = None
        best_time = None

        for car_index, times in enumerate(arrival_times):
            if location not in times:
                continue
            arrival = times[location]
            if best_time is None or arrival < best_time:
                best_time = arrival
                best_car = car_index

        if best_car is not None:
            assignments[best_car].append(person)

    return assignments
