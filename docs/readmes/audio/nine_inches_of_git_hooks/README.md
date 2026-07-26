<!-- source: https://github.com/awdemos/nine_inches_of_git_hooks.git sha: ac64cba05822db81d5315b32f0614fd418c9f4db readme: main/README.md -->
# awdemos/nine_inches_of_git_hooks

AI voice clone that screams your commit messages in Nine Inch Nails style

---

# Nine Inches of Git Hooks

An AI voice clone that reads your commit messages in Nine Inch Nails inspired screams for push hooks.

## Features

- 🎸 Aggressive industrial scream synthesis using ChatterBox TTS
- 🎤 Automatically reads commit messages when you push
- 🔊 Industrial-style audio distortion effects
- 📁 Easy installation and setup

## Installation

1. Clone or download this repository
2. Navigate to your git project directory
3. Run the install script:

```bash
bash nine-inches-of-git-hooks/install.sh
```

## Usage

Once installed, the hook will automatically activate when you push commits:

```bash
git commit -m "Fixed the critical bug"
git push
# 🎸 Nine Inches of Git Hooks will scream your commit message! 🎸
```

## How It Works

1. **Git Hook**: Installs a `post-push` hook that triggers after `git push`
2. **Commit Extraction**: Gets the commit messages that were just pushed
3. **Voice Synthesis**: Uses ChatterBox TTS with aggressive settings to simulate industrial screams
4. **Audio Effects**: Applies distortion and reverb for that industrial sound
5. **Playback**: Plays the screaming commit messages through your audio output

## Customization

You can modify the `nine_inches_of_git_hooks.py` script to adjust:
- Speed, pitch, and energy settings
- Distortion effects
- Emotion parameters
- Audio processing

## Requirements

- Python 3.6+
- Git
- Audio output device

## Uninstall

Remove the hook by deleting:
```bash
rm .git/hooks/post-push
```

## License

This project is for entertainment purposes. Use responsibly!
