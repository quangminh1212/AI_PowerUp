<!-- source: https://github.com/Ayubjon/reasonsplit.git sha: 1b7fcf441a4947cf3aa64fdb2ce51ff73fd8e3f9 readme: main/README.md -->
# Ayubjon/reasonsplit

Split reasoning-model output (DeepSeek R1, QwQ, thinking models) into chain-of-thought and final answer. Zero-dependency CLI + library.

---

# reasonsplit

> Split reasoning-model output into **chain-of-thought** and **final answer** — reliably, with zero dependencies.

Reasoning models like **DeepSeek R1**, **QwQ**, and other "thinking" models wrap their internal monologue in `<think>…</think>` tags before giving the real answer. If you forward that raw text to a user, a log, or another tool, you leak the reasoning — or worse, your JSON parser chokes on it.

`reasonsplit` cleanly separates the two. It is a tiny library **and** a CLI, has **no dependencies**, and handles the messy real-world cases that one-line `string.replace()` hacks miss.

![reasonsplit terminal demo](assets/demo.svg)

## Why not just `replace(/<think>.*<\/think>/, '')`?

Because real model output breaks naive regex:

- **Multiple blocks** scattered through the text.
- **Nested** tags of the same name.
- **Truncated streams** — the closing `</think>` never arrives, so a greedy regex either deletes everything or nothing.
- **Missing opening tag** — several DeepSeek R1 deployments emit only the *closing* `</think>`, with reasoning before it and the answer after.
- **Attributes and odd casing** — `<Think id="1">`.

`reasonsplit` handles all of these with a single-pass, depth-aware scanner, and tells you when the stream was cut off.

## Install

```bash
# Library + CLI
npm install reasonsplit

# Or run the CLI without installing
npx reasonsplit --help
```

Requires Node.js ≥ 18. No other dependencies.

## CLI usage

```bash
# Pipe a reasoning model's output straight through — get the clean answer
ollama run deepseek-r1 "9.11 or 9.9 — which is bigger?" | reasonsplit

# Inspect the hidden chain-of-thought
cat reply.txt | reasonsplit --reasoning

# Get everything as structured JSON
cat reply.txt | reasonsplit --json

# Custom tag names
cat reply.txt | reasonsplit --tags think,thinking,reasoning,scratch
```

| Flag | Description |
|------|-------------|
| `-a, --answer` | Print only the final answer (default) |
| `-r, --reasoning` | Print only the extracted reasoning |
| `-j, --json` | Print the full structured result |
| `-t, --tags <list>` | Comma-separated reasoning tag names |
| `--no-infer` | Don't infer a missing opening tag from a stray `</think>` |
| `-h, --help` | Show help |
| `-v, --version` | Show version |

## Library usage

```js
import split, { stripReasoning, extractReasoning, hasReasoning } from 'reasonsplit';

const raw = '<think>9.11 vs 9.9: compare decimals, 9.90 > 9.11</think>9.9 is larger.';

const { answer, reasoning, blocks, truncated } = split(raw);
// answer    -> "9.9 is larger."
// reasoning -> "9.11 vs 9.9: compare decimals, 9.90 > 9.11"
// blocks    -> [{ tag: 'think', content: '...', closed: true }]
// truncated -> false

stripReasoning(raw);    // "9.9 is larger."
extractReasoning(raw);  // "9.11 vs 9.9: compare decimals, 9.90 > 9.11"
hasReasoning(raw);      // true
```

### `split(text, options)`

Returns `{ answer, reasoning, blocks, truncated }`.

| Option | Default | Description |
|--------|---------|-------------|
| `tags` | `['think','thinking','reasoning','reflection','scratchpad']` | Tag names treated as reasoning (case-insensitive) |
| `inferMissingOpen` | `true` | Treat a stray closing tag as a block that opened at the start of the pending text |

- `answer` — the final answer with all reasoning removed, trimmed.
- `reasoning` — all reasoning blocks joined with a blank line.
- `blocks` — each block: `{ tag, content, closed, inferredOpen? }`.
- `truncated` — `true` when a block was left open (an interrupted stream).

## Handling interrupted streams

When you stream tokens and the connection drops mid-thought, the `<think>` block never closes. `reasonsplit` reports this instead of silently returning garbage:

```js
split('<think>still working through the problem when the stream cut o');
// { answer: '', reasoning: 'still working through the problem when the stream cut o',
//   blocks: [{ tag: 'think', content: '...', closed: false }], truncated: true }
```

Check `truncated` to decide whether to wait for more tokens or retry.

## Use cases

- Strip reasoning before showing answers to end users.
- Log chain-of-thought separately for debugging or evals.
- Clean output before passing it to a JSON parser or another tool.
- Detect truncated streaming responses in a pipeline.

## Development

```bash
npm test   # runs node --test (24 tests, zero dependencies)
```

## License

MIT © 2026 Ayubjon

## Support

This tool is free and open source. If it saved you some time, an optional tip is always welcome (never required):

- **USDT — Ethereum (ERC-20):** `0xad39bdf2df0b8dd6991150fcea0a156150ed19b8`
- Verify on Etherscan: <https://etherscan.io/address/0xad39bdf2df0b8dd6991150fcea0a156150ed19b8>

> Please send only on the **Ethereum (ERC-20)** network. Thank you! 🙏
