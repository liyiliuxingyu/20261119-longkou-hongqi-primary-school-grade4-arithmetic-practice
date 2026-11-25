# 20261119龙口市红旗小学四年级计算练习试题

[高清试题版（PDF）](四年级计算_试题版.pdf) · [红笔答案与评分细则（PDF）](四年级计算_答案版.pdf)

本练习共 12 题，按原稿顺序分三栏排版。试题版共一页，采用 A4 纵向纸张，留有竖式和脱式演算空间。答案版第一页在原题下方列出竖式与脱式步骤，第二页附百分制评分细则。竖式计算 6 题，共 40 分。脱式计算 6 题，共 60 分。

## 工程文件

| 文件 | 用途 |
| --- | --- |
| [LaTeX 源码](四年级计算_排版源码.tex) | 编辑两版共用的题目、答案、评分细则及版式 |
| [构建脚本](build.py) | 一次生成试题版和答案版 |

## 重新生成 PDF

安装 Python 3.7 或更高版本，以及带中文支持的 TeX Live 或 MacTeX。将 Python、`xelatex` 和 `xdvipdfmx` 的可执行文件目录加入系统的 `PATH`。排版使用 `ctexart`、`xeCJK`、`fontspec`、`geometry`、`amsmath`、`tikz`（PGF），以及 TeX Live 的 Fandol 中文字体、Latin Modern 和 Computer Modern 字体。完整安装 TeX Live 已包含上述依赖。

在工程根目录运行下列命令。Windows 可用 `py -3` 代替 `python3`。

```console
python3 build.py
```

生成的两份 PDF 位于 `build/`。如需指定输出目录，可运行 `python3 build.py --output my-pdfs`。脚本对每个版本独立运行两遍 XeLaTeX，再将 XDV 转为 PDF。它通过源码已有的 `\PrintAnswers` 开关生成答案版。工程根目录归档的两份 PDF 可直接打印，默认构建会将新文件写入单独的目录。

构建时间戳默认为 2026 年 11 月 19 日 00:00 UTC，可通过环境变量 `SOURCE_DATE_EPOCH` 指定其他时间戳。不同版本的 TeX 引擎、宏包或字体可能影响分页、字形和 PDF 字节内容。

## 复编核验

用同一套 TeX 工具在两个临时目录分别执行上述脚本，两次生成的试题版和答案版分别通过 SHA-256 一致性校验。将重编文件与工程根目录的归档文件逐页按 300 dpi 栅格化比对，试题版一页及答案版两页的像素完全一致，逐页提取的文本也一致。
