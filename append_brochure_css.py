with open(r'd:\sutram_new_final_group\Sutram_2026\css\style.css', 'r', encoding='utf-8-sig', errors='replace') as f:
    css = f.read()

brochure_css = """

/* ══════════════════════════════════════════════════════════════════
   EVENT BROCHURE DOWNLOAD & VIEWER SHOWCASE
   ══════════════════════════════════════════════════════════════════ */
.brochure-showcase {
  max-width: 980px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.brochure-hero-card {
  background: #ffffff;
  border-radius: 20px;
  border: 1.5px solid rgba(22, 139, 183, 0.16);
  box-shadow: 0 16px 40px rgba(14, 34, 71, 0.08);
  padding: clamp(24px, 4vw, 36px);
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 24px;
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.brochure-hero-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 6px;
  height: 100%;
  background: linear-gradient(180deg, #00b4d8 0%, #2575fc 100%);
}

.brochure-hero-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 48px rgba(14, 34, 71, 0.12);
}

.brochure-badge-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.brochure-format-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 6px;
  background: rgba(220, 38, 38, 0.1);
  color: #dc2626;
  border: 1px solid rgba(220, 38, 38, 0.2);
}

.brochure-size-badge {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
  color: #5a738e;
  background: rgba(14, 34, 71, 0.05);
  padding: 4px 10px;
  border-radius: 6px;
}

.brochure-title {
  font-family: var(--font-heading);
  font-size: clamp(20px, 3vw, 26px);
  font-weight: 800;
  color: #0e2247;
  margin: 0 0 10px;
  line-height: 1.25;
}

.brochure-desc {
  font-family: var(--font-body);
  font-size: 14.5px;
  line-height: 1.6;
  color: #506577;
  margin: 0;
  max-width: 580px;
}

.brochure-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 220px;
}

.brochure-btn-download {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(135deg, #0077b6 0%, #00b4d8 100%);
  color: #ffffff !important;
  font-family: var(--font-heading);
  font-size: 14.5px;
  font-weight: 700;
  padding: 14px 24px;
  border-radius: 12px;
  text-decoration: none;
  box-shadow: 0 8px 24px rgba(0, 119, 182, 0.3);
  transition: all 0.25s ease;
  cursor: pointer;
  border: none;
}

.brochure-btn-download:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0, 119, 182, 0.42);
  filter: brightness(1.06);
}

.brochure-btn-preview {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(0, 180, 216, 0.08);
  color: #0077b6 !important;
  font-family: var(--font-heading);
  font-size: 13.5px;
  font-weight: 700;
  padding: 12px 20px;
  border-radius: 12px;
  text-decoration: none;
  border: 1.5px solid rgba(0, 180, 216, 0.35);
  transition: all 0.25s ease;
}

.brochure-btn-preview:hover {
  background: rgba(0, 180, 216, 0.16);
  border-color: #00b4d8;
  transform: translateY(-1px);
}

/* Feature grid in brochure page */
.brochure-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.brochure-feat-box {
  background: #ffffff;
  border-radius: 14px;
  padding: 18px 20px;
  border: 1px solid rgba(22, 139, 183, 0.14);
  box-shadow: 0 4px 16px rgba(14, 34, 71, 0.04);
  display: flex;
  align-items: center;
  gap: 14px;
}

.brochure-feat-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(0, 180, 216, 0.12);
  color: #0077b6;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.brochure-feat-text h4 {
  font-family: var(--font-heading);
  font-size: 14px;
  font-weight: 700;
  color: #0e2247;
  margin: 0 0 3px;
}

.brochure-feat-text p {
  font-family: var(--font-body);
  font-size: 12.5px;
  color: #64748b;
  margin: 0;
}

/* Embedded interactive viewer */
.brochure-viewer-card {
  background: #ffffff;
  border-radius: 20px;
  border: 1.5px solid rgba(22, 139, 183, 0.16);
  box-shadow: 0 16px 40px rgba(14, 34, 71, 0.08);
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.brochure-viewer-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 12px;
  border-bottom: 1px dashed rgba(14, 34, 71, 0.14);
  flex-wrap: wrap;
  gap: 10px;
}

.brochure-viewer-head span {
  font-family: var(--font-heading);
  font-size: 14.5px;
  font-weight: 700;
  color: #0e2247;
  display: flex;
  align-items: center;
  gap: 8px;
}

.brochure-frame-container {
  width: 100%;
  height: 680px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(14, 34, 71, 0.12);
  background: #f8fafc;
}

.brochure-iframe {
  width: 100%;
  height: 100%;
  border: none;
}

/* Dark mode overrides */
[data-theme="dark"] .brochure-hero-card,
[data-theme="dark"] .brochure-feat-box,
[data-theme="dark"] .brochure-viewer-card {
  background: var(--hx-surface) !important;
  border-color: var(--hx-line) !important;
  box-shadow: 0 14px 38px rgba(0, 0, 0, 0.45) !important;
}

[data-theme="dark"] .brochure-title,
[data-theme="dark"] .brochure-feat-text h4,
[data-theme="dark"] .brochure-viewer-head span {
  color: var(--hx-text) !important;
}

[data-theme="dark"] .brochure-desc,
[data-theme="dark"] .brochure-feat-text p {
  color: var(--hx-dim) !important;
}

[data-theme="dark"] .brochure-size-badge {
  background: rgba(255, 255, 255, 0.08);
  color: var(--hx-cyan);
}

[data-theme="dark"] .brochure-btn-preview {
  background: rgba(0, 229, 255, 0.1);
  color: var(--hx-cyan) !important;
  border-color: rgba(0, 229, 255, 0.35);
}

[data-theme="dark"] .brochure-feat-icon {
  background: rgba(0, 229, 255, 0.12);
  color: var(--hx-cyan);
}

[data-theme="dark"] .brochure-viewer-head {
  border-bottom-color: var(--hx-line);
}

[data-theme="dark"] .brochure-frame-container {
  border-color: var(--hx-line);
  background: #0d1527;
}

@media (max-width: 768px) {
  .brochure-hero-card {
    grid-template-columns: 1fr;
  }
  .brochure-actions {
    width: 100%;
  }
  .brochure-frame-container {
    height: 480px;
  }
}
"""

if '.brochure-showcase' not in css:
    with open(r'd:\sutram_new_final_group\Sutram_2026\css\style.css', 'a', encoding='utf-8') as f:
        f.write(brochure_css)
    print("Appended brochure styles to style.css!")
else:
    print("Brochure styles already present.")
