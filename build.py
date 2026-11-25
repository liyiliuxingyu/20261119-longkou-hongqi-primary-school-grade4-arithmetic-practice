"""Rebuild the printable worksheet and the answer key with XeLaTeX."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "四年级计算_排版源码.tex"
EDITIONS = (("四年级计算_试题版.pdf", False), ("四年级计算_答案版.pdf", True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build",
                        help="output directory (default: build/ next to this script)")
    args = parser.parse_args()
    for executable in ("xelatex", "xdvipdfmx"):
        if shutil.which(executable) is None:
            parser.exit(1, f"Missing {executable}. Install TeX Live and add its bin directory to PATH.\n")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", "1795046400")  # 2026-11-19 00:00 UTC
    env.update(FORCE_SOURCE_DATE="1", TZ="UTC")

    with tempfile.TemporaryDirectory(dir=output) as tmp:
        staging = Path(tmp)
        for filename, answers in EDITIONS:
            work = staging / ("answers" if answers else "questions")
            work.mkdir()
            shutil.copyfile(SOURCE, work / "worksheet.tex")
            prefix = r"\def\PrintAnswers{1}" if answers else ""
            (work / "main.tex").write_text(prefix + r"\input{worksheet.tex}" + "\n",
                                           encoding="utf-8")
            for _ in range(2):
                subprocess.run(["xelatex", "-no-pdf", "-interaction=nonstopmode",
                                "-halt-on-error", "-file-line-error", "main.tex"],
                               cwd=work, env=env, check=True)
            subprocess.run(["xdvipdfmx", "-f", "lm.map", "-f", "cm.map",
                            "-f", "cmextra.map", "-f", "symbols.map", "-f", "latxfont.map",
                            "-o", "main.pdf", "main.xdv"],
                           cwd=work, env=env, check=True)
            (work / "main.pdf").replace(staging / filename)
        for filename, _ in EDITIONS:
            (staging / filename).replace(output / filename)
            print(output / filename)


if __name__ == "__main__":
    main()
