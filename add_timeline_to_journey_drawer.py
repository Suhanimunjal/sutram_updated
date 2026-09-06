#!/usr/bin/env python3
"""
Add timeline rows inside the Hackathon Journey mobile drawer sublist.
Handles both normal and 'active' class link variants.
Skips files that are already patched.
"""
import os, re, glob

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = glob.glob(os.path.join(pages_dir, "*.html"))

# The timeline block to inject
TIMELINE_INJECT = """\
          <li class="drawer-sublist-divider">Up Next</li>
          <li class="drawer-timeline-row" data-timeline-group="1" data-roll-date="2026-09-10"><span class="drawer-timeline-label">Registration Opens</span><span class="drawer-timeline-value" data-date="2026-08-20">20 Aug 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="1" data-roll-date="2026-09-10"><span class="drawer-timeline-label">Registration Closes</span><span class="drawer-timeline-value" data-date="2026-09-10">10 Sep 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="2" data-roll-date="2026-09-12"><span class="drawer-timeline-label">Problem Statement Release</span><span class="drawer-timeline-value" data-date="2026-09-12">12 Sep 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="3" data-roll-date="2026-09-22"><span class="drawer-timeline-label">Idea / Proposal Submission</span><span class="drawer-timeline-value" data-date="2026-09-22">22 Sep 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="4" data-roll-date="2026-09-28"><span class="drawer-timeline-label">Shortlisting</span><span class="drawer-timeline-value" data-date="2026-09-28">28 Sep 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="5" data-roll-date="2026-10-10"><span class="drawer-timeline-label">Mentorship</span><span class="drawer-timeline-value" data-date="2026-10-10">10 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="6" data-roll-date="2026-10-18"><span class="drawer-timeline-label">Prototype / PPT Submission</span><span class="drawer-timeline-value" data-date="2026-10-18">18 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="7" data-roll-date="2026-10-28"><span class="drawer-timeline-label">Grand Finale</span><span class="drawer-timeline-value" data-date="2026-10-25">25 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="7" data-roll-date="2026-10-28"><span class="drawer-timeline-label">Winner Announcement</span><span class="drawer-timeline-value" data-date="2026-10-28">28 Oct 2026</span></li>
          <li class="drawer-timeline-empty" data-timeline-empty hidden>All milestones completed. Thank you for being part of SUTRAM 2026!</li>
          <li><a href="timeline.html">View Full Timeline ↗</a></li>"""

# More flexible pattern: match the last <li> inside Hackathon Journey drawer
# that links to results.html (with or without active class), followed by </ul>
# Uses a lookahead for the Timeline drawer-group that follows
PATTERN = re.compile(
    r'(<li>\s*<a(?:[^>]*)href="results\.html"[^>]*>[^<]*</a>\s*</li>)'
    r'(\s*</ul>\s*</li>)'
    r'(?=\s*(?:<li class="drawer-group">|<li class="drawer-group open">)\s*<button[^>]*>Timeline)',
    re.DOTALL
)

changed = []
skipped = []
no_match = []

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already patched
    if 'drawer-sublist-divider' in content and 'Up Next' in content:
        skipped.append(os.path.basename(fpath))
        continue

    new_content = PATTERN.sub(
        lambda m: m.group(1) + "\n" + TIMELINE_INJECT + "\n" + m.group(2),
        content
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed.append(os.path.basename(fpath))
    else:
        no_match.append(os.path.basename(fpath))

print(f"Updated {len(changed)} files:")
for name in changed:
    print(f"  + {name}")

if skipped:
    print(f"\nAlready patched ({len(skipped)}):")
    for name in skipped:
        print(f"  ~ {name}")

if no_match:
    print(f"\nNo match ({len(no_match)}):")
    for name in no_match:
        print(f"  - {name}")
