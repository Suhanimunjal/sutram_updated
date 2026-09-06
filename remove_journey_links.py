#!/usr/bin/env python3
"""
Remove 'View Full Journey' links (and surrounding divider) from all HTML nav menus.
"""
import os, re, glob

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = glob.glob(os.path.join(pages_dir, "*.html"))

# Patterns to remove (desktop dropdown and mobile drawer variants)
# 1. Desktop: divider + link block
desktop_pattern = re.compile(
    r'\s*<div class="nav-dropdown-divider"></div>\s*\n\s*<a[^>]*href="journey\.html"[^>]*>View Full Journey[^<]*</a>',
    re.MULTILINE
)

# 2. Mobile drawer: <li><a href="journey.html">View Full Journey...</a></li>
drawer_pattern = re.compile(
    r'\s*<li>\s*<a(?:[^>]*)href="journey\.html"[^>]*>View Full Journey[^<]*</a>\s*</li>',
    re.MULTILINE
)

changed = []
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = desktop_pattern.sub("", content)
    new_content = drawer_pattern.sub("", new_content)

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed.append(os.path.basename(fpath))

print(f"Updated {len(changed)} files:")
for name in changed:
    print(f"  - {name}")
