<!-- source: https://github.com/nventive/Promptitude.git sha: d635b035eb34c6320d7fb470d3fdc0736b520dbb readme: main/README.md -->
# nventive/Promptitude

IDE Extension to automatically sync AI coding assistants configuration and prompt files stored remotely to your IDE. 

---

# Promptitude IDE Extension

> Automatically sync GitHub Copilot prompts from multiple Git repositories to your local VS Code environment.

## 🎯 Overview

The Promptitude Extension automatically synchronizes the latest GitHub Copilot prompts, instructions, and templates from one or more Git repositories to your local VS Code user prompts directory. This ensures you always have access to the most up-to-date, peer-reviewed prompts across all your projects from multiple sources.

## ✨ Features

- **🔄 Automatic Sync**: Configurable sync frequency (daily by default)
- **📦 Multiple Repositories**: Support for syncing from multiple Git repositories simultaneously
- **🌍 Cross-Platform**: Works on macOS, Windows, and Linux with intelligent symlink fallback
- **⚙️ Configurable**: Customizable sync frequency and target directory
- **🔐 Secure**: Uses your existing GitHub authentication from VS Code and secure PAT storage for Azure DevOps
- **🌐 Multi-Provider**: Supports both GitHub and Azure DevOps repositories
- **📦 Read-Only**: Safe pull-only synchronization (no risk of overwriting repositories)
- **🎨 User-Friendly**: Simple setup with minimal configuration required
- **📊 Status Indicators**: Clear feedback on sync status and last update time
- **🛡️ Error Handling**: Graceful handling of repository conflicts and partial failures
- **💻 Windows Compatibility**: Automatic fallback to file copies when symlinks aren't available (no admin rights needed)

## 🚀 Quick Start

### Prerequisites

- VS Code 1.70.0 or higher
- GitHub authentication configured in VS Code (for GitHub repositories)
- Azure DevOps Personal Access Token (for Azure DevOps repositories)
- Access to a git repository with prompts and configuration files

### Installation

1. Download the latest `promptitude-extension.vsix` file from the releases
2. Open VS Code
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette
4. Type "Extensions: Install from VSIX" and select it
5. Browse and select the downloaded `.vsix` file
6. Restart VS Code when prompted

### First-Time Setup

1. Open VS Code Settings (`Ctrl+,` or `Cmd+,`)
2. Search for "Promptitude"
3. Configure your preferences (optional - defaults work for most users)
4. The extension will automatically perform an initial sync

## ⚙️ Configuration

### Extension Settings

| Setting                         | Description                      | Default                                                              | Type    |
| ------------------------------- | -------------------------------- | -------------------------------------------------------------------- | ------- |
| `promptitude.enabled`           | Enable/disable automatic syncing | `true`                                                               | boolean |
| `promptitude.frequency`         | Sync frequency                   | `"daily"`                                                            | string  |
| `promptitude.customPath`        | Custom prompts directory path    | `""`                                                                 | string  |
| `promptitude.repositories`      | Repositories with optional branch (use `url` or `url\|branch`) | `[]`                                   | array   |
| `promptitude.syncOnStartup`     | Sync when VS Code starts         | `true`                                                               | boolean |
| `promptitude.showNotifications` | Show sync status notifications   | `true`                                                               | boolean |
| `promptitude.syncChatmode`      | Sync agent prompts (supports both agents/ and legacy chatmodes/ directories) | `true`                   | boolean |
| `promptitude.syncInstructions`  | Sync instructions prompts        | `true`                                                               | boolean |
| `promptitude.syncPrompt`        | Sync prompt files                | `true`                                                               | boolean |

### Sync Frequency Options

- `"startup"` - Only sync when VS Code starts
- `"hourly"` - Sync every hour
- `"daily"` - Sync once per day (default)
- `"weekly"` - Sync once per week
- `"manual"` - Only sync when manually triggered

### Default Prompts Directory Paths

The extension automatically detects the correct prompts directory for your operating system:

- **macOS**: `~/Library/Application Support/Code/User/prompts`
- **Windows**: `%APPDATA%\Code\User\prompts`
- **Linux**: `~/.config/Code/User/prompts`

You can override this by setting a custom path in `promptitude.customPath`.

The extension will adapt this path automatically to function with non-default VS Code profiles.

### Platform-Specific Behavior

#### Windows Symlink Handling

On Windows, the extension intelligently handles file synchronization:

- **With Developer Mode or Admin Rights**: Creates symlinks for optimal performance (files stay in sync automatically)
- **Without Special Permissions**: Automatically falls back to copying files (no admin rights required)
- Both approaches work seamlessly - the extension detects and manages active prompts correctly

To enable symlinks on Windows 10/11 without admin rights:
1. Go to Settings → Update & Security → For developers
2. Enable "Developer Mode"
3. Restart VS Code

**Note**: File copy mode works perfectly fine for most users and requires no special setup.

### Multiple Repository Configuration

The extension supports syncing from multiple Git repositories simultaneously. This is useful for organizations that maintain prompt collections across multiple repositories or for users who want to combine prompts from different sources.

#### Setting up Multiple Repositories (with optional per-repo branch)

1. **Using VS Code Settings UI**:
   - Open Settings (`Ctrl+,` or `Cmd+,`)
    - Search for "promptitude.repositories"
    - Click "Add Item" to add each repository using one of the following formats:
       - `https://github.com/your-org/prompts` (defaults to branch `main`)
       - `https://github.com/your-org/prompts|develop` (explicit branch)
       - `https://dev.azure.com/org/project/_git/repo` (Azure DevOps modern format)
       - `https://org.visualstudio.com/project/_git/repo` (Azure DevOps legacy format)

2. **Using JSON Configuration**:
   ```json
    {
       "promptitude.repositories": [
          "https://github.com/your-org/prompts",
          "https://github.com/your-org/prompts|develop",
          "https://github.com/another-org/shared-prompts|release"
       ]
    }
   ```

#### Error Handling

When syncing multiple repositories:

- **Partial Success**: If some repositories sync successfully while others fail, the extension shows a partial success notification with details
- **Complete Failure**: If all repositories fail, an error notification is shown
- **Individual Errors**: Repository-specific errors are logged and reported separately

## 🎮 Usage

### Automatic Sync

Once configured, the extension works automatically based on your sync frequency setting. You'll see notifications (if enabled) when sync operations complete.

### Status Bar

The extension adds a status bar item showing:

- Sync status (✅ synced, 🔄 syncing, ❌ error)
- Last sync time
- Click to manually trigger sync

## 📁 Synced Content

The extension syncs all prompt files from the repository subdirectories into a flattened structure:

```
agents/*.md          → User/prompts/
chatmodes/*.md       → User/prompts/ (legacy support)
instructions/*.md   → User/prompts/
prompts/*.md         → User/prompts/
```


## 🔧 Troubleshooting

Access these commands through the VS Code Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`):

### General Commands

| Command | Description |
|---------|-------------|
| **Promptitude: Sync Now** | Manually trigger an immediate sync of all configured repositories |
| **Promptitude: Show Status** | Display extension status, configuration, and authentication information |
| **Promptitude: Open Prompts Folder** | Open the local prompts directory in your system file explorer |

### Azure DevOps Authentication Management

| Command | Description |
|---------|-------------|
| **Promptitude: Add Azure DevOps Personal Access Token** | Add or update a Personal Access Token (PAT) used to access Azure DevOps repositories |
| **Promptitude: Remove Azure DevOps Personal Access Token(s)** | Remove one or all stored PATs |
| **Promptitude: Clear Azure DevOps Authentication Cache** | Clear cached organization authentication; forces re-authentication on next sync |



### Common Issues

#### Sync Fails with Authentication Error

**Problem**: Extension can't access the GitHub repository

**Solutions**:

1. Ensure you're signed into GitHub in VS Code (`View > Command Palette > GitHub: Sign In`)
2. Verify you have access to the repository
3. Check your internet connection

#### Azure DevOps Authentication Issues

**Problem**: Extension can't access Azure DevOps repository (400/401/403 errors)

**Solutions**:

1. Ensure your Personal Access Token (PAT) has the correct permissions:
   - Minimum required: `Code (read)` permission
   - For organization repositories: ensure PAT has access to the specific organization/project
2. Verify the repository URL format is correct:
   - Modern: `https://dev.azure.com/org/project/_git/repo`
   - Legacy: `https://org.visualstudio.com/project/_git/repo`
3. Check that the PAT hasn't expired
4. Use the "Promptitude: Add Azure DevOps Personal Access Token" command to re-enter your PAT

#### Prompts Directory Not Found

**Problem**: Extension can't find or create the prompts directory

**Solutions**:

1. Ensure VS Code has write permissions to the user directory
2. Manually create the prompts directory if it doesn't exist
3. Set a custom path in extension settings

#### Sync Takes Too Long

**Problem**: Sync operation seems stuck

**Solutions**:

1. Check your internet connection
2. Try manual sync to see detailed error messages
3. Restart VS Code and try again

### Debug Mode

Enable debug logging:

1. Open VS Code Settings
2. Search for "promptitude.debug"
3. Enable debug mode
4. Check the "Promptitude" output channel for detailed logs

## 🔒 Security & Privacy

- **Read-Only Access**: The extension only pulls content from the repository
- **No Data Collection**: No usage data or personal information is collected
- **GitHub Authentication**: Uses VS Code's built-in GitHub authentication
- **Azure DevOps Authentication**: Securely stores Personal Access Tokens using VS Code's SecretStorage
- **Local Storage**: All prompts are stored locally on your machine
- **No Network Requests**: Only communicates with GitHub/Azure DevOps for repository access

## 🛠️ Development

### Building from Source

```bash
# Clone the repository
git clone <url>

# Install dependencies
npm install

# Build the extension
npm run compile

# Package the extension
npm run package
```

### Project Structure

```
tools/vscode-extension/
├── src/
│   ├── extension.ts          # Main extension entry point
│   ├── syncManager.ts        # Sync logic and GitHub integration
│   ├── configManager.ts      # Configuration management
│   ├── statusBarManager.ts   # Status bar integration
│   └── utils/
│       ├── fileSystem.ts     # File system operations
│       ├── github.ts         # GitHub API wrapper
│       └── notifications.ts  # User notifications
├── package.json              # Extension manifest
├── tsconfig.json            # TypeScript configuration
├── webpack.config.js        # Build configuration
└── README.md               # This file
```

### Scripts

- `npm run compile` - Build the extension
- `npm run watch` - Build in watch mode
- `npm run package` - Create VSIX package
- `npm run test` - Run tests
- `npm run lint` - Run ESLint


## 🤝 Contributing

We welcome contributions to improve the extension! Please see our [Contribution Guide](../../docs/contribution-guide.md) for details.

### Reporting Issues

1. Check existing issues in the repository
2. Create a new issue with:
   - Extension version
   - VS Code version
   - Operating system
   - Detailed description of the problem
   - Steps to reproduce

### Feature Requests

1. Open an issue with the "enhancement" label
2. Describe the desired functionality
3. Explain the use case and benefits

## 📋 Changelog

For the complete release history, detailed changes, and migration notes, please refer to the project's changelog:

[See CHANGELOG.md](./CHANGELOG.md)

## 📄 License

Apache 2.0

## 📞 Support

For support and questions:

- Check the [troubleshooting section](#-troubleshooting) above
- Report an issue.


---

**Made with ❤️ by the Logient-nventive Team**
