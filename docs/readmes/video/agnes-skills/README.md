<!-- source: https://github.com/ziho7/agnes-skills.git sha: 898e8cd9370c40d24f9d123e3a6f8ad30b71960a readme: main/README.md -->
# ziho7/agnes-skills

Claude Code skills for Agnes AI image and video generation APIs

---

# Agnes Skills

Claude Code skills for the [Agnes AI](https://platform.agnes-ai.com) platform — image and video generation APIs.

## Skills

| Skill | Description |
|-------|-------------|
| [agnes-imagegen](./agnes-imagegen/SKILL.md) | Text-to-image, image-to-image, multi-image composition using Agnes Image 2.0 Flash |
| [agnes-videogen](./agnes-videogen/SKILL.md) | Text-to-video, image-to-video, keyframe interpolation using Agnes Video V2.0 |

## Installation

Copy the skill folders into your Claude Code skills directory:

```bash
# For each skill you want to use:
cp -r agnes-imagegen ~/.claude/skills/
cp -r agnes-videogen ~/.claude/skills/
```

Or symlink them:

```bash
ln -s "$(pwd)/agnes-imagegen" ~/.claude/skills/agnes-imagegen
ln -s "$(pwd)/agnes-videogen" ~/.claude/skills/agnes-videogen
```

## Prerequisites

1. Get an API key from [Agnes AI Platform](https://platform.agnes-ai.com)
2. Set your API key as an environment variable or replace `YOUR_API_KEY` in the skill files

## Usage

Once installed, Claude Code will automatically invoke the skills when you ask to generate images or videos with Agnes.

Examples:
- "Generate an image of a cat on a beach at sunset using agnes"
- "Create a video from this image using agnes"
