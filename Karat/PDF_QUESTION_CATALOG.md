# Supplied PDF question catalog

This catalog summarizes `Karat_-_Coding_Questions.pdf`. Prompts in the runnable
files are paraphrased and normalized where the PDF extraction was incomplete.

## Per-question files

Each question family now has its own implementation file and matching test
file. Implementations are under `exercise/`, and tests are under `test/`.
For example, Academic Schedule uses `exercise/academic_schedule.py` and
`test/test_academic_schedule.py`.

The other families follow the same pattern:

- `domain_analysis`, `snake_exits`, `book_endings`, `camping`
- `catch_cheaters`, `mini_game`, `puzzle_checker`
- `thrilling_teleporters`, `writing_application`, `cipher`
- `delivery_bot`, `generation_graph`, `movie_recommendation`
- `passage_tracker`, `most_powerful_card`, `picking_restaurant`
- `resource_access_log`, `snowy_mountain`, `tomb_raider`, `treasure_room`

Run a complete family with its hyphenated topic name:

```bash
python3 Karat/run_tests.py academic-schedule
python3 Karat/run_tests.py domain-analysis
python3 Karat/run_tests.py snake-exits
```

The original combined practice modules remain available for reference.

## Runnable in `karat_practice.py`

- Academic Schedule, Part 1: shared courses — `courses`
- Domain Analysis, Question 1: aggregate subdomain visits — `domains`
- Snake Exits, Part 2: nearest reachable exit — `exit`

## Runnable in `pdf_practice.py`

- Academic Schedule, Part 2: curriculum path midpoints — `midpoints`
- Book Endings, Part 1: fixed-option ending or loop — `ending`
- Camping, Part 1: shopping department visits saved — `shopping`
- Catch Cheaters, Part 1: scrambled word in available letters — `scramble`
- Domain Analysis, Question 2: longest contiguous browsing history — `history`
- Mini Game, Part 1: triples plus exactly one pair — `hand`
- Puzzle Checker, Part 1: valid N-by-N matrix — `matrix`
- Snake Exits, Part 1: completely passable rows and columns — `lanes`
- Thrilling Teleporters, Part 1: one-roll destinations — `teleporters`
- Writing Application, Part 1: greedy word wrapping — `wrap`

Run one from the repository root:

```bash
python3 Karat/run_tests.py midpoints
python3 Karat/run_tests.py ending
python3 Karat/run_tests.py shopping
python3 Karat/run_tests.py scramble
python3 Karat/run_tests.py history
python3 Karat/run_tests.py hand
python3 Karat/run_tests.py matrix
python3 Karat/run_tests.py lanes
python3 Karat/run_tests.py teleporters
python3 Karat/run_tests.py wrap
```

Run every new PDF exercise with:

```bash
python3 Karat/run_tests.py pdf
```

## Remaining parts runnable in `pdf_more_practice.py`

- Book Endings, Part 2: reachable good endings — `good-endings`
- Camping, Part 2: assign passengers to the first arriving car — `carpool`
- Catch Cheaters, Part 2: locate a word in a grid — `word-location`
- Catch Cheaters, Part 3: locate disjoint words — `word-locations`
- Cipher, Part 1: matrix transposition — `transpose`
- Cipher, Part 2: keyed substitution — `encrypt`
- Cipher, Part 3: ambiguous numeric decryption — `decrypt`
- Delivery Bot, Part 1: graph origins and terminal destinations — `delivery`
- Delivery Bot, Part 2: buildable robots — `robots`
- Domain Analysis, Question 3: ad conversion attribution — `ads`
- Generation Graph, Part 1: zero/one-parent nodes — `parents`
- Generation Graph, Part 2: common ancestors — `ancestor`
- Generation Graph, Part 3: earliest ancestor — `earliest`
- Mini Game, Part 2: hands containing triples and runs — `advanced-hand`
- Most Powerful Card: transitive matchup winner — `card`
- Movie Recommendation, Part 1: follow-count grouping — `follows`
- Movie Recommendation, Part 2: movie recommendations — `movies`
- Passage Tracker, Part 1: log parsing — `parse-log`
- Passage Tracker, Part 2: journey counting — `journeys`
- Passage Tracker, Part 3: speeding detection — `speeders`
- Picking Restaurant: mutual-friend recommendation — `restaurant`
- Puzzle Checker, Part 2: nonogram validation — `nonogram`
- Resource Access Log, Question 1: user access ranges — `access`
- Resource Access Log, Question 2: busiest five-minute window — `busiest`
- Resource Access Log, Question 3: transition probabilities — `transitions`
- Snake Exits, Part 3: connected nest entrances — `nests`
- Snowy Mountain: cheapest crossing day — `snow`
- Thrilling Teleporters, Part 2: board reachability — `finishable`
- Tomb Raider: sphere-to-hole distance — `spheres`
- Treasure Room, Question 1: filter treasure-leading rooms — `treasure-rooms`
- Treasure Room, Question 2: paid-instruction shortest path — `treasure-path`
- Writing Application, Part 2: reflow and justification — `justify`

Every distinct PDF question is now represented once. Where the source was
truncated or allowed several outputs, the function docstring states the
deterministic assumption used by its tests.
