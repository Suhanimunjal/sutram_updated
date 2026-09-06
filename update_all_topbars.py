#!/usr/bin/env python3
"""
Update header topbar across all pages in pages/
Left side: IGDTUW banner
Right side: Partner logos (Emblem, ISEA, C-DAC, NFSU, MANIT Bhopal, IIIT Sonepat, GTU)
"""
import glob
import os
import re

TOPBAR_LEFT_NEW = """        <div class="topbar-left">
          <a href="index.html" class="topbar-igdtuw-link" aria-label="Indira Gandhi Delhi Technical University for Women" title="Indira Gandhi Delhi Technical University for Women">
            <img class="igdtuw-banner-img theme-logo-light" src="../assets/images/partners/igdtuw_header_hd.png" alt="Indira Gandhi Delhi Technical University for Women" />
            <img class="igdtuw-banner-img theme-logo-dark" src="../assets/images/partners/igdtuw_header_hd_light.png" alt="Indira Gandhi Delhi Technical University for Women" />
          </a>
        </div>"""

TOPBAR_RIGHT_NEW = """        <div class="topbar-right">
          <div class="topbar-partner-logos">
            <img class="partner-logo emblem-logo" src="../assets/images/partners/Emblem_of_India_with_transparent_background.png" alt="Government of India emblem" title="Government of India" />
            <img class="partner-logo isea-logo" src="../assets/images/partners/isea_logo.png" alt="ISEA logo" title="Information Security Education and Awareness (ISEA)" />
            <img class="partner-logo cdac-logo" src="../assets/images/logos/cdac.png" alt="C-DAC" title="Centre for Development of Advanced Computing (C-DAC)" />
            <img class="partner-logo nfsu-logo" src="../assets/images/logos/nfsu_logo.png" alt="NFSU" title="National Forensic Sciences University (NFSU)" />
            <img class="partner-logo mnit-logo" src="../assets/images/logos/mnit_bhopal.png" alt="MANIT Bhopal" title="Maulana Azad National Institute of Technology, Bhopal" />
            <img class="partner-logo iiit-logo" src="../assets/images/logos/iiit_sonipat.png" alt="IIIT Sonepat" title="Indian Institute of Information Technology, Sonepat" />
            <img class="partner-logo gtu-logo" src="../assets/images/logos/gtu.png" alt="GTU" title="Gujarat Technological University (GTU)" />
          </div>
          <a class="login-btn" href="login.html">Login</a>
        </div>"""

pages_dir = r"d:\sutram_new_final_group\Sutram_2026\pages"
html_files = [p for p in glob.glob(os.path.join(pages_dir, "*.html"))
              if os.path.basename(p) not in ["login.html", "registration.html", "404.html"]]

topbar_left_pattern = re.compile(
    r'<div class="topbar-left">\s*<a href="index\.html"[^>]*>\s*<img class="igdtuw-image"[^>]*>\s*</a>\s*</div>',
    re.DOTALL
)

topbar_right_pattern = re.compile(
    r'<div class="topbar-right">\s*<img class="logo-image"[\s\S]*?<a class="login-btn" href="login\.html">Login</a>\s*</div>',
    re.DOTALL
)

for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = topbar_left_pattern.sub(TOPBAR_LEFT_NEW, content)
    new_content = topbar_right_pattern.sub(TOPBAR_RIGHT_NEW, new_content)

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fname}")
    else:
        print(f"No changes needed or already updated: {fname}")
