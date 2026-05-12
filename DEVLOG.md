# Development Log – The Torchbearer

**Student Name:** William Ngo
**Student ID:** 130818451

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/8/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I will implement the questions in order from part 1 to part 6, doing the README part first and then implementing the corresponding torchbearer.py question after. The parts that I expect to be difficult is trying to understand the context itself and then matching the implementation to the context. Since I have the idea that this is not a simple Dijkstra's algorithm problem, I think another difficulty will be trying to modify the algorithm to meet this problem's needs. I plan to test by running the provided tests first, and then writing my own test cases that concern edge cases and other worries that I may have.

---

## Entry 2 – [5/9/2026]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

Initially, when I read the problem scenario, I thought that the problem asked us to compute the inter-locations while finding an optimal route in a single run, combining two different algorithms. While doing Part 1 and 2, I realized that the problem actually involved using Dijkstra over each source node, and then finding the optimal order using the computed distances with another algorithm. 

---

## Entry 3 – [5/11/2026]: [Branch and Bound]

As I was implementing _explore(), I recognized that the problem resembled a Branch and Bound algorithm that we went over in class, so it made coding the skeleton easy to write. Writing the inner logic that applied to this problem in specific was the more challenging part, such as realizing how I had to deal with infinite distances, and how I was supposed to iterate through the relics set while removing items at the same time. The solutions themselves were simple but it did take me some time to realize the simple solution because my brain was already fried.  

---

## Entry 4 – [5/11/2026]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

I wouldn't necessarily change anything from how I did this final. I learned from past exams and assignments that I probably should not be procrastinating. As a result, I started earlier, worked on the final part by part every day, and was not overwhelmed. Something that I might improve is maybe writing my functions more cleanly. My code still works but I feel like there are more optimal ways to write the algorithm compared to how I wrote it. 

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 45 minutes |
| Part 2: Precomputation Design | 2 hours |
| Part 3: Algorithm Correctness | 1 hour |
| Part 4: Search Design | 30 minutes |
| Part 5: State and Search Space | 45 minutes |
| Part 6: Pruning | 2 hours |
| Part 7: Implementation | 2 hours |
| README and DEVLOG writing | 4 hours |
| **Total** | 13 hours |
