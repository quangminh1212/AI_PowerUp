<!-- source: https://github.com/rbutinar/ade-catalog.git sha: d9ff33d0c1028e0e4e5f0fa4fe161444a5555d52 readme: main/README.md -->
# rbutinar/ade-catalog

Agentic Data Engineering Framework - Enable autonomous data workflows with AI agents

---

# Agentic Data Engineer (ADE) — Catalog

**A local, self-hostable metadata catalog for Databricks + Power BI** — with
cross-platform lineage, an interactive graph explorer, and an MCP server so Claude
can query your data estate.

![ADE Catalog walkthrough](ade_catalog/web/static/img/features-tour.gif)

> **Preview edition.** This is the open, self-host preview: SQLite, local, no login,
> Power BI + Databricks from files you already have. Looking for the previous
> Streamlit version? → release **v0.3.0**.

## What it does

- **Parse** Power BI (TMDL / PBIP projects) and Databricks (`.py` notebooks) from files on disk
- **Catalog** every table, measure, notebook, report across platforms — browse + full-text search
- **Trace** cross-platform lineage in an interactive graph (bronze → gold → semantic model → measure)
- **Ask** — an MCP server exposes the catalog to Claude Desktop / Claude Code

## Quick start

```bash
git clone https://github.com/rbutinar/ade-catalog.git
cd ade-catalog
pip install -r requirements.txt          # SQLite = stdlib; no DB drivers to install

# 1. Create the local SQLite catalog
python -m ade_catalog.schemas.deploy_sqlite

# 2. Build the demo catalog (synthetic Acme estate)
python -m ade_catalog.ingest --source demo
python -m ade_catalog.cli lineage build --view Demo

# 3. Browse it
python -m ade_catalog.cli serve            # http://localhost:5001
```

Everything runs locally against a SQLite file — no accounts, no cloud, no login.

## Use it with Claude (MCP)

The bundled `.mcp.json` starts the catalog's MCP server over stdio — just open the
project in Claude Code, or add it to Claude Desktop:

```json
{
  "mcpServers": {
    "ade-catalog": {
      "command": "python",
      "args": ["-m", "ade_catalog.mcp_server.stdio"],
      "cwd": "/path/to/ade-catalog"
    }
  }
}
```

Then ask: *"What measures depend on the sales fact table?"*, *"Trace the lineage from
bronze to the Power BI model"*, *"Which notebooks write to gold?"*

## Bring your own data

Drop your exported files under `ade_data/<env>/inputs/` and rebuild:

- **Power BI** — a PBIP project's `definition/` folder (TMDL): tables, columns, measures (DAX), relationships
- **Databricks** — exported `.py` notebooks: table lineage (inputs/outputs) with variable resolution

```bash
python -m ade_catalog.ingest --source ade_data/my_env/inputs --view "My Env"
python -m ade_catalog.cli lineage build --view "My Env"
```

## Public preview vs. hosted / enterprise

| | Public preview (this repo) | Hosted preview & enterprise |
|---|---|---|
| Backend | SQLite, local | Postgres / SQL Server, multi-tenant |
| Sources | Power BI + Databricks, from files | + Fabric, Tableau, Talend, Cloudera, Oracle, Postgres, … + live/automated extraction |
| Lineage graph | ✅ interactive explorer | ✅ + large-graph performance |
| MCP | ✅ (stdio + HTTP) | ✅ hosted, org-scoped |
| AI assistant, AI enrichment, Excel/query export, data products | — | ✅ |
| Publish & share (multi-user, RLS) | — | ✅ |

**Want the managed version?** A hosted **private preview** runs at
[ade-catalog.vercel.app](https://ade-catalog.vercel.app) — build locally, then publish
and consume it online. Interested in enterprise? → **roberto.butinar@gmail.com**

## License

Apache 2.0 — see [LICENSE](LICENSE).

**Roberto Butinar** — [LinkedIn](https://linkedin.com/in/rbutinar) · [GitHub](https://github.com/rbutinar)
