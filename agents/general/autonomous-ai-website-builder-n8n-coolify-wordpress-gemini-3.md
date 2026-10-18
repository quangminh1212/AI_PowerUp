# Autonomous-AI-Website-Builder-n8n-Coolify-Wordpress-Gemini-3-
A fully autonomous workflow that deploys, designs, and populates a Dockerized WordPress site using n8n, Coolify, and Google Gemini 3.
![alt text](https://img.shields.io/badge/n8n-Workflow-FF6560?style=for-the-badge&logo=n8n)

![alt text](https://img.shields.io/badge/Coolify-Deployment-6B21A8?style=for-the-badge)

![alt text](https://img.shields.io/badge/WordPress-CMS-21759B?style=for-the-badge&logo=wordpress)

![alt text](https://img.shields.io/badge/AI-Gemini%203-4285F4?style=for-the-badge&logo=google)

📖 Overview

This repository contains an end-to-end automation pipeline designed for Service Businesses and AI Agencies. It transforms a single user prompt (e.g., "Create a modern website for a Solar Panel installation company in Texas") into a fully deployed, content-rich, and interactive website.

By leveraging Google Gemini 3 for intelligence and Coolify for infrastructure, this tool treats WordPress as a headless CMS database while injecting a high-performance, AI-architected Single Page Application (SPA) frontend directly into the Elementor Canvas.
✨ Key Features

    Infrastructure Automation: Automatically deploys a Dockerized WordPress container via the Coolify API.

    Zero-Touch Configuration: Uses SSH and wp-cli to install themes, configure permalinks, and create admin users without human intervention.

    Global Design System: A dedicated "Layout Architect" AI generates a unified CSS framework, Header, and Footer that persists across all pages (fixing the common AI issue of inconsistent designs).

    Intelligent Sitemap Strategy: Analyzes the specific industry to generate the perfect page hierarchy (Home, Services, Use Cases, Contact).

    Functional Lead Gen: Automatically embeds a custom JavaScript contact form that bypasses PHP mailers and posts leads directly to an n8n Webhook for immediate CRM automation.

    Dynamic Blog Integration: Includes a custom JS fetcher that retrieves real WordPress posts and displays them in an AI-styled grid, combining custom design with CMS management.

🏗️ Technical Architecture

The Pipeline:

    Provision: Workflow sends a POST request to Coolify to spin up a new WordPress service.

    Configure: N8n SSHs into the container to install hello-elementor, configure wp-cli, and set up the environment.

    Strategize: Gemini 3 analyzes the business niche and outputs a JSON Sitemap and Content Strategy.

    Design (Global): The "Layout AI" creates the global HTML structure (Nav/Footer) and CSS variables (Glassmorphism/Modern UI).

    Build (Loop): The workflow iterates through the sitemap. The "Content AI" generates unique, semantic HTML <section> content for every page.

    Assemble: A logic node stitches the Global Header + Page Content + Global Footer + Scripts, injecting dynamic navigation links based on the sitemap.

    Publish: The final HTML is pushed to WordPress via the REST API using the elementor_canvas template to ensure a blank slate.

🔌 Integrations
Component	Role
n8n	The orchestrator managing logic, loops, and API calls.
Coolify	Hosting platform managing the Docker containers.
Google Gemini 3	The brain generating code, copy, and design strategy.
WordPress	The database/CMS for managing posts and pages.
Webhooks	Captures form submissions for downstream automation (Slack, Email, CRM).
🛠️ Setup & Usage

    Import: Import the JSON workflow file into your n8n instance.

    Credentials: Configure your credentials for:

        Coolify API

        SSH (for the Docker host)

        OpenRouter / Google Gemini

    Config Node: Update the Config Variables node with your target domain, service name, and webhook receiver URL.

    Run: Submit the form trigger with your business description.

    Result: In ~3 minutes, you will have a live, fully designed website.
