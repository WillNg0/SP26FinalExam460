# The Torchbearer

**Student Name:** William Ngo
**Student ID:** 130818451
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run from S is not enough because it would only find the shortest path from one location to all other locations. It cannot decide which order to visit the relic chambers that results in the least total fuel cost. 

- **What decision remains after all inter-location costs are known:**
  After all the inter-location costs are known, the least fuel-cost route between relic chambers must be decided.

- **Why this requires a search over orders (one sentence):**
  This requires a search over orders because the least-cost route must be determined among different valid relic chamber routes. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| - Entrance node | Node where the Torchbearer starts |
| - Relic chamber node | Compute least cost to every other location after reaching a chamber |
| - Exit node | Compute the lowest cost for each location to reach the exit |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Dungeon Locations |
| What the values represent | Cheapest distance from source node to every other location |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | The hash function allows for constant time look up for each dungeon |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** Number of runs equal k plus the start node and exit node, which is O(k)
- **Cost per run:** O(m log n)
- **Total complexity:** O(k) * O(m log n) = O(k*m log n)
- **Justification (one line):** Since the cost per run is O(m log n) and we have to run Dijkstra O(k) times, we have to multiply their time complexities for the total complexity. 

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  For every node v that has already been finalized in S, dist[v] gives the least cost path from x to v and no better paths exist.

- **For nodes not yet finalized (not in S):**
  For the nodes u that have not been finalized in S, dist[u] gives the current least cost path from x to u based on the finalized nodes in S. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  At the start, the source node is initialized with distance 0 and no other nodes have been processed yet, so their distances are initialized to infinity. 

- **Maintenance : why finalizing the min-dist node is always correct:**
  The graph consists of nonnegative edge weights, meaning that a better path cannot be discovered after a path has been finalized with the minimum distance.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The shortest path from the source node to all reachable nodes have been discovered and finalized. 

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Since Dijkstra produces the correct shortest distance from the source node, an optimal route can be decided by seeing which route produces the minimum cost among different valid routes. 

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Picking the cheapest next node available
- **Counter-example setup:** 
| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 2   | 3   | 1   | --  |
| B         | --  | 1   | 100 | 2   |
| C         | 3   | --  | 3   | 2   |
| D         | 3   | 2   | --  | 100 |
- **What greedy picks:** S -> D -> C -> B -> T &nbsp; total fuel = 1 + 2 + 3 + 2 = **8**
- **What optimal picks:** S -> D -> B -> C -> T &nbsp; total fuel = 1 + 3 + 1 + 2 = **7**
- **Why greedy loses:** Greedy chooses the cheapest option available, but does not consider how its decisions can affect later paths. Later paths can be cheaper than current cheapest path. 

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore the order to visit the relic chambers that results in the minimum total fuel cost. 

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | curr_loc | string | Current location that the Torchbearer is at |
| Relics already collected | coll_relics | set | Relics that have been collected already |
| Fuel cost so far | fuel_so_far | int | The total fuel cost used so far|

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1) average case |
| Operation: mark a relic as collected | Time complexity: O(1) average case |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) average case |
| Why this structure fits | Allows the Torchbearer to avoid revisiting relics and backtrack in near constant time |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** O(k!)
- **Why:** The algorithm may have to consider every permutation of relic chambers to visit for the minimum total fuel cost.  

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** Cost of the best route so far 
- **When it is used:** When the explored path is worse than the current best
- **What it allows the algorithm to skip:** Routes that are worse than current best 

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The current location, total fuel cost at that point, and which relics have been visited
- **What the lower bound accounts for:** The minimum possible total cost to continue exploring from the current state
- **Why it never overestimates:** It is computed using the cost that the torchbearer has used so far and the lowest available cost available going forward

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- The best-so-far is an actual cost for a complete and valid route the Torchbearer has explored.
- If the current branch's lower bound is greater than the best-so-far, the current branch can never beat it, so pruning is safe. 

---

## References

> Bullet list. If none beyond lecture notes, write that.

- https://wiki.python.org/moin/TimeComplexity 
