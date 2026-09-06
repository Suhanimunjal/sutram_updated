import glob
import re
import os

files = glob.glob(r'd:\sutram_new_final_group\Sutram_2026\pages\*.html')
print(f"Checking {len(files)} files...")

updated_count = 0

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Primary desktop navigation dropdown for "Hackathon Journey"
    # Find the nav-item containing "Hackathon Journey"
    def repl_desktop_nav(match):
        block = match.group(0)
        # Check active status
        is_active_prob = 'active' in re.search(r'<a[^>]*href="problem-statements\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="problem-statements\.html"[^>]*>', block) else False
        is_active_reg = 'active' in re.search(r'<a[^>]*href="registration\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="registration\.html"[^>]*>', block) else False
        is_active_eval = 'active' in re.search(r'<a[^>]*href="evaluation\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="evaluation\.html"[^>]*>', block) else False
        is_active_res = 'active' in re.search(r'<a[^>]*href="results\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="results\.html"[^>]*>', block) else False
        is_active_jour = 'active' in re.search(r'<a[^>]*href="journey\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="journey\.html"[^>]*>', block) else False

        prob_cls = ' class="active"' if is_active_prob else ''
        reg_cls = ' class="active"' if is_active_reg else ''
        eval_cls = ' class="active"' if is_active_eval else ''
        res_cls = ' class="active"' if is_active_res else ''
        jour_cls = ' active' if is_active_jour else ''

        new_dropdown = f'''<div class="nav-dropdown-menu">
        <a{prob_cls} href="problem-statements.html">Problem Statements</a>
        <a{reg_cls} href="registration.html">Registration and PPT Submission</a>
        <a{eval_cls} href="evaluation.html">Evaluation</a>
        <a{res_cls} href="results.html">Results</a>
        <div class="nav-dropdown-divider"></div>
        <a class="nav-dropdown-link{jour_cls}" href="journey.html">View Full Journey \u2197</a>
      </div>'''
        return new_dropdown

    content = re.sub(
        r'<div class="nav-dropdown-menu">\s*<a[^>]*href="problem-statements\.html"[^>]*>.*?View Full Journey [^<]*</a>\s*</div>',
        repl_desktop_nav,
        content,
        flags=re.DOTALL
    )

    # 2. Drawer sublist for "Hackathon Journey"
    def repl_drawer_nav(match):
        block = match.group(0)
        is_active_prob = 'active' in re.search(r'<a[^>]*href="problem-statements\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="problem-statements\.html"[^>]*>', block) else False
        is_active_reg = 'active' in re.search(r'<a[^>]*href="registration\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="registration\.html"[^>]*>', block) else False
        is_active_eval = 'active' in re.search(r'<a[^>]*href="evaluation\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="evaluation\.html"[^>]*>', block) else False
        is_active_res = 'active' in re.search(r'<a[^>]*href="results\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="results\.html"[^>]*>', block) else False
        is_active_jour = 'active' in re.search(r'<a[^>]*href="journey\.html"[^>]*>', block).group(0) if re.search(r'<a[^>]*href="journey\.html"[^>]*>', block) else False

        prob_cls = ' class="active"' if is_active_prob else ''
        reg_cls = ' class="active"' if is_active_reg else ''
        eval_cls = ' class="active"' if is_active_eval else ''
        res_cls = ' class="active"' if is_active_res else ''
        jour_cls = ' class="active"' if is_active_jour else ''

        new_drawer = f'''<ul class="drawer-sublist">
          <li class="drawer-sublist-label">Hackathon Journey</li>
          <li><a{prob_cls} href="problem-statements.html">Problem Statements</a></li>
          <li><a{reg_cls} href="registration.html">Registration and PPT Submission</a></li>
          <li><a{eval_cls} href="evaluation.html">Evaluation</a></li>
          <li><a{res_cls} href="results.html">Results</a></li>
          <li><a{jour_cls} href="journey.html">View Full Journey \u2197</a></li>
        </ul>'''
        return new_drawer

    content = re.sub(
        r'<ul class="drawer-sublist">\s*<li class="drawer-sublist-label">Hackathon Journey</li>.*?View Full Journey [^<]*</a></li>\s*</ul>',
        repl_drawer_nav,
        content,
        flags=re.DOTALL
    )

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated {os.path.basename(fpath)}")

print(f"Successfully updated {updated_count} files.")
