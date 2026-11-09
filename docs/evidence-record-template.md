# 证据记录模板（14 字段）

> 铁则：**无复现证据不得标 PASS；CI 绿灯 ≠ 安全验收；AI 自检不能替代独立复核。**
> 没有真值的字段，写 `fields_na` + 为什么没有，**不要填假值**。

| # | 字段 | 填什么 | 本仓无真值时怎么写 |
|---|---|---|---|
| 1 | Repository | `账号/仓名` | — |
| 2 | Issue | Issue 编号或链接 | `fields_na: 无对应 Issue` |
| 3 | PR | PR 编号或链接 | `fields_na: 直推/无 PR` |
| 4 | Base SHA | 变更前 commit | `fields_na: 新建仓无基线` |
| 5 | Head SHA | 变更后 commit | — |
| 6 | Commit SHA | 实际提交 | — |
| 7 | Diff 链接 | GitHub compare URL | `fields_na: 无可比对象` |
| 8 | Test Command | 完整可复制命令 | — |
| 9 | Test Log | 输出或日志链接 | — |
| 10 | Negative Control | 什么情况下这个改动会失效 | `fields_na: 未构造` |
| 11 | Security Impact | 无 / 有（说明） | — |
| 12 | License Impact | 无 / 有（说明） | — |
| 13 | Approval | 谁批的、什么时候、批了什么 | `fields_na: 未触及 L3/L4` |
| 14 | Verification Result | PASS / FAIL / PARTIAL / NOT VERIFIED / BLOCKED | — |

## 示例（已填满）

| 字段 | 值 |
|---|---|
| Repository | lgd-ai/lgd-repo-template |
| Issue | fields_na: 基线初始化，无 Issue |
| PR | #1 |
| Base SHA | fields_na: 首提交无父 |
| Head SHA | 3f2a1c9 |
| Commit SHA | 3f2a1c9 |
| Diff 链接 | https://github.com/lgd-ai/lgd-repo-template/commit/3f2a1c9 |
| Test Command | `python -m pytest -q` |
| Test Log | Actions run #12，PASS |
| Negative Control | 删掉 LICENSE 后 self-check 应 FAIL（已实测 FAIL） |
| Security Impact | 无 |
| License Impact | 新增 MIT 许可证，无冲突 |
| Approval | Steven Zhao 2026-11-09 批：建仓并推送基线 |
| Verification Result | PASS |
