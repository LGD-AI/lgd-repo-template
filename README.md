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
| `SPEC.md` | 契约骨架：范围 / 输入 / 输出 / 不变式 / 主张上限 |
| `STRUCTURE.md` | 分层地图 + 改动代价表 |
| `EVIDENCE-INDEX.md` | 证据分级 L1–L4，初始全 0，附升级条件 |
| `tools/check_standard.py` | 一条命令判定本仓是否 8/8 |
| `tests/test_template_integrity.py` | 模板自检：模板自己必须 8/8 |

## 八项基线（本模板的验收口径）

| 项 | 文件 | 判据 |
|---|---|---|
| C1 | `LICENSE` | 法律上可复用 |
| C2 | `README.md` | 是什么、怎么跑、主张上限 |
| C3 | `EVIDENCE-INDEX.md` | 分级有据，零写零 |
| C4 | `STRUCTURE.md` | 分层 + 改动代价 |
| C5 | `SPEC.md` | 可对照的契约 |
| C6 | `tools/` | 一条命令自验 |
| C7 | `tests/` | 第三方可离线复跑 |
| C8 | `.github/workflows/` | push 即跑 |

自检命令：

```bash
python tools/check_standard.py          # 退出码 0 = 8/8，1 = 有缺项
python -m unittest discover tests       # 模板自身完整性
```

## 初始化步骤

1. 以本仓为模板新建目标仓（或复制本包内容）。
2. 改 `CODEOWNERS` 里的账号为实际所有者。
3. 改 `.github/dependabot.yml` 的 `package-ecosystem` 为本仓实际技术栈。
4. 套 `rulesets/main-protection.json`（**注意：私有仓在 GitHub Free 上不支持，需 Pro/Team**）。
5. 填 `SPEC.md` 的"范围 / 不回答的问题 / 主张上限"——**这三处空着，等于没有契约**。
6. 跑 `python tools/check_standard.py` 与 `ci.yml`，确认 8/8 且 `LGD Self Check` 绿灯后再提交业务代码。

## 已知能力边界（重要，不要误传）

- **私有仓在 Free 计划下无法配置分支保护与 Ruleset**（实测 403：`Upgrade to GitHub Pro or make this repository public to enable this feature.`）。
- **组织级 Ruleset 需要 GitHub Team**（实测 403：`Upgrade to GitHub Team to enable this feature.`）。
- 因此本模板的"门禁"部分，**在 Free 计划下只对公开仓生效**；私有仓的门禁要等付费或转公开。
- 模板给的是**结构骨架**，不产生证据。`EVIDENCE-INDEX.md` 里的 `0` 必须由真实执行改写；照模板填非 `0` 即造假，比不填更糟。

## 许可证

本模板包代码部分 MIT；文档部分保持 CC-BY-4.0 口径，与 LGD 其他发布物一致。
