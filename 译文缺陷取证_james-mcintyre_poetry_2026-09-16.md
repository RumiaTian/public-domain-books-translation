# 译文缺陷取证：james-mcintyre_poetry（2026-09-16，阶段三审校挂起件）

**结论先行**：`译文/poetry.zh-CN.md`（交付物，CSV 对应产物）只覆盖 `原文/poetry.md` 的 **71.9%**；
`译文/poetry_part1..5.zh-CN.md`（5 个分片）合计覆盖 **93.5%**。交付物是**未完成的中间产物**，
分片在交付物落盘之后才完成且**从未合并**。本书**挂起不予审校**（不写 C 级报告以免把"未完成产物"
误标为"已审"）；不做任何文件修改（审核阶段红线）。

## 一、实测数据（只读复算）

| 指标 | poetry.zh-CN.md（交付物） | part1–5 合计 |
|---|---|---|
| ===Original=== 块数 | 1319（O=C 对称） | 1602 |
| 源文覆盖（归一化后字符级） | 162,238 / 224,688 = **71.9%** | 210,953 / 224,688 = **93.5%** |
| 英文块能在源文中逐字命中 | 1133/1319 = 86% | 1579/1602 = 98.6% |
| 十分位覆盖（源文 0→100%） | 0.94 0.78 0.94 0.95 0.74 **0.00** 0.66 0.61 0.72 0.85 | 全部 0.93–0.98 |
| 段数（预检脚本口径） | EN=6471 vs CN=6340（**中译少 130 段**） | — |

- 交付物第 6 十分位（源文中段约 50–60% 位置）覆盖率 **0.00**——中间存在整段空洞；第 7–9 十分位
  覆盖率 0.61–0.72，散布近 54 处 >200 字符的源文内容在交付物中完全没有（英文块与中文块均无）。
- 分片与交付物的重叠率：part1 100%、part2 100%、part3 26%、part4 69%、part5 85%
  —— 后段（中后部）大范围缺失，与十分位数据一致。

## 二、时间线（mtime 取证）

| 时间（2026-09-09） | 文件 | 事件 |
|---|---|---|
| 20:50 | endnotes.zh-CN.md | 尾注完成 |
| 21:02 | poetry_part2 | 分片 2 落盘 |
| 21:35 | poetry_part1 | 分片 1 落盘 |
| **21:38** | **poetry.zh-CN.md** | **交付物落盘（提前收工）** |
| **21:38** | **translation_queue.csv** | **随即置 done** |
| 21:44 / 21:46 / 21:46 | poetry_part3 / part5 / part4 | 分片 3–5 才落盘（晚于交付物与 done 置位） |

→ 交付物与分片是两套独立产出；分片（覆盖率 93.5%）完成时间晚于 done 置位，未回并。

## 三、结构性异常

1. `poetry.zh-CN.md` 以 `## Endnotes / 尾注` 开头（整份文件 187 个 `##` 标题），与独立
   `endnotes.md` 内容重复出现于篇首。
2. 分片并集自身仍有 17 处 >150 字符的源文缺口（例：`robertfleminggourley…` 传记注 1150 字、
   `thomascampbellpreface…` 1958 字），需核为"散文注/标题等版式内容未译"还是真实缺译——
   重修时一并处置。

## 四、建议处置（需翻译阶段执行，本审校阶段不代行）

1. **首选**：以 part1→part5 顺序合并重建 `poetry.zh-CN.md`（分片为源文位置切片、彼此基本不重叠、
   块级结构完整），再补译上节缺口（约 6.5% 源文，多为散文注）并复跑 check_bilingual.py；
   完成后重新入审。
2. **备选**：将 `poetry.md` 重列入翻译队列按超大文件切片流程重译。
3. 无论哪种，处置完成后需同步 `translation_queue.csv` 状态语义（poetry.md 的 done 应视为未完成）。

## 五、复算命令（可复现）

```bash
# 源文覆盖与十分位（在 翻译项目/james-mcintyre_poetry/ 下）
python - <<'EOF'
import re
def norm(s): return re.sub(r'[^0-9A-Za-z\u4e00-\u9fff]','',s).lower()
src = norm(open('原文/poetry.md', encoding='utf-8').read())
def blocks(p):
    t = open(p, encoding='utf-8').read()
    return re.findall(r'===Original===(.*?)===Chinese===', t, re.S)
def cov(bs):
    c = bytearray(len(src))
    for b in bs:
        nb = norm(b); i = src.find(nb)
        if nb and i >= 0: c[i:i+len(nb)] = b'\x01'*len(nb)
    return c
full = cov(blocks('译文/poetry.zh-CN.md')); parts = []
for i in range(1,6): parts += blocks(f'译文/poetry_part{i}.zh-CN.md')
n=len(src)
print('full %.3f' % (sum(full)/n), 'parts %.3f' % (sum(cov(parts))/n))
EOF
```

**出具**：阶段三审核调度（主 Agent），2026-09-16。证据均来自只读复算；未改动 译文/、原文/、
术语表.md、translation_queue.csv、项目说明.md、Plan.md 任何既有文件。
