# SECURITY.md — 安全基线与漏洞上报

## 上报

发现本仓或其依赖的安全问题，请**不要**开公开 Issue，走私密渠道：GitHub Security Advisory（Privately report）或邮件联系仓库所有者。

## 基线（每个仓都必须满足）

| 项 | 要求 |
|---|---|
| 依赖告警 | Dependabot alerts **必须开启**（关闭状态下接口返回 403 `alerts are disabled`） |
| 密钥扫描 | Secret scanning **必须开启**（关闭状态下返回 404 `Secret scanning is disabled`） |
| 依赖升级 | 必须有 `.github/dependabot.yml` |
| 工作流固定 | 第三方 action **必须 pin 到 commit SHA**，不得用 `@master`/`@main` |
| 权限最小化 | workflow 必须显式写 `permissions:`，默认 `contents: read` |
| 密钥卫生 | 任何密钥不得提交进仓库；发现即轮换，不是删文件了事 |
| 许可证 | 不得为空，不得为 NOASSERTION 而无说明 |

## 已实测的两条限制（写清，避免误判）

1. 私有仓在 GitHub Free 上无法配置分支保护/Ruleset（403 `Upgrade to GitHub Pro...`）。
2. 组织级 Ruleset 需要 GitHub Team（403 `Upgrade to GitHub Team...`）。

因此本仓若为私有且位于 Free 计划，**门禁不可用**，须在审计报告中记 `NOT VERIFIED`，不得记 PASS。
