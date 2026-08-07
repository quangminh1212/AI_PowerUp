# 🕷️ Web Crawl — Remote Tools cho AI lấy thông tin từ Web

> **Danh mục các công cụ, framework, MCP server hỗ trợ AI crawl, scrape, fetch, extract dữ liệu từ internet.**
>
> Các tool này cho phép AI agent truy cập, đọc, phân tích nội dung web — phục vụ research, RAG, data pipeline, monitoring.

---

## 📊 Tổng quan (17 Repos)

| # | Repo | Stars | Loại | Chức năng chính |
|---|------|-------|------|-----------------|
| 1 | **[crawl4ai](crawl4ai)** | 77k+ | 🕷️ Crawler | Open-source LLM-friendly web crawler. Markdown output, structured extraction, deep crawling |
| 2 | **[firecrawl](firecrawl)** | 25k+ | 🔥 Scrape API | Web scraping API — scrape, crawl, map, search. Convert任何website sang markdown |
| 3 | **[scrapegraph-ai](scrapegraph-ai)** | 22k+ | 🤖 AI Scraper | AI-powered web scraping — dùng LLM để tự hiểu cấu trúc website, extract data |
| 4 | **[jina-reader](jina-reader)** | 10k+ | 📖 Reader | URL → clean markdown. Reader API cho AI, hỗ trợ search, grounding |
| 5 | **[browser-use](browser-use)** | 15k+ | 🌐 Browser Agent | Browser automation cho AI agents — navigate, click, fill forms, extract |
| 6 | **[spider](spider)** | 5k+ | 🕸️ Crawler Cloud | Rust-based web crawler — fast, scalable, cloud-ready crawling |
| 7 | **[tavily](tavily)** | 8k+ | 🔍 Search+Extract | Tavily API — search, extract, crawl optimized cho RAG pipelines |
| 8 | **[apify-client](apify-client)** | 3k+ | 🏪 Scraping Platform | Apify platform — 55,000+ ready-made scrapers cho mọi website |
| 9 | **[trafilatura](trafilatura)** | 6k+ | 📄 Extractor | Web content extraction — clean text, metadata từ HTML. Best-in-class accuracy |
| 10 | **[optillm](optillm)** | 2k+ | ⚡ Optimized LLM | Optimized LLM inference + web context processing |

## 🔧 MCP Servers (cho AI Agent)

| # | Repo | Loại | Chức năng |
|---|------|------|-----------|
| 11 | **[firecrawl-mcp-server](firecrawl-mcp-server)** | MCP | Firecrawl official — scrape/crawl/map/search qua MCP tools |
| 12 | **[crawl4ai-mcp-server](crawl4ai-mcp-server)** | MCP | Crawl4AI lightweight MCP — self-hosted, free scraping |
| 13 | **[crawl4ai-mcp-server-bjorn](crawl4ai-mcp-server-bjorn)** | MCP | Crawl4AI高性能 MCP — CloudFlare Workers, optimized |
| 14 | **[playwright-mcp](playwright-mcp)** | MCP | Microsoft Playwright — browser automation MCP cho testing + scraping |
| 15 | **[crawl4ai-mcp](crawl4ai-mcp)** | MCP | Crawl4AI MCP — markdown output + citations |
| 16 | **[mcp-crawl4ai](mcp-crawl4ai)** | MCP | Crawl4AI MCP 100% free — self-hosted, no API key |
| 17 | **[mcp-crawl4ai-rag](mcp-crawl4ai-rag)** | MCP | Crawl4AI + RAG pipeline — crawl → embed → query |

## 🎯 Lựa chọn theo Use Case

### Cần crawl nhanh, clean markdown → **Crawl4AI** hoặc **Trafilatura**
```bash
# Crawl4AI — LLM-friendly markdown
crawl4ai https://example.com --output markdown

# Trafilatura — accurate extraction
trafilatura https://example.com
```

### Cần scrape với AI understanding → **ScrapeGraphAI**
```bash
# AI tự phân tích DOM structure
scrapegraph-ai "Extract all product prices from this page" --url https://shop.com
```

### Cần browser automation → **Browser-Use** hoặc **Playwright MCP**
```python
# Browser-use — AI agent tự navigate
from browser_use import Agent
agent = Agent(task="Search for latest AI news on Google")
await agent.run()
```

### Cần search + extract cho RAG → **Tavily** hoặc **Jina Reader**
```python
# Tavily — optimized cho RAG
from tavily import TavilyClient
client = TavilyClient(api_key="...")
results = client.search("latest AI research", include_raw_content=True)
```

### Cần scraping platform-scale → **Apify** hoặc **Firecrawl**
```python
# Apify — 55k+ ready scrapers
from apify_client import ApifyClient
client = ApifyClient("YOUR_TOKEN")
run = client.actor("apify/web-scraper").call(input={"startUrls": ["https://example.com"]})
```

### Cần MCP tools cho AI agent → **Firecrawl MCP** hoặc **Playwright MCP**
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@mendableai/firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "..." }
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

## 📦 Install nhanh

### Crawl4AI (pip)
```bash
pip install crawl4ai
crawl4ai-setup  # Install browser binaries
crawl4ai https://example.com
```

### Firecrawl (npm/pip)
```bash
# npm
npx -y @mendableai/firecrawl-mcp

# pip
pip install firecrawl-py
```

### ScrapeGraphAI (pip)
```bash
pip install scrapegraphai
```

### Trafilatura (pip)
```bash
pip install trafilatura
trafilatura https://example.com
```

### Tavily (pip)
```bash
pip install tavily-python
```

### Browser-Use (pip)
```bash
pip install browser-use
playwright install chromium
```

### Apify Client (pip)
```bash
pip install apify-client
```

### Jina Reader
```bash
curl "https://r.jina.ai/https://example.com"  # Free, no API key
```

## 🔗 Liên kết

- [Crawl4AI Docs](https://docs.crawl4ai.com/)
- [Firecrawl Docs](https://docs.firecrawl.dev/)
- [ScrapeGraphAI Docs](https://scrapegraphai.com/)
- [Tavily Docs](https://docs.tavily.com/)
- [Apify Docs](https://docs.apify.com/)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Jina Reader API](https://jina.ai/reader/)
- [MCP Registry](https://registry.modelcontextprotocol.io/)

---

*Last updated: 2026-08-07 | Part of [AI PowerUp](../README.md) ecosystem*
