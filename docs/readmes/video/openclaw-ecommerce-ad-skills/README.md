<!-- source: https://github.com/lujiaheng-artpivot/openclaw-ecommerce-ad-skills.git sha: fc0e3e57b2b320c48726a5ff09fb6885d012b52e readme: main/README.md -->
# lujiaheng-artpivot/openclaw-ecommerce-ad-skills

OpenClaw creative studio skills for ecommerce ads, TVC craft, Seedance video generation, and AI manga drama workflows.

---

# OpenClaw Creative Studio Skills

一个把电商广告、TVC 工艺、Seedance 视频生成和 AI 漫剧整合到一起的 OpenClaw 技能仓库。现在仓库里同时覆盖增长投放工作流、品牌化视频包装、角色一致性剧情短片，以及生成后的质量分析闭环。

## 这次整合后的重点

- 把原本独立的 `openclaw-seed2-skills` 四个技能并入统一 `skills/` 架构
- 新增 `story-video-orchestrator`，把角色图 -> 剧本/分镜 -> 多场景视频 -> 质检报告连成一条流水线
- 新增 `manga-director` 和 `video-qc` 两个 Agent，补齐剧情视频侧的协作角色
- 为关键技能补充 `references/` 资源，避免 Skill 说明只剩脚本调用示例
- 修复安装脚本的别名写入问题，并补上更完整的命令别名

## Skill Families

| 分层 | 代表技能 | 主要用途 |
|------|----------|----------|
| 增长广告层 | `ad-orchestrator`, `ad-copywriting`, `ad-analytics`, `ad-abtest` | 电商广告、出海投放、多平台素材迭代 |
| TVC 工艺层 | `tvc-storyboard`, `tvc-color-grading`, `tvc-sound-design` | 更偏导演/后期视角的品牌短片制作 |
| 剧情视频层 | `seedance-video`, `manga-style-video`, `manga-drama`, `story-video-orchestrator` | AI 漫剧、剧情短片、角色一致性视频 |
| 分析质检层 | `volcengine-video-understanding` | 视频理解、质量评估、叙事复盘 |

## 快速开始

### 1. 安装

```bash
chmod +x install.sh
./install.sh
```

默认会安装到：

- `~/.openclaw/skills`
- `~/.openclaw/agents`
- `~/.openclaw/config`

如果你在桌面版或自定义目录下运行，可以通过 `OPENCLAW_HOME`、`OPENCLAW_SKILLS_DIR`、`OPENCLAW_AGENTS_DIR`、`OPENCLAW_CONFIG_DIR` 覆盖。

### 2. 广告素材流水线

```bash
run-pipeline \
  --product-image ./product.jpg \
  --product-info '{"name":"无线耳机","price":"299元","features":["降噪","长续航","防水"]}' \
  --platform douyin \
  --output-dir ./ad_output
```

### 3. 剧情视频流水线

```bash
run-story-pipeline \
  --character ./character.png \
  --theme "樱花树下的邂逅" \
  --style anime_2d \
  --scenes 4 \
  --output-dir ./story_output
```

### 4. 底层模型能力直调

```bash
seedance-t2v --prompt "产品在晨光中缓慢旋转展示" --ratio 16:9 --duration 5 --output ./output.mp4
manga-text-video --prompt "少女在海边回头微笑" --style ghibli --output ./ghibli.mp4
generate-manga-drama --character ./character.png --theme "古风仙侠奇缘" --output-dir ./drama_output
analyze-video --video ./output.mp4 --aspect comprehensive --output ./analysis.md
```

## 仓库结构

```text
openclaw-ecommerce-ad-skills/
├── README.md
├── install.sh
├── .gitignore
├── references/
│   ├── architecture-overview.md
│   └── cross-border-playbook.md
├── skill-event-bus/
│   └── bus.json
├── agents/
│   ├── creative-director.agent.yaml
│   ├── tvc-creative-director.agent.yaml
│   ├── manga-director.agent.yaml
│   └── video-qc.agent.yaml
└── skills/
    ├── ad-*
    ├── tvc-*
    ├── seedance-video/
    ├── manga-style-video/
    ├── manga-drama/
    ├── story-video-orchestrator/
    └── volcengine-video-understanding/
```

## 现在包含什么

- 19 个技能
- 10 个 Agent
- 1 份统一事件总线
- 2 份仓库级参考文档
- 多个 Skill 内部 `references/` 资源

## 推荐工作流

### 电商增长

`ad-orchestrator` -> `ad-analytics` -> `ad-abtest`

适合从商品信息直接出文案、场景图、视频、分析报告和变体。

### 品牌/TVC

`tvc-storyboard` + `tvc-hook-generator` + `tvc-sound-design` + `seedance-video`

适合先做导演层设计，再用模型层完成画面生成。

### AI 漫剧

`story-video-orchestrator` -> `manga-drama` -> `volcengine-video-understanding`

适合一张角色图起步，快速做剧情分镜并带质检复盘。

## 平台和区域

支持抖音、小红书、淘宝、快手、TikTok Global、Amazon、Instagram、YouTube、Shopee 等平台。跨境投放建议、语言与市场适配可查看：

- `references/architecture-overview.md`
- `references/cross-border-playbook.md`

## 运行依赖

- Python 3.10+
- `ARK_API_KEY`
- `ffmpeg`（视频后处理相关技能建议安装）
- `volcengine-python-sdk[ark]`

## 适合谁用

- 想把 OpenClaw 做成广告内容工厂的人
- 需要把 Seedance/豆包能力接进自己的创作流的人
- 想同时覆盖“投放视频”和“剧情短片”两条产线的人
