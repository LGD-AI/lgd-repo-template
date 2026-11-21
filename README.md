# LGD repo template

新建仓库时复制本仓的治理基线，避免每个新仓再补一遍课。

## 一次性动作（建仓后 5 分钟）

1. 复制 `.github/`、`SECURITY.md` 到新仓（`workflows/lgd-ci.yml` 里的 SHA 保持与 `LGD-AI/lgd-ci` 当前 HEAD 一致）。
2. 建 `lgd-standard-gate` ruleset：deletion + non_fast_forward + pull_request（0 审批、dismiss stale reviews、required thread resolution）+ required_linear_history，allow_merge_methods 只留 squash/rebase，bypass `RepositoryRole 5 / always`。
3. 仓设置：`allow_squash_merge=true`、`allow_merge_commit=false`、`allow_rebase_merge=true`、`delete_branch_on_merge=true`、`allow_auto_merge=true`。
4. 打开 private vulnerability reporting、开启 Discussions、开启 immutable releases。
5. 有真实业务测试时，`lgd-ci.yml` 里把 `run-tests` 打开；否则保持 `false`（业务测试留给自己仓内的 CI）。

## 硬规则（血泪总结）

- **任何"必需检查"都必须是某个 workflow 真会产出的 context**。没有产出物的必需检查 = 永久红灯 = 合并链瘫痪（`repo-gate` 就是这么把 5 个仓锁死的）。
- **不要单独打开 `sha_pinning_required`**。它必须与"全仓 action 引用迁移到 40 位 SHA"同步做，否则作业在 `Set up job` 阶段就判死。
- **不要把 `strict`（必须与基分支同步）打开**。单人 + Dependabot 场景下，每合并一个 PR 其余全部 BEHIND，队列永远追不上。
- 共享 CI 只做布局与 JSON 卫生；业务测试留在各仓自有 CI，否则必然长期红一片。