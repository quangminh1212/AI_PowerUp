# CloneLab

Hermes-facing **git clone workspace + lineage manager** for projects **you** develop based on other repos.

1. **Clone** third-party remotes  
2. **Track** own projects with **`based_on`** (upstream)  
3. Store **`rules`** + **`references`** per project  
4. Materialize agent-readable packs under `projects/<id>/`

SoT: `C:\Dev\CloneLab`. Hermes attaches via **skill junction only**.

## Quick start

```powershell
cd C:\Dev\CloneLab
python -m pip install -e ".[dev]"
clonelab smoke

# Seed all known C:\Dev labs (based_on + rules + refs + packs)
clonelab seed --replace

clonelab list --role own
clonelab show routerlab
clonelab lineage
```

### Own project card

```powershell
clonelab track C:\Dev\MyLab `
  --based-on "https://up/base|core" `
  --rule "Junction only — no hermes-agent edits"

clonelab rule add mylab "Receipt must be readable before done"
clonelab ref add mylab --url https://up/docs --kind docs --note "guide"
clonelab show mylab
clonelab pack mylab
```

### Pack layout (per project)

```
projects/routerlab/
├── RULES.md           # human/agent rules + based_on summary
└── references.yaml    # structured refs + based_on
```

Registry: `clones/registry.yaml` (schema **v3**).

## Model

| Field | Meaning |
|-------|---------|
| `role` | `own` / `clone` / `reference` |
| `based_on[]` | upstream bases (`id`, `url`, `note`) |
| `rules[]` | development rules for *this* derivative |
| `references[]` | extra refs (`kind`: repo\|docs\|issue\|paper\|license\|other) |
| `path` / `url` | local path + own remote |

## CLI map

| Command | Purpose |
|---------|---------|
| `seed` | load known labs + rules/refs |
| `show <id>` | full card |
| `rule add\|list\|rm` | manage rules |
| `ref add\|list\|rm` | manage references |
| `pack [id]` | write `projects/<id>/` |
| `track` / `based-on` / `lineage` | own lineage |
| `clone` / `pull` / `status` | third-party clones |

## Hermes attach

```powershell
powershell -File C:\Dev\CloneLab\scripts\install.ps1
# chat: /clonelab
```

## AgentLab pin

Submodule: `integrations/clonelab` → `C:/Dev/CloneLab`
