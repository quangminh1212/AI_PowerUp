<!-- source: https://github.com/aaronrussell/shifts.git sha: 44b750f38ae383f535fd5a92a2f956390a322066 readme: main/README.md -->
# aaronrussell/shifts

Elixir framework for composing autonomous AI agent workflows.

---

# Shifts

![Hex.pm](https://img.shields.io/hexpm/v/shifts?color=informational)
![License](https://img.shields.io/github/license/lebrunel/shifts?color=informational)
![Build Status](https://img.shields.io/github/actions/workflow/status/lebrunel/shifts/elixir.yml?branch=main)

Shifts is a framework for composing autonomous **agent** workflows, using a mixture of LLM backends.

- 🤖 **Automate your chores** - have AI agents handle the mundane so you can focus on the things you care about.
- 💪🏻 **Agents with superpowers** - create tools, so your agents can interact with the Web or internal APIs and systems.
- 🧩 **Flexible and adaptable** - easily compose and modify workflows to suit your specific needs.
- 🤗 **Delightful simplicity** - pipe instructions together using just plain English and intuitive APIs.
- 🎨 **Mix and match** - Plug into different LLMs even within the same workflow so you are always using the right tool for job.

### Current dev status

| Version   | Stability                                                    | Status                  |
| --------- | ------------------------------------------------------------ | ----------------------- |
| `0.0.x`   | For the brave and adventurous - expect breaking changes.     | **👈🏻 We are here!** |
| `0.x.0`   | Focus on better docs with less frequent breaking changes.    |                         |
| `1.0.0` + | 🚀 Launched. Great docs, great dev experience, stable APIs. |                         |

### Currently supported LLMs

- Anthropic / Claude 3 - **Recommended**
- Ollama - Hermes Pro

## Installation

The package can be installed by adding `shifts` to your list of dependencies in `mix.exs`.

```elixir
def deps do
  [
    {:shifts, "~> 0.0.2"}
  ]
end
```

Documentation to follow...

## Licence

This package is open source and released under the [Apache-2 Licence](https://github.com/lebrunel/shifts/blob/master/LICENSE).

© Copyright 2024 [Push Code Ltd](https://www.pushcode.com/).
