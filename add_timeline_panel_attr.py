#!/usr/bin/env python3
"""
Add data-timeline-panel to the Hackathon Journey drawer-sublist.
Uses a simple approach: find "Hackathon Journey" button followed by
<ul class="drawer-sublist"> and add the attribute.
"""
import os, re, glob

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = glob.glob(os.path.join(pages_dir, "*.html"))

# Pattern: Hackathon Journey button followed (within ~200 chars) by the ul tag
PATTERN = re.compile(
    r'(>Hackathon Journey\s*<span[^>]*>▾</span></button>\s*)'
    r'(<ul class="drawer-sublist">)',
    re.DOTALL
)

changed = []
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if 'drawer-sublist-divider' not in content:
        continue  # not a patched journey drawer page

    if '>Hackathon Journey' not in content:
        continue

    new_content = PATTERN.sub(
        lambda m: m.group(1) + '<ul class="drawer-sublist" data-timeline-panel>',
        content
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed.append(os.path.basename(fpath))
    else:
        # Try alternate: button may have aria-expanded="true" (active pages)
        PATTERN2 = re.compile(
            r'(>Hackathon Journey\s*<span[^>]*>▾</span></button>)\s*\r?\n(\s*)(<ul class="drawer-sublist">)',
            re.DOTALL
        )
        new_content2 = PATTERN2.sub(
            lambda m: m.group(1) + '\n' + m.group(2) + '<ul class="drawer-sublist" data-timeline-panel>',
            content
        )
        if new_content2 != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content2)
            changed.append(os.path.basename(fpath) + " (alt)")

print(f"Updated {len(changed)} files:")
for name in changed:
    print(f"  + {name}")
