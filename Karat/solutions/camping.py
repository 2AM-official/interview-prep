"""Reference solutions for the camping-trip exercises."""

from __future__ import annotations


def shopping_savings(
    products: list[list[str]], shopping_list: list[str]
) -> int:
    """Return department visits saved by grouping the shopping list."""
    if not shopping_list:
        return 0

    department_by_product = {
        product: department for product, department in products
    }
    departments = [
        department_by_product[product] for product in shopping_list
    ]
    original_visits = 1 + sum(
        current != previous
        for previous, current in zip(departments, departments[1:])
    )
    grouped_visits = len(set(departments))
    return original_visits - grouped_visits


def carpool(
    roads: list[list[str]],
    starts: list[str],
    people: list[list[str]],
) -> list[list[str]]:
    """Assign each reachable person to the first car reaching their location."""
    next_road = {
        origin: (destination, int(minutes))
        for origin, destination, minutes in roads
    }

    arrival_times: list[dict[str, int]] = []
    for start in starts:
        times = {start: 0}
        location = start
        elapsed = 0
        visited = {start}
        while location in next_road:
            destination, minutes = next_road[location]
            if destination in visited:
                break
            elapsed += minutes
            times[destination] = elapsed
            visited.add(destination)
            location = destination
        arrival_times.append(times)

    assignments = [[] for _ in starts]
    for person, location in people:
        candidates = [
            (times[location], car_index)
            for car_index, times in enumerate(arrival_times)
            if location in times
        ]
        if candidates:
            _arrival, car_index = min(candidates)
            assignments[car_index].append(person)
    return assignments
