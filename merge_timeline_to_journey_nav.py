#!/usr/bin/env python3
"""
Merge the desktop Timeline nav-item into the Hackathon Journey dropdown,
then remove the standalone Timeline nav-item across all pages.
"""
import os, re, glob

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = glob.glob(os.path.join(pages_dir, "*.html"))

# The timeline block to inject into the Hackathon Journey dropdown
# (uses nav-timeline-row divs + nav-timeline-menu style, with a divider label)
TIMELINE_BLOCK = """\n        <div class="nav-dropdown-divider"></div>
        <span class="nav-dropdown-section-label">Up Next</span>
        <div class="nav-dropdown-menu nav-timeline-inline" data-timeline-panel>
          <div class="nav-timeline-row" data-timeline-group="1" data-roll-date="2026-10-05"><span class="nav-timeline-label">Registration / Idea Submission Opens</span><span class="nav-timeline-value" data-date="2026-09-07">7 Sep 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="1" data-roll-date="2026-10-05"><span class="nav-timeline-label">Registration / Idea Submission Closes</span><span class="nav-timeline-value" data-date="2026-10-05">5 Oct 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="2" data-roll-date="2026-10-25"><span class="nav-timeline-label">First Round Results</span><span class="nav-timeline-value" data-date="2026-10-25">25 Oct 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="3" data-roll-date="2026-10-28"><span class="nav-timeline-label">Problem Statement Release</span><span class="nav-timeline-value" data-date="2026-10-28">28 Oct 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="4" data-roll-date="2026-11-10"><span class="nav-timeline-label">Mentorship Sessions</span><span class="nav-timeline-value" data-date="2026-11-01">1–10 Nov 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="5" data-roll-date="2026-11-20"><span class="nav-timeline-label">Prototype / PPT Submission</span><span class="nav-timeline-value" data-date="2026-11-20">20 Nov 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="6" data-roll-date="2026-12-05"><span class="nav-timeline-label">Final 25 Teams Selected</span><span class="nav-timeline-value" data-date="2026-12-05">5 Dec 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="7" data-roll-date="2026-12-27"><span class="nav-timeline-label">Hackathon Finale</span><span class="nav-timeline-value" data-date="2026-12-26">26–27 Dec 2026</span></div>
          <div class="nav-timeline-row" data-timeline-group="7" data-roll-date="2026-12-27"><span class="nav-timeline-label">Winner Announcement</span><span class="nav-timeline-value" data-date="2026-12-27">27 Dec 2026</span></div>
          <p class="nav-timeline-empty" data-timeline-empty hidden>All milestones completed. Thank you for being part of SUTRAM 2026!</p>
        </div>
        <a class="nav-dropdown-link" href="timeline.html">View Full Timeline ↗</a>"""

# Pattern: match the closing of Hackathon Journey dropdown's </div></div>
# specifically the </div> that closes nav-dropdown-menu, then </div> for nav-item
# We find: results.html link followed by closing </div>\n  </div>
JOURNEY_CLOSE_PATTERN = re.compile(
    r'(<a href="results\.html">[^<]*</a>)'
    r'(\s*</div>\s*</div>)'
    r'(?=\s*\n\s*<div class="nav-item">[\s\S]*?Timeline)',
    re.DOTALL
)

# Pattern to remove the entire standalone Timeline nav-item block
TIMELINE_NAV_PATTERN = re.compile(
    r'\s*<div class="nav-item">\s*\n\s*<button[^>]*>Timeline\s*<span[^>]*>▾</span></button>\s*\n'
    r'[\s\S]*?'
    r'</div>\s*\n\s*</div>(?=\s*\n\s*<a[^>]*>FAQ)',
    re.DOTALL
)

changed = []
skipped = []

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already done (timeline injected, standalone removed)
    if 'nav-dropdown-section-label' in content:
        skipped.append(os.path.basename(fpath))
        continue

    # Step 1: Inject timeline into Journey dropdown
    new_content = JOURNEY_CLOSE_PATTERN.sub(
        lambda m: m.group(1) + TIMELINE_BLOCK + "\n      </div>\n  </div>",
        content
    )

    if new_content == content:
        print(f"  [NO MATCH - journey inject] {os.path.basename(fpath)}")
        continue

    # Step 2: Remove standalone Timeline nav-item
    new_content2 = TIMELINE_NAV_PATTERN.sub("", new_content)

    if new_content2 != new_content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content2)
        changed.append(os.path.basename(fpath))
    else:
        # Still write step 1 changes even if step 2 didn't match
        print(f"  [TIMELINE REMOVE NO MATCH] {os.path.basename(fpath)}")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed.append(os.path.basename(fpath) + " (inject only)")

print(f"\nUpdated {len(changed)} files:")
for name in changed:
    print(f"  + {name}")
if skipped:
    print(f"\nSkipped (already done): {len(skipped)}")
