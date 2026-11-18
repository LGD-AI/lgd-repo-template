# -*- coding: utf-8 -*-
"""一条命令判定仓库是否达到八项基线（默认查当前仓库，无需网络）。

用法：
    python tools/check_standard.py            # 检查当前目录（本地）
    python tools/check_standard.py --remote owner/repo   # 检查 GitHub 仓（需 GH_TOKEN）

退出码：0 = 8/8 全达标；1 = 有缺项。判定只看文件是否在，不看自述。
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request

ITEMS = [
    ("C1", "LICENSE", "法律上可复用"),
    ("C2", "README.md", "说明是什么、怎么跑、主张上限"),
    ("C3", "EVIDENCE-INDEX.md", "证据分级 L1–L4，零如实写零"),
    ("C4", "STRUCTURE.md", "分层地图与改动代价"),
    ("C5", "SPEC.md", "可对照的契约，含主张上限"),
    ("C6", "tools/", "一条命令可自验"),
    ("C7", "tests/", "第三方可离线复跑"),
    ("C8", ".github/workflows/", "push 即跑"),
]

PATTERNS = {
    "C1": r"(^|/)licen[sc]e(\.(md|txt))?$",
    "C2": r"(^|/)readme(\.(md|txt))?$",
    "C3": r"evidence[-_]index",
    "C4": r"(structure|architecture)\.md$",
    "C5": r"(spec|specification)\.md$",
    "C6": r"^(tools|scripts|bin)/",
    "C7": r"^(tests|test|conformance)/|(^|/)test_.*\.py$",
    "C8": r"^\.github/workflows/",
}


def paths_local(root="."):
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", "__pycache__", "dist", "build")]
        for f in fn:
            out.append(os.path.relpath(os.path.join(dp, f), root).replace("\\", "/").lower())
    return out


def paths_remote(repo):
    tok = os.environ.get("GH_TOKEN", "")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/git/trees/HEAD?recursive=1",
        headers={"Authorization": "Bearer " + tok, "User-Agent": "check-standard"})
    with urllib.request.urlopen(req, timeout=30) as r:
        t = json.loads(r.read().decode())
    return [x["path"].lower() for x in t["tree"]]


def main(argv):
    if argv and argv[0] == "--remote":
        target = argv[1]
        paths = paths_remote(target)
    else:
        target = os.getcwd()
        paths = paths_local()

    miss = []
    for code, label, why in ITEMS:
        ok = any(re.search(PATTERNS[code], p) for p in paths) if code != "C6" else any(re.search(PATTERNS[code], p + "/x") for p in paths)
        if not ok:
            miss.append(f"{code} {label}（{why}）")

    print(f"{target}: {8 - len(miss)}/8")
    if miss:
        print("  缺: " + "；".join(miss))
    return 0 if not miss else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
