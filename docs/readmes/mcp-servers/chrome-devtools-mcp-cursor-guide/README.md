<!-- source: https://github.com/ochapple/chrome-devtools-mcp-cursor-guide.git sha: 8a7aacd5dfd616dee4a43adff3a687d523f3f231 readme: main/README.md -->
# ochapple/chrome-devtools-mcp-cursor-guide

Chrome DevTools MCP integration guide for Cursor IDE - Enable AI coding assistants to debug web pages directly in Chrome

---

# Chrome DevTools MCP × Cursor IDE — Guide & Starter

> **Make Cursor *see* your web app.** This repo shows how to wire up the official **Chrome DevTools MCP server** to **Cursor IDE** so your AI assistant can debug live pages: inspect DOM, capture network traces, run Lighthouse, take screenshots, and more.

<p align="center">
  <img alt="Cursor + Chrome DevTools" src="assets/cover.png" width="640">
</p>

## Why this repo?

Community projects like `browser-tools-mcp` proved Cursor can control a headless browser.  
This guide integrates **Chrome’s official DevTools MCP server** maintained by the Chrome DevTools team — unlocking **full** DevTools capabilities:

- ✅ DOM & styles inspection
- ✅ Console logs & JS errors
- ✅ Network waterfalls & timings
- ✅ Lighthouse & Core Web Vitals
- ✅ Accessibility (a11y) checks
- ✅ Screenshots, mobile emulation, visual diffs
- ✅ Headless mode & CI-friendly flags

> TL;DR: This is **true debugging**, not just screenshots.

---

## Quick Start

## 🚀 Easiest Install (Cursor does it for you)

If you’re using **Cursor IDE**, you can simply **ask Cursor to install & configure the Chrome DevTools MCP**. Cursor will do the heavy lifting **as long as you grant Full Disk Access** (macOS) and provide the DevTools MCP package link.

**Paste this in Cursor chat:**

> *“Install the **Chrome DevTools MCP** and enable it for me.  
> Grant any required permissions.  
> Use the official package **chrome-devtools-mcp** and add it to my MCP servers.  
> If needed, update `settings.json` and restart Cursor.”*

- On macOS, ensure **System Settings → Privacy & Security → Full Disk Access → Cursor = ON**.  
- Cursor will install the MCP and wire up your `settings.json`.  
- You can immediately run DevTools commands (see prompts below).

**Don’t want to grant Full Disk Access?** No problem — use the **Manual Setup** below.


### Prereqs


### Where is `settings.json` on each OS?

| OS | Path to `settings.json` |
|---|---|
| **macOS** | `~/Library/Application Support/Cursor/User/settings.json` |
| **Windows** | `%APPDATA%\Cursor\User\settings.json` (usually `C:\Users\<you>\AppData\Roaming\Cursor\User\settings.json`) |
| **Linux** | `~/.config/Cursor/User/settings.json` |

> If the `User` folder or `settings.json` doesn’t exist, create them.

- Node.js **v20+**
- npm
- Cursor IDE **v1.7.38+**
- Chrome (stable/beta/dev/canary)

### 1) Install the DevTools MCP server (manual)

```bash
npm install -g chrome-devtools-mcp
chrome-devtools-mcp --version
```

### 2) Configure Cursor (manual)

Edit your Cursor settings (macOS path shown; adjust for your OS):

`~/Library/Application Support/Cursor/User/settings.json`

**Option A — Global install**
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "chrome-devtools-mcp",
      "args": []
    }
  }
}
```

**Option B — npx (auto‑update)**
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

### 3) Restart Cursor (manual)

That’s it. Cursor will spin up the MCP server on demand.

---

## Tools

You can quickly open your Cursor settings file using:

- macOS/Linux: `./tools/edit-settings.sh`
- Windows: `./tools/edit-settings.ps1`

These scripts detect your OS path and open or create the settings.json file for editing.

## Advanced Config


> **OS note:** The `settings.json` location differs by OS (see table above). Edit that file and restart Cursor after changes.


Use `args` to control Chrome:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "chrome-devtools-mcp",
      "args": ["--channel", "canary", "--viewport", "1280x720", "--headless"]
    }
  }
}
```

- `--channel <stable|beta|dev|canary>`
- `--headless`
- `--viewport 1280x720`
- `--browserUrl http://127.0.0.1:9222` (attach to existing Chrome)

---

## Try These Prompts in Cursor

- “Check performance metrics for https://example.com and recommend fixes.”
- “Analyze network requests for https://github.com; list slow resources.”
- “Inspect the DOM of the header; show computed styles and layout.”
- “Take a mobile screenshot of https://example.com and highlight layout issues.”
- “Run a Lighthouse audit and summarize Core Web Vitals.”

Expected behavior with MCP enabled:
- Chrome launches (or connects)
- You get real console/DOM/network data
- You can capture screenshots and audits from inside Cursor

---

## Why This Is More Feature‑Rich (vs `browser-tools-mcp`)

| Capability | `browser-tools-mcp` | **Chrome DevTools MCP (this guide)** |
|---|---|---|
| Maintainer | Community | **Chrome DevTools Team** |
| Protocol | Puppeteer-like wrapper | **Full DevTools Protocol** |
| DOM inspection | Partial | **Full** |
| Network tracing | ❌ | **✅** |
| Lighthouse / CWV | ❌ | **✅** |
| Console logs / errors | ❌ | **✅** |
| Accessibility audit | ❌ | **✅** |
| Responsive testing | Basic | **Advanced** |
| CI/headless stability | Mixed | **Robust** |

---

## Troubleshooting

1. **Server won’t start**
   - Confirm Node.js ≥ 20: `node -v`
   - Ensure global install succeeded: `chrome-devtools-mcp --version`
   - Chrome installed? Try launching Chrome manually.

2. **Cursor doesn’t see the server**
   - Validate `settings.json` JSON syntax.
   - Restart Cursor after editing settings.
   - On macOS/Linux, check the exact settings path.

3. **Need logs**
   ```bash
   export DEBUG=*
   chrome-devtools-mcp --logFile /tmp/chrome-devtools-mcp.log
   ```

---

## Security Notes

This MCP exposes browser content to tools inside Cursor. Treat it like a real debugger:
- Don’t open pages with sensitive data.
- Use a separate Chrome profile for testing.
- Prefer headless + isolated environments in CI.

---

## Repo Structure

```
chrome-devtools-mcp-cursor-guide/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ examples/
│  ├─ cursor-settings.json
│  ├─ prompts.md
├─ scripts/
│  ├─ quick-test.sh
│  └─ ci-headless-example.sh
├─ .github/
│  ├─ ISSUE_TEMPLATE/bug_report.md
│  └─ workflows/lint.yml
└─ assets/
   └─ cover.png  (placeholder)
```

---

## Roadmap

- [ ] Add Windows/Linux settings paths table
- [ ] Add demo GIFs (Lighthouse run, DOM inspect, console error capture)
- [ ] Add CI examples (GitHub Actions & headless Chrome)
- [ ] Add sample prompts library

---


## 🤖 Let Cursor Create the GitHub Repo for You

If you want **Cursor to create the public GitHub repo** from this template, zip, and push it for you, paste this in Cursor chat:

> *“Create a new **public GitHub repository** named `chrome-devtools-mcp-cursor-guide`.  
> Unzip the attached archive and initialise a git repo.  
> Add all files, create an initial commit, and push to GitHub (main branch).  
> Add topics: cursor, chrome-devtools, mcp, ai-development, web-performance.  
> Then reply with the repo URL.”*

If Cursor needs credentials, it will prompt you to authenticate GitHub.


## Credits

- Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp  
- Model Context Protocol: https://modelcontextprotocol.io  
- Cursor IDE: https://cursor.sh

---

## License

MIT — see [LICENSE](LICENSE).
