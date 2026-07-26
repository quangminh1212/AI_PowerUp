<!-- source: https://github.com/PhysicalAI-0/Embodied-Ai-Challenges.git sha: d5d2f4e51f40ad81eb84f4481a138f883f22352d readme: main/README.md -->
# PhysicalAI-0/Embodied-Ai-Challenges

Community-maintained tracker for embodied AI and robotics competitions.

---

# Embodied AI Challenges

A community-maintained tracker for embodied AI, robotics, robot learning, manipulation, navigation, humanoid, and simulation-to-real competitions.

## Currently Active Challenges

The table below is generated from `data/competitions/*.yaml` and only includes challenges with `open` or `ongoing` status. See the website for the full active and past challenge archive.

<!-- BEGIN CHALLENGE_TABLE -->
| Challenge | Year | Venue | Status | Schedule | Deadline | Task Types | Environment | Last Verified |
|---|---:|---|---|---|---|---|---|---|
| [2nd RoCo Challenge](https://rocochallenge.github.io/RoCo-IROS2026/) | 2026 | IROS 2026 | open | multi-stage | 2026-07-12 | manipulation | hybrid | 2026-07-08 |
| [2026 EBiM Challenge](https://ebim-benchmark.github.io/index.html) | 2026 |  | open | multi-stage | 2026-08-03 | manipulation, loco-manipulation | hybrid | 2026-07-08 |
| [2026 BEHAVIOR Challenge](https://behavior.stanford.edu/challenge/index.html) | 2026 |  | open | fixed | 2026-10-16 | loco-manipulation | simulation | 2026-07-08 |
| [RoboChallenge](https://robochallenge.ai/home) | 2026 |  | ongoing | rolling | rolling | manipulation, benchmark | real-world | 2026-07-08 |
<!-- END CHALLENGE_TABLE -->

## Status Values

Use `status` to describe the current lifecycle state of a challenge.

- `upcoming`: announced but not yet open
- `open`: registration or submission is open
- `ongoing`: competition process is active
- `closed`: deadline passed, results not finalized
- `finished`: results or final event completed
- `archived`: historical entry kept for reference

## Schedule Values

Use `schedule_type` to describe the structure of a challenge timeline.

- `fixed`: standard challenge with fixed dates or deadlines
- `multi-stage`: challenge with separate qualification, preliminary, final, or similar stages
- `rolling`: long-running challenge that accepts submissions or evaluations on a rolling basis
- `open-ended`: long-running challenge without a clearly defined end date
- `unknown`: schedule structure is not clear from official sources

## License

Code and documentation are released under the MIT License. Challenge metadata is intended for public community use with attribution to official sources.
