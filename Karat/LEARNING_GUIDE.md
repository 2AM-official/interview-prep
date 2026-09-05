# Karat Coding Interview Learning Guide

This guide organizes the supplied Karat practice questions by topic. Use it
to study the problem statement, explain an approach aloud, implement the
function, run focused tests, and review complexity.

## Project layout

- Implementations: `Karat/exercise/`
- Tests: `Karat/test/`
- Focused test runner: `Karat/run_tests.py`

Run one complete question family from the repository root:

```bash
python3 Karat/run_tests.py academic-schedule
python3 Karat/run_tests.py domain-analysis
python3 Karat/run_tests.py snake-exits
```

A failing `NotImplementedError` means that part is still a starter exercise.

## Recommended practice routine

For each question:

1. Restate the inputs and expected output in your own words.
2. Work through one sample manually.
3. State the data structures you plan to use.
4. Implement the simplest correct solution.
5. Run the focused tests.
6. Add an edge-case test.
7. Explain time and space complexity.
8. Discuss how the solution would change for much larger input.

## Interview checklist

Before coding, clarify:

- Can the input be empty?
- Can records be duplicated?
- Is output order important?
- Are identifiers strings or numbers?
- Can a graph contain cycles?
- Can there be multiple valid answers?
- Should malformed input be rejected or assumed valid?

While coding:

- Use descriptive names.
- Separate input parsing from the main algorithm.
- State invariants for loops and recursive functions.
- Test the smallest valid input and a no-result case.

## 1. Academic Schedule

Files:

- `exercise/academic_schedule.py`
- `test/test_academic_schedule.py`

Run:

```bash
python3 Karat/run_tests.py academic-schedule
```

Part 1 asks for shared courses for every pair of students. The main patterns
are hash maps, sets, pair generation, and set intersection.

Part 2 asks for midpoint courses on every root-to-leaf curriculum track. The
main patterns are directed graphs, root detection, depth-first search,
backtracking, and path indexing.

## 2. Book Endings

Files:

- `exercise/book_endings.py`
- `test/test_book_endings.py`

Run:

```bash
python3 Karat/run_tests.py book-endings
```

Part 1 follows one fixed choice through a book and must detect loops. Part 2
explores every choice and returns all reachable good endings. Practice graph
traversal, terminal states, and visited sets.

## 3. Camping

Files:

- `exercise/camping.py`
- `test/test_camping.py`

Run:

```bash
python3 Karat/run_tests.py camping
```

Part 1 counts department visits saved by grouping a shopping list. Practice
mapping products to departments, counting contiguous runs, and distinct sets.

Part 2 assigns passengers to cars based on arrival time. Practice graph route
traversal, cumulative time, and comparing candidates.

## 4. Catch Cheaters

Files:

- `exercise/catch_cheaters.py`
- `test/test_catch_cheaters.py`

Run:

```bash
python3 Karat/run_tests.py catch-cheaters
```

Part 1 finds a word that can be formed from available letters. Practice
frequency counters and repeated-character handling.

Parts 2 and 3 locate words in a grid using right/down paths. The final part
must assign non-overlapping paths to several words. Practice DFS,
backtracking, coordinate paths, and global state.

## 5. Cipher

Files:

- `exercise/cipher.py`
- `test/test_cipher.py`

Run:

```bash
python3 Karat/run_tests.py cipher
```

The parts cover matrix transposition, keyed substitution, and ambiguous
numeric decryption. Practice indexing, character mapping, case preservation,
tokenization, and backtracking.

## 6. Delivery Bot

Files:

- `exercise/delivery_bot.py`
- `test/test_delivery_bot.py`

Run:

```bash
python3 Karat/run_tests.py delivery-bot
```

Part 1 maps graph origins to reachable terminal destinations. Part 2 checks
which robots can be built from available parts. Practice graph traversal,
root/leaf detection, memoization, and subset checks.

## 7. Domain Analysis

Files:

- `exercise/domain_analysis.py`
- `test/test_domain_analysis.py`

Run:

```bash
python3 Karat/run_tests.py domain-analysis
```

Question 1 aggregates visits for full domains and parent domains. Practice
string parsing and hash-map aggregation.

Question 2 finds the longest contiguous sequence shared by two browsing
histories. This is the longest common substring pattern and uses dynamic
programming.

Question 3 attributes ad clicks to purchasing users. Practice parsing,
joining records through IDs and IPs, and grouped counting.

## 8. Generation Graph

Files:

- `exercise/generation_graph.py`
- `test/test_generation_graph.py`

Run:

```bash
python3 Karat/run_tests.py generation-graph
```

The parts find nodes with zero or one parent, determine whether two nodes
share an ancestor, and find an earliest ancestor. Practice parent adjacency
maps, indegree counting, DFS/BFS, and ancestor depth.

## 9. Mini Game

Files:

- `exercise/mini_game.py`
- `test/test_mini_game.py`

Run:

```bash
python3 Karat/run_tests.py mini-game
```

Part 1 validates hands made of identical triples plus exactly one pair.
Frequency counts and modulo arithmetic are central.

Part 2 also allows runs. Practice recursive search, consuming/restoring
counts, and trying alternative valid groupings.

## 10. Most Powerful Card

Files:

- `exercise/most_powerful_card.py`
- `test/test_most_powerful_card.py`

Run:

```bash
python3 Karat/run_tests.py most-powerful-card
```

Matchup pairs describe which card defeats another. Practice directed graphs,
transitive reachability, and identifying a unique winner.

## 11. Movie Recommendation

Files:

- `exercise/movie_recommendation.py`
- `test/test_movie_recommendation.py`

Run:

```bash
python3 Karat/run_tests.py movie-recommendation
```

Part 1 groups users by follow count. Part 2 recommends movies through social
connections. Practice grouping, adjacency sets, deduplication, and excluding
already-seen items.

## 12. Passage Tracker

Files:

- `exercise/passage_tracker.py`
- `test/test_passage_tracker.py`

Run:

```bash
python3 Karat/run_tests.py passage-tracker
```

The parts parse access logs, count journeys, and detect speeding. Practice
structured parsing, grouping events by entity, sorting by time, and deriving
metrics from consecutive events.

## 13. Picking Restaurant

Files:

- `exercise/picking_restaurant.py`
- `test/test_picking_restaurant.py`

Run:

```bash
python3 Karat/run_tests.py picking-restaurant
```

The question recommends a restaurant through mutual friends. Practice graph
neighborhoods, intersections, candidate scoring, and deterministic
tie-breaking.

## 14. Puzzle Checker

Files:

- `exercise/puzzle_checker.py`
- `test/test_puzzle_checker.py`

Run:

```bash
python3 Karat/run_tests.py puzzle-checker
```

Part 1 verifies that every row and column contains exactly `1` through `N`.
Practice matrix validation, sets, and careful dimension checks.

Part 2 validates nonogram clues. Practice scanning rows/columns, converting
filled cells into run lengths, and comparing those runs with clues.

## 15. Resource Access Log

Files:

- `exercise/resource_access_log.py`
- `test/test_resource_access_log.py`

Run:

```bash
python3 Karat/run_tests.py resource-access-log
```

The questions calculate each user's access range, find the busiest
five-minute resource window, and build transition probabilities. Practice
time conversion, sorting, sliding windows, nested counters, and probability
normalization.

## 16. Snake Exits

Files:

- `exercise/snake_exits.py`
- `test/test_snake_exits.py`

Run:

```bash
python3 Karat/run_tests.py snake-exits
```

Part 1 finds rows and columns with no blocked cells. Practice matrix scanning.

Part 2 finds the nearest reachable boundary exit. Practice BFS and shortest
paths in an unweighted grid.

Part 3 counts connected nest entrances. Practice connected components,
boundary detection, and DFS/BFS.

## 17. Snowy Mountain

Files:

- `exercise/snowy_mountain.py`
- `test/test_snowy_mountain.py`

Run:

```bash
python3 Karat/run_tests.py snowy-mountain
```

The question chooses the cheapest day to cross changing terrain. Practice
evaluating candidate days, path costs, and dynamic programming or shortest
path reasoning.

## 18. Thrilling Teleporters

Files:

- `exercise/thrilling_teleporters.py`
- `test/test_thrilling_teleporters.py`

Run:

```bash
python3 Karat/run_tests.py thrilling-teleporters
```

Part 1 returns unique possible destinations after one die roll. Practice
simulation, lookup maps, deduplication, and preserving order.

Part 2 checks whether the board is finishable. Practice graph reachability,
cycle detection, and reasoning about every possible move.

## 19. Tomb Raider

Files:

- `exercise/tomb_raider.py`
- `test/test_tomb_raider.py`

Run:

```bash
python3 Karat/run_tests.py tomb-raider
```

The question calculates the minimum distance between spheres and holes.
Practice three-dimensional Euclidean distance, radii, and clamping negative
surface distances to zero.

## 20. Treasure Room

Files:

- `exercise/treasure_room.py`
- `test/test_treasure_room.py`

Run:

```bash
python3 Karat/run_tests.py treasure-room
```

Question 1 filters rooms that lead to treasure under graph constraints.
Question 2 finds a route with the fewest paid instructions. Practice reverse
graphs, reachability, weighted shortest paths, and Dijkstra's algorithm.

## 21. Writing Application

Files:

- `exercise/writing_application.py`
- `test/test_writing_application.py`

Run:

```bash
python3 Karat/run_tests.py writing-application
```

Part 1 greedily wraps words within a line width. Part 2 reflows and justifies
text. Practice tokenization, greedy packing, distributing spaces, and edge
cases such as one-word lines.

## Pattern review

Hash maps and sets:

- Academic Schedule Part 1
- Domain Analysis Question 1
- Delivery Bot Part 2
- Mini Game

Graph traversal:

- Academic Schedule Part 2
- Book Endings
- Delivery Bot Part 1
- Generation Graph
- Snake Exits
- Treasure Room

Dynamic programming and backtracking:

- Catch Cheaters
- Cipher Part 3
- Domain Analysis Question 2
- Mini Game Part 2
- Snowy Mountain

Sorting and sliding windows:

- Passage Tracker
- Resource Access Log

Matrix and grid processing:

- Catch Cheaters
- Puzzle Checker
- Snake Exits
- Cipher Part 1

## Final review questions

For every completed solution, be ready to answer:

1. Why is your chosen data structure appropriate?
2. What are the time and space complexities?
3. Which input causes the worst-case runtime?
4. What edge cases did you test?
5. How would you handle malformed or extremely large input?
6. Could recursion exceed the call-stack limit?
7. Is output deterministic when sets or dictionaries are used?
