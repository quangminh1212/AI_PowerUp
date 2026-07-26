<!-- source: https://github.com/paddo/flutter-auto-reload.git sha: c61e55876f70037186566fda52f281ceb601cc5b readme: main/README.md -->
# paddo/flutter-auto-reload

Automatic hot reload for Flutter development without an IDE - perfect for vim, terminal workflows, and AI coding assistants

---

# Flutter Auto-Reload Tools

Automatic hot reload for Flutter development without an IDE. Perfect for terminal-based workflows, vim/helix users, and AI coding assistants.

## Features

- 🔥 **Automatic Hot Reload** - Instantly reloads when `.dart` files change
- 🔄 **Smart Hot Restart** - Automatically restarts when `pubspec.yaml` changes
- ⌨️ **Manual Control** - Still supports manual reload (r) and restart (R)
- 🖥️ **IDE-Free** - Works with any text editor that saves files
- 🚀 **Zero Configuration** - Just run and code
- 📱 **Multi-Device Support** - Run multiple instances for different devices

## Quick Start

```bash
# Clone this repository
git clone https://github.com/paddo/flutter-auto-reload.git

# Copy tools to your Flutter project
cp -r flutter-auto-reload/* your-flutter-app/tools/

# Run your Flutter app with auto-reload
cd your-flutter-app
./tools/run_with_auto_reload.sh
```

## Installation Options

### Option 1: Direct Download (Recommended)

Download the scripts directly to your Flutter project:

```bash
# Create tools directory in your Flutter project
mkdir -p tools
cd tools

# Download the scripts
curl -O https://raw.githubusercontent.com/paddo/flutter-auto-reload/main/run_with_auto_reload.sh
curl -O https://raw.githubusercontent.com/paddo/flutter-auto-reload/main/auto_reload_watcher.dart
curl -O https://raw.githubusercontent.com/paddo/flutter-auto-reload/main/auto_reload.dart

# Make the shell script executable
chmod +x run_with_auto_reload.sh
```

### Option 2: Git Submodule

Add as a submodule to your project:

```bash
git submodule add https://github.com/paddo/flutter-auto-reload.git tools/auto-reload
```

## Usage

### Basic Usage

The simplest way - just run the script from your Flutter project root:

```bash
./tools/run_with_auto_reload.sh
```

This will:
- Start Flutter in debug mode with hot reload enabled
- Watch all `.dart` files in `lib/` for changes
- Automatically trigger hot reload when files are saved
- Automatically trigger hot restart when `pubspec.yaml` changes

### With Specific Device

Run on a specific device or simulator:

```bash
# List available devices
flutter devices

# Run on specific device (use device ID from the list)
./tools/run_with_auto_reload.sh 00008130-000E354424C1401C

# Run on Chrome
./tools/run_with_auto_reload.sh chrome
```

### Manual Two-Terminal Setup

If you prefer to run Flutter and the watcher separately:

**Terminal 1 - Start Flutter:**
```bash
flutter run --hot --pid-file=/tmp/flutter-app.pid
```

**Terminal 2 - Start Watcher:**
```bash
dart tools/auto_reload_watcher.dart
```

### All-in-One Dart Script

For a single-process solution (note: may have terminal I/O limitations):

```bash
dart tools/auto_reload.dart
```

## How It Works

The tools leverage Flutter's built-in signal handling:

1. **Flutter Process**: Runs with `--pid-file` flag to track its process ID
2. **File Watcher**: Monitors your project files using Dart's `Directory.watch()` API
3. **Signal Communication**:
   - Sends `SIGUSR1` for hot reload (Dart code changes)
   - Sends `SIGUSR2` for hot restart (pubspec/asset changes)

## File Watching Details

### What Gets Watched

- **Hot Reload Triggers:**
  - All `.dart` files in the `lib/` directory (recursively)
  - Changes are detected instantly using OS-level file system events

- **Hot Restart Triggers:**
  - `pubspec.yaml` - dependency changes
  - `pubspec.lock` - locked dependency updates

### Performance

- Uses native file system events (inotify on Linux, FSEvents on macOS)
- Minimal CPU usage - no polling
- Instant response to file changes
- Handles thousands of files efficiently

## Keyboard Commands

While the auto-reload is running, you can still use Flutter's manual commands:

- `r` - Manual hot reload
- `R` - Manual hot restart
- `q` - Quit the application
- `h` - Show help

## Troubleshooting

### Flutter Process Not Stopping

If the script says it stopped Flutter but it's still running:

```bash
# Find Flutter processes
ps aux | grep flutter

# Force kill if needed
kill -9 <PID>
```

### No Auto-Reload Happening

Check that:
1. You're running from your Flutter project root
2. The `lib/` directory exists with `.dart` files
3. The watcher shows "Watcher is active" message
4. Your editor is actually saving files (not just displaying changes)

### Permission Denied

Make the shell script executable:

```bash
chmod +x tools/run_with_auto_reload.sh
```

## Platform Support

- ✅ **macOS** - Fully tested
- ✅ **Linux** - Fully tested
- ✅ **WSL2** - Works great
- ⚠️ **Windows** - Use WSL2 or Git Bash (native Windows support coming soon)

## Use Cases

### For Vim/Neovim Users

Add to your vim config for seamless integration:

```vim
" Run Flutter with auto-reload
nnoremap <leader>fr :!./tools/run_with_auto_reload.sh<CR>
```

### For Terminal Multiplexer Users (tmux/screen)

Perfect for split-pane workflows:
- Top pane: Your editor
- Bottom pane: Flutter with auto-reload
- Side pane: Device preview

### For AI Coding Assistants

Tools like GitHub Copilot, Claude Code, or Cursor can edit files while auto-reload keeps your app updated.

### For Remote Development

Works great with SSH and remote development:
- Edit files remotely
- Auto-reload triggers on the remote machine
- Preview on local device via port forwarding

## Contributing

Contributions are welcome! Some areas for improvement:

- [ ] Windows native support (without WSL)
- [ ] Configuration file support (`.flutter_auto_reload.yaml`)
- [ ] Custom file patterns and ignore lists
- [ ] Web dashboard for reload statistics
- [ ] Integration with popular editors (VS Code extension, vim plugin, etc.)
- [ ] Package distribution (pub.dev, Homebrew, npm)

## Technical Details

### Signal Handling

Flutter's hot reload mechanism responds to Unix signals:

```dart
// In Flutter's source:
// SIGUSR1 -> hot reload
// SIGUSR2 -> hot restart
```

Our watcher simply sends these signals when detecting changes.

### File System Events

We use Dart's efficient file watching API:

```dart
Directory('lib').watch(recursive: true).listen((event) {
  // React to file changes
});
```

This provides near-instant response times without polling.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

Created by [paddo](https://github.com/paddo)

## Acknowledgments

- Flutter team for the excellent `--pid-file` and signal handling features
- The Dart team for the robust file watching API
- The terminal-loving developer community

## Related Projects

- [nodemon](https://github.com/remy/nodemon) - Inspiration for file watching
- [entr](https://github.com/eradman/entr) - Unix file watching tool
- [watchexec](https://github.com/watchexec/watchexec) - Generic file watcher

---

If you find these tools useful, please star the repository and share with other Flutter developers who prefer terminal workflows!