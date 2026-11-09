# LGD 仓库基线模板（lgd-repo-template）

本仓是 LGD 三账号体系的**统一仓库基线模板包**。新建仓库时按本包初始化，保证"有籍、有证、有门禁"三律在每个仓都落地。

## 包里有什么

| 文件 | 作用 |
|---|---|
| `AGENTS.md` | 10 席 Agent 职责与 L0–L4 权限铁律 |
| `SECURITY.md` | 漏洞上报与供应链安全基线 |
| `CONTRIBUTING.md` | 提交规范与 PR 要求 |
| `CODEOWNERS` | 默认审阅人，兜住"PR 无人审"的缺口 |
| `LICENSE` | MIT（可按仓替换，但不得为空） |
| `.github/dependabot.yml` | 依赖升级自动通道 |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR 必须填证据字段 |
| `.github/workflows/ci.yml` | 调用可复用自检流水线 |
| `.github/workflows/self-check.yml` | 可复用流水线本体（工作流名 `LGD Self Check`） |
| `rulesets/main-protection.json` | 默认分支保护规则（公开仓可直接套用） |
| `docs/evidence-record-template.md` | 14 字段证据模板 |

## 初始化步骤

1. 以本仓为模板新建目标仓（或复制本包内容）。
2. 改 `CODEOWNERS` 里的账号为实际所有者。
3. 改 `.github/dependabot.yml` 的 `package-ecosystem` 为本仓实际技术栈。
4. 套 `rulesets/main-protection.json`（**注意：私有仓在 GitHub Free 上不支持，需 Pro/Team**）。
5. 跑一次 `ci.yml`，确认 `LGD Self Check` 绿灯后再提交业务代码。

## 已知能力边界（重要，不要误传）

- **私有仓在 Free 计划下无法配置分支保护与 Ruleset**（实测 403：`Upgrade to GitHub Pro or make this repository public to enable this feature.`）。
- **组织级 Ruleset 需要 GitHub Team**（实测 403：`Upgrade to GitHub Team to enable this feature.`）。
- 因此本模板的"门禁"部分，**在 Free 计划下只对公开仓生效**；私有仓的门禁要等付费或转公开。

## 许可证

本模板包代码部分 MIT；文档部分保持 CC-BY-4.0 口径，与 LGD 其他发布物一致。
