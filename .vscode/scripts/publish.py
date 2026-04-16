#!/usr/bin/env python3
"""Prepare a Hugo draft post for publishing.

Updates front matter to:
- Set draft: false
- Set date to the current UTC time
- Add cover block with placeholder values (if missing)
- Add summary with placeholder value (if missing)
"""

import re
import sys
from datetime import datetime, timezone


def main():
    if len(sys.argv) < 2:
        print("Usage: publish.py <file>")
        sys.exit(1)

    filepath = sys.argv[1]

    with open(filepath, "r") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        print(f"No YAML front matter found in {filepath}")
        sys.exit(1)

    fm = match.group(1)
    body = content[match.end():]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

    # draft → false
    if re.search(r"^draft:", fm, re.MULTILINE):
        fm = re.sub(r"^draft:\s*.*$", "draft: false", fm, flags=re.MULTILINE)
    else:
        fm += "\ndraft: false"

    # set publish date
    if re.search(r"^date:", fm, re.MULTILINE):
        fm = re.sub(r"^date:\s*.*$", f"date: {now}", fm, flags=re.MULTILINE)
    else:
        fm += f"\ndate: {now}"

    # add cover block if absent
    if not re.search(r"^cover:", fm, re.MULTILINE):
        fm += '\ncover:\n  image: "fill me in"\n  alt: "fill me in"\n  relative: false'

    # add summary if absent
    if not re.search(r"^summary:", fm, re.MULTILINE):
        fm += '\nsummary: "fill me in"'

    with open(filepath, "w") as f:
        f.write(f"---\n{fm}\n---{body}")

    print(f"✓ Published: {filepath}")


if __name__ == "__main__":
    main()
