# WorkerLab

**Live coding-agent activity monitor** cho máy cục bộ: theo dõi agent, tool, workflow; cung cấp hàng đợi job lưu bằng YAML và dashboard.

SoT: `C:\Dev\WorkerLab`. Hermes gắn qua **skill junction only**. OpenWork/OpenWorker chỉ là tham chiếu trong `sources/catalog.yaml`, không vendored.

## Phạm vi bảo mật

WorkerLab chỉ dành cho máy cục bộ. HTTP server chỉ chấp nhận `127.0.0.1`, `::1`, hoặc `localhost`; mặc định `127.0.0.1:4173`. Không đổi bind thành địa chỉ LAN/public, không đặt sau reverse proxy, không công khai qua tunnel. API không có xác thực; dữ liệu riêng tư đã biết được redaction nhưng đầu ra vẫn nên xem là dữ liệu nội bộ.

## Cài đặt, chạy, kiểm thử

Yêu cầu: Node.js 20+, Python 3.11+.

```powershell
cd C:\Dev\WorkerLab
python -m pip install -e ".[dev]"
npm start
# http://127.0.0.1:4173
```

Có thể double-click `run.bat`. Node server không có dependency npm; không cần `npm install`.

```powershell
cd C:\Dev\WorkerLab
python -m pytest tests -q
npm test
workerlab smoke
```

Cấu hình server tùy chọn: `HOST` (chỉ loopback), `PORT` (1–65535), `WORKERLAB_PYTHON`, `WORKERLAB_CACHE_MS`, `WORKERLAB_CONTEXT_CACHE_MS`.

## HTTP API

Tất cả route chỉ hỗ trợ `GET`. `fresh=1` bỏ qua cache. JSON dùng `Cache-Control: no-store`.

| Route | Query | Kết quả |
|---|---|---|
| `GET /api/health` | — | Tình trạng service/Python, version, số agent view, tuổi cache; trả `503` khi probe Python lỗi. |
| `GET /api/agents` | `fresh=1` | Toàn bộ snapshot agent đã redaction. |
| `GET /api/workflows` | `fresh=1` | Workflow đang hoạt động. |
| `GET /api/summary` | `fresh=1`, `all=1` | Summary, workflows, network, timeline; `all=1` thêm node idle vào network. |
| `GET /api/timeline` | `fresh=1`, `limit=N` | Lịch sử tool mới nhất; mặc định 80, giới hạn 1–500. |
| `GET /api/context` | `fresh=1` | Inventory MCP, skill, plugin, rule cục bộ đã redaction. |
| `GET /api/network` | `fresh=1`, `all=1` | Graph agent/model/workspace/tool/context; `all=1` gồm idle. |

`GET /` phục vụ dashboard; asset tĩnh nằm dưới `public/`. Method khác `GET`/`HEAD` trả `405`.

## CLI

```powershell
workerlab smoke
workerlab agents
workerlab live
workerlab live --agent grok,hermes --alive
workerlab live --json
workerlab watch --interval 2
workerlab context
```

Live monitor đọc process list và session/log store cục bộ; không cần network. Agent hỗ trợ gồm Grok CLI, Hermes, Codex, Claude, Cursor, OpenCode, Aider, Windsurf, Gemini, Qwen, Copilot, Continue. Phase: `thinking`, `tool_running`, `waiting_model`, `running`, `responding`, `idle`, `unknown`. Hermes alive window: message cuối ≤ 20 phút.

## Hàng đợi job

```powershell
workerlab init runs\demo --name demo
workerlab enqueue runs\demo --title "hello job" --instructions "do the work"
workerlab list runs\demo
workerlab run runs\demo --once
workerlab status runs\demo
```

Status: `queued | running | ok | error | skipped`.

## Hermes attach

```powershell
powershell -File C:\Dev\WorkerLab\scripts\install.ps1
# chat: /workerlab
# detach: scripts\uninstall.ps1
```

## Vận hành

Xem [`RUNBOOK.md`](RUNBOOK.md) để xử lý port, Python, probe, YAML, disk, backup, rollback.

## Layout

```text
workerlab/                    Python package
server.js                     Local dashboard/API
public/                       Dashboard UI
sources/catalog.yaml          External references
skills/workerlab/             Hermes skill
scripts/install.ps1           Attach script
tests/                        pytest
test/                         node:test
.github/workflows/ci.yml      Windows release gate
```

## AgentLab pin

Submodule: `integrations/workerlab` → `C:/Dev/WorkerLab`
