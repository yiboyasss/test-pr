#!/usr/bin/env python3
import os
import datetime

def main():
    # 输出目录：生成到 doc/source/_generated
    out_dir = os.path.join("doc", "source", "_generated")
    os.makedirs(out_dir, exist_ok=True)

    # 每次运行更新一个文件，确保有内容变更，以便能在 PR 中看到新提交
    out_file = os.path.join(out_dir, "auto_generated.txt")
    content = f"Auto-generated at: {datetime.datetime.utcnow().isoformat()}Z\n"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Wrote {out_file}")

if __name__ == "__main__":
    main()