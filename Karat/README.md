# Karat Python mock interviews

These exercises paraphrase commonly reported Karat question families. They are
practice problems, not a claim that Karat will reuse an exact prompt.

## Interview format

Treat each topic as a separate 45-minute programming round:

1. Read the function documentation in `karat_practice.py` or
   `pdf_practice.py`.
2. Spend 2-3 minutes clarifying assumptions and stating an approach aloud.
3. Implement only that method.
4. Run its focused tests.
5. Explain time and space complexity and add one edge-case test.

Karat commonly precedes coding with about 10 minutes of technical discussion.
Before each mock, pick two prompts from the discussion bank below and answer
them aloud.

## Run

Python 3.10 or newer is sufficient; no third-party packages are required.

```bash
python3 run_tests.py badge
python3 run_tests.py domains
python3 run_tests.py courses
python3 run_tests.py rectangle
python3 run_tests.py story
python3 run_tests.py exit
python3 run_tests.py pdf
python3 run_tests.py all
```

New functions in `pdf_practice.py` and `pdf_more_practice.py` intentionally
raise `NotImplementedError`. See `PDF_QUESTION_CATALOG.md` for the supplied
PDF's complete topic mapping and focused commands.

## Suggested order

| Session | Topic | Main patterns |
|---|---|---|
| 1 | `domains` | strings, hash maps, aggregation |
| 2 | `courses` | maps, sets, pair generation |
| 3 | `badge` | sorting, sliding windows |
| 4 | `rectangle` | matrix scanning |
| 5 | `story` | directed graphs, cycle handling |
| 6 | `exit` | breadth-first search |

## Discussion bank

- Why choose a hash map instead of sorting? Compare complexity and memory.
- How would you process input too large to fit on one machine?
- How would you expose the solution through a backward-compatible API?
- What tests would you add before deploying the code?
- Where would caching help, and how would you invalidate stale entries?
- Which database indexes support the main access pattern?
- How would retries, timeouts, and idempotency protect a third-party call?
- Identify bottlenecks if traffic grows by 100 times.

## What interviewers look for

- Clarifying ambiguous requirements before coding
- A correct simple solution before premature optimization
- Working code with deliberate tests
- Clear narration rather than long silent stretches
- Explicit time and space complexity
- Awareness of malformed input and boundary conditions

Public references used to select the topics:

- Karat candidate experience: https://karat.com/candidate-experience/
- Karat question discussion: https://karat.com/karat-interview-questions-explained/
- Candidate-reported question families: badge access, domain counts, shared
  courses, zero rectangles, story endings, and grid traversal
