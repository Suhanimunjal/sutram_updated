#!/usr/bin/env python3
"""
1. In desktop nav: Remove extra "nav-dropdown-menu" class from:
   <div class="nav-dropdown-menu nav-timeline-inline" data-timeline-panel>
   so it becomes:
   <div class="nav-timeline-inline" data-timeline-panel>

2. In mobile drawer:
   a) Update the timeline rows in Hackathon Journey drawer to official dates.
   b) Remove the standalone Timeline drawer group (<li class="drawer-group">...Timeline...</li>).
"""
import glob
import os
import re

DRAWER_TIMELINE_ROWS = """          <li class="drawer-sublist-divider">Up Next</li>
          <li class="drawer-timeline-row" data-timeline-group="1" data-roll-date="2026-10-05"><span class="drawer-timeline-label">Registration / Idea Submission Opens</span><span class="drawer-timeline-value" data-date="2026-09-07">7 Sep 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="1" data-roll-date="2026-10-05"><span class="drawer-timeline-label">Registration / Idea Submission Closes</span><span class="drawer-timeline-value" data-date="2026-10-05">5 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="2" data-roll-date="2026-10-25"><span class="drawer-timeline-label">First Round Results</span><span class="drawer-timeline-value" data-date="2026-10-25">25 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="3" data-roll-date="2026-10-28"><span class="drawer-timeline-label">Problem Statement Release</span><span class="drawer-timeline-value" data-date="2026-10-28">28 Oct 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="4" data-roll-date="2026-11-10"><span class="drawer-timeline-label">Mentorship Sessions</span><span class="drawer-timeline-value" data-date="2026-11-01">1–10 Nov 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="5" data-roll-date="2026-11-20"><span class="drawer-timeline-label">Prototype / PPT Submission</span><span class="drawer-timeline-value" data-date="2026-11-20">20 Nov 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="6" data-roll-date="2026-12-05"><span class="drawer-timeline-label">Final 25 Teams Selected</span><span class="drawer-timeline-value" data-date="2026-12-05">5 Dec 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="7" data-roll-date="2026-12-27"><span class="drawer-timeline-label">Hackathon Finale</span><span class="drawer-timeline-value" data-date="2026-12-26">26–27 Dec 2026</span></li>
          <li class="drawer-timeline-row" data-timeline-group="7" data-roll-date="2026-12-27"><span class="drawer-timeline-label">Winner Announcement</span><span class="drawer-timeline-value" data-date="2026-12-27">27 Dec 2026</span></li>
          <li class="drawer-timeline-empty" data-timeline-empty hidden>All milestones completed. Thank you for being part of SUTRAM 2026!</li>
          <li><a href="timeline.html">View Full Timeline ↗</a></li>"""

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = [p for p in glob.glob(os.path.join(pages_dir, "*.html"))
              if os.path.basename(p) not in ["login.html", "registration.html", "404.html"]]

for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix desktop nav class
    content = content.replace(
        '<div class="nav-dropdown-menu nav-timeline-inline" data-timeline-panel>',
        '<div class="nav-timeline-inline" data-timeline-panel>'
    )

    # 2. Update Hackathon Journey drawer timeline rows:
    # Match from <li class="drawer-sublist-divider">Up Next</li> to <li><a href="timeline.html">View Full Timeline ↗</a></li>
    # inside Hackathon Journey drawer-group
    journey_tl_pattern = re.compile(
        r'<li class="drawer-sublist-divider">Up Next</li>[\s\S]*?<li><a href="timeline\.html">View Full Timeline ↗</a></li>'
    )
    # Only replace the first occurrence in the drawer (or we replace and then remove the second)
    content = journey_tl_pattern.sub(DRAWER_TIMELINE_ROWS, content, count=1)

    # 3. Remove standalone Timeline drawer group:
    # <li class="drawer-group">\s*<button[^>]*>Timeline\s*<span[^>]*>.*?</li>\s*</ul>\s*</li>
    timeline_drawer_pattern = re.compile(
        r'\s*<li class="drawer-group">\s*<button[^>]*class="drawer-group-toggle"[^>]*>Timeline\s*<span[\s\S]*?</ul>\s*</li>',
        re.DOTALL
    )
    content = timeline_drawer_pattern.sub("", content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {fname}")
