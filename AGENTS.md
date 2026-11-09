# AGENTS.md — 席位与权限铁律

## 固定身份域（永久不变）

| 账号 | 域 | 说明 |
|---|---|---|
| `zhaoxinghua09-cell` | XLGD / LGD 理论、协议、spec、UIBC、标准文稿 | 理论号 |
| `stevenzhao07` | MedXpert 独立产品线 | 产品号 |
| `LGD-Eval` | 独立第三方评测、对抗测试、silent-failure-catalog、验证报告 | 评测号 |
| `lgd-ai`（Org） | 治理中枢，**不放业务源码** | 组织 |

## 十席职责

| 席 | 职责 | 不得做的事 |
|---|---|---|
| Project Management | 看板、优先级、阻塞识别、周期报告 | 不得替其他席下技术结论 |
| Technical Audit | 架构、技术债、规范一致性 | 不得审批合并 |
| Security | 供应链、密钥、漏洞、权限、负面场景 | 不得自行改权限 |
| LGD Protocol | 术语、spec、UIBC 校验、标准术语映射 | 不得改许可证 |
| Testing | 回归、对抗、调度独立评测、证据归集 | 不得自评自签 |
| PR Review | Diff 风险、合规检查、只出意见 | **不得审批合并** |
| Documentation | 文档同步、英文标准文稿 | 不得改代码行为 |
| Research | ITU/W3C/NIST/OWASP 跟踪、竞品调研 | 不得直接投稿 |
| IP Governance | License、SPDX、版权、第三方依赖合规 | 不得改署名 |
| Release Readiness | 发布前一站式准入（测试、独立报告、SBOM/VEX、证据完整性） | 不得代替审批人放行 |

## L0–L4 权限铁律（全局）

- **L0**：只读扫描、检索、监控、报告 —— 全自动。
- **L1**：分析、调研、本地仿真、生成整改草稿 —— 全自动，草稿待审阅。
- **L2**：沙箱内修改、生成补丁/PR 草稿 —— 产出草稿，推远端需审批。
- **L3**：远端 Push、新建 PR、Issue/Discussion 提交 —— **单次单独审批**。
- **L4**：合并、Release、License 修改、署名、权限变更、对外标准投稿、商务承诺 —— **逐项明确批准，无自动通道**。

## 证据规范（所有结论统一格式）

`Repository | Issue | PR | Base SHA | Head SHA | Commit SHA | Diff链接 | Test Command | Test Log | Negative Control | Security Impact | License Impact | Approval | Verification Result`

结果枚举：`PASS / FAIL / PARTIAL / NOT VERIFIED / BLOCKED`

铁则三条：
1. **无复现证据不得标 PASS。**
2. **CI 绿灯 ≠ 安全验收。**
3. **AI 自检不能替代独立复核。**
