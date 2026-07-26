<!-- source: https://github.com/Rishav03Raj/mini-code-copilot.git sha: 575b6ab4a2a7c6e9514ab7c9d82760c8c1d9f878 readme: main/README.md -->
# Rishav03Raj/mini-code-copilot

Mini Code Copilot is a responsive web application that simulates an AI coding assistant. Built with Next.js and Tailwind CSS, it features a split-screen IDE layout, syntax highlighting for JavaScript/Python/C++, and a persistent history drawer to track and manage code generations.

---

<div align="center">

🚀 MINI CODE COPILOT

Your Lightweight, Web-Based Coding Assistant

<br />
<br />

⚡ TRY IT NOW ⚡

<!-- LIVE DEMO BUTTON -->

<a href="https://mini-code-copilot-five.vercel.app/" target="_blank">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/👁️_VIEW_LIVE_DEMO-CLICK_TO_OPEN_APP-2ea44f?style=for-the-badge&logo=vercel&logoColor=white" alt="View Live Demo" height="40" />
</a>

<br />

Live Link:
https://mini-code-copilot-five.vercel.app/

<br />

<!-- DEPLOY BUTTON -->

<br />

"A seamless split-screen IDE experience that simulates AI code generation with zero latency."

</div>

📑 TABLE OF CONTENTS

Section

Description

1. The Vision

What is this project and why does it exist?

2. Architecture

A deep dive into the file structure & logic.

3. Tech Stack

The modern tools powering the application.

4. Features

A breakdown of UI/UX capabilities.

5. Getting Started

Step-by-step setup guide.

6. Roadmap

Future plans for production scaling.

🎯 1. THE VISION

Mini Code Copilot solves the problem of clunky, slow coding interfaces. It provides a clean, distraction-free environment where developers can type natural language prompts and receive instant code suggestions.

💡 Core Philosophy

Speed First: No heavy backend delays.

Visual Clarity: High contrast, split-screen layout.

Persistence: Your work is saved automatically.

🏗️ 2. ARCHITECTURE & DESIGN

This project abandons the traditional "spaghetti code" approach for a Strict Modular Architecture.

📂 File System Breakdown

app/page.tsx (The Brain)

Acts as the Controller. It manages the global state (Theme, History, Inputs) and orchestrates the layout.

Uses a Split-Pane Layout: Left for Input, Right for Output.

lib/mockApi.ts (The Engine)

Simulates a backend API.

Instead of hitting a real server, it parses keywords ("reverse", "sort", "api") and returns pre-optimized snippets with a realistic network delay.

hooks/useLocalStorage.ts (The Memory)

A custom React Hook that silently syncs state to the browser's localStorage.

Ensures that if you refresh the page, your Dark Mode and History are exactly where you left them.

⚡ 3. TECH STACK

<div align="center">

Category

Technology

Role in Project

Framework

Next.js 15

App Router, Layout Optimization, Server Components.

UI Library

React 19

Component Logic, State Management, Hooks.

Styling

Tailwind CSS

Utility-first styling, Dark Mode engine, Responsive Grid.

Icons

Lucide React

Lightweight, SVG-based professional iconography.

Language

TypeScript

Type safety, Interfaces for History/Settings.

</div>

⭐ 4. CORE FEATURES

🎨 The Interface (UI/UX)

Split-Screen IDE:

Left Panel: Distraction-free prompt area.

Right Panel: Syntax-highlighted code output.

Smart Theme Engine:

Toggles between Sun (Light) and Moon (Dark) modes.

Colors are forced via CSS variables to override browser defaults.

🧠 The Logic

Mock AI Generation:

Recognizes keywords like python, react, api.

Displays a "Thinking..." loading state with an animated progress bar.

History Drawer (Slide-Over):

A professional sidebar that slides from the Right.

Features Search, Delete, and Favorite functionality.

Sit on z-index: 999 to float above all content.

⚙️ Settings & Customization

Font Size Control: Adjust text from XS to Large.

Line Spacing: Control density from 1.0 to 2.0.

Language Selector: Switch between JavaScript, Python, and C++.

🚀 5. GETTING STARTED

Follow these exact steps to run the "Mini Code Copilot" on your local machine.

Step 1: Clone & Install

Open your terminal and run:

# 1. Clone the repository
git clone [https://github.com/yourusername/mini-code-copilot.git](https://github.com/yourusername/mini-code-copilot.git)

# 2. Navigate to directory
cd mini-code-copilot

# 3. Install dependencies
npm install


Step 2: Ignite the Server

Start the development environment:

npm run dev


Step 3: Launch

Open your browser and visit:

http://localhost:3000

🔮 6. FUTURE ROADMAP

If we were to take this project to a Series A Startup level, here is the execution plan:

🔹 Phase 1: Real Intelligence

[ ] Replace mockApi.ts with OpenAI GPT-4o API.

[ ] Implement Streaming (SSE) to make text appear character-by-character (Ghostwriter effect).

🔹 Phase 2: Cloud Sync

[ ] Add NextAuth.js (Google/GitHub Login).

[ ] Replace localStorage with PostgreSQL (Supabase) to save history across devices.

🔹 Phase 3: Advanced Editor

[ ] Swap the simple <pre> block for Monaco Editor (VS Code's core).

[ ] Add syntax highlighting colors (PrismJS).

<div align="center">

Built with ❤️ using Next.js & Tailwind
© 2024 Mini Code Copilot. MIT License.

</div>
