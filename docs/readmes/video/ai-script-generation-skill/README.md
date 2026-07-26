<!-- source: https://github.com/FeiFei-AIDev/ai-script-generation-skill.git sha: ad36a8e249c05c0e51b8a4aaaaaaa40874a507d2 readme: main/README.md -->
# FeiFei-AIDev/ai-script-generation-skill

Codex/Claude skill for generating bilingual-ready AI short-video scripts with frameworks, hooks, and examples.

---

# AI Script Generation Skill / AI 短视频脚本生成 Skill

一个面向 AI 教程、AI 提效技巧内容创作者的 Codex/Claude Skill。它会根据用户提供的主题和参考素材，结合爆款叙事框架、热点话题和心理触发点，一次生成 5 个适合小红书、抖音、视频号的 30-40 秒短视频脚本方案。

A Codex/Claude skill for creators who publish AI tutorials and productivity tips. Given a topic and optional reference material, it combines proven short-video structures, trend angles, and psychological hooks to generate five ready-to-shoot 30-40 second scripts for Xiaohongshu, Douyin, and WeChat Channels.

## Features / 功能亮点

- 生成 5 个不同角度的短视频脚本：干货效率型、痛点共鸣型、悬念反转型、对比冲击型、热点借势型。
- 自动拆解参考素材的结构、心理触发点和可复用表达。
- 基于 `references/` 中的框架库、风格指南、心理触发点手册和热点库进行创作。
- 每个脚本包含标题、核心卖点、使用框架、结合热点、心理钩子、完整口播、画面建议、预估时长和制作难度。
- 适用于 AI 工具教程、效率工作流、AI 入门学习、产品实践和内容选题。

- Generates five script angles: practical efficiency, pain-point empathy, suspense/reversal, before/after contrast, and trend-jacking.
- Analyzes reference scripts for structure, hooks, and reusable phrasing.
- Uses the bundled `references/` library for narrative frameworks, style guidance, psychological triggers, and trend notes.
- Each script includes a title, value proposition, framework, trend angle, psychological hooks, full voiceover, visual suggestions, estimated duration, and production difficulty.
- Useful for AI tool tutorials, productivity workflows, AI learning content, product practice, and content ideation.

## Directory / 目录结构

```text
.
├── SKILL.md                         # Skill instructions / Skill 主指令
├── references/
│   ├── framework.md                 # Narrative frameworks / 爆款叙事框架
│   ├── hot.md                       # Trend notes / 热点库
│   ├── styles.md                    # Persona and style guide / 人设与风格指南
│   └── triggers.md                  # Psychological triggers / 心理触发点手册
└── drafts/                          # Example generated drafts / 示例脚本草稿
```

## Installation / 安装方式

Copy this folder into your local skills directory:

将本目录复制到你的本地 skills 目录：

```bash
cp -R ai-script-generation ~/.codex/skills/
```

If you use Claude-style skill loading, copy it into the corresponding `.claude/skills/` directory:

如果你使用 Claude 风格的 skill 目录，也可以复制到对应的 `.claude/skills/`：

```bash
cp -R ai-script-generation .claude/skills/
```

After installation, restart or reload your agent so it can discover the skill.

安装后请重启或刷新你的 agent，让它重新发现该 skill。

## Usage / 使用方式

Ask for a short-video script and provide a topic. Reference material is optional.

告诉 agent 你要创作的短视频主题即可，也可以附上参考脚本或案例。

Example prompts:

示例提示词：

```text
帮我想个关于如何用 AI 做 PPT 的短视频脚本，要 5 个不同角度。
```

```text
我需要一个 30 秒的小红书教程脚本，主题是 AI 绘画入门，要让人看完想收藏。
```

```text
Write five short-video scripts about using AI to summarize meetings. Make them practical and suitable for social platforms.
```

## Output / 输出内容

The skill returns:

该 skill 会输出：

- Analysis summary / 分析摘要
- Five script concepts / 5 个脚本方案
- Hook and psychological trigger analysis / 钩子与心理触发点
- Full voiceover script / 完整口播脚本
- Visual suggestions / 画面建议
- Duration estimate / 预估时长
- Production difficulty / 制作难度
- Practical creator notes / 创作建议

## Notes / 注意事项

- Scripts are optimized for 30-45 seconds of spoken delivery.
- The default tone is practical, conversational, and creator-friendly.
- Avoid overpromising outcomes or using sensitive/unsafe claims.
- Keep trend references fresh by updating `references/hot.md`.

- 脚本默认控制在 30-45 秒口播时长。
- 默认语气为实用、口语化、适合短视频创作者表达。
- 避免过度承诺、违规话术和敏感表达。
- 建议定期更新 `references/hot.md`，保持热点库新鲜。

## License / 许可

No license has been specified yet. Add one if you want to define reuse terms.

当前尚未指定开源许可证。如需明确复用范围，可以后续补充许可证。
