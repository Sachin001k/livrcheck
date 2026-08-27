"""
Visual polish for LivrCheck: a small CSS injection plus HTML/CSS components
(hero banner, FIB-4 gauge, how-it-works steps, why-it-matters card, diet
section, FAQ cards). Kept separate from app.py so the calculation/auth logic
stays easy to read.

The CSS below targets Streamlit's `data-testid` attributes, which have been
stable across recent Streamlit versions (this app requires streamlit>=1.36).
If a future Streamlit release renames these, the app still works — it just
loses the extra polish, since none of this affects functionality.
"""

import re

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --lc-primary: #0f9b8e;
    --lc-primary-light: #38d9c9;
    --lc-blue: #3b82f6;
    --lc-purple: #7c3aed;
    --lc-purple-light: #a78bfa;
    --lc-green: #16a34a;
    --lc-amber: #f59e0b;
    --lc-indigo: #6366f1;
    --lc-rose: #e11d48;
    --lc-radius: 16px;
    --lc-bg-soft: #f2fbfa;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif;
}

@keyframes lc-gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes lc-fade-up {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes lc-pop-in {
    from { opacity: 0; transform: scale(0.92); }
    to { opacity: 1; transform: scale(1); }
}
@keyframes lc-slide-in {
    from { left: 0%; }
    to { left: var(--lc-target); }
}

/* Hero banner */
.lc-hero {
    background: linear-gradient(120deg, #0b756b 0%, #0f9b8e 45%, #38d9c9 100%);
    background-size: 200% 200%;
    animation: lc-gradient-shift 10s ease infinite;
    border-radius: var(--lc-radius);
    padding: 2.1rem 1.5rem;
    text-align: center;
    color: #ffffff;
    margin-bottom: 1.4rem;
    box-shadow: 0 12px 30px rgba(15, 155, 142, 0.28);
}
.lc-hero h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 2.1rem;
    margin: 0 0 0.35rem 0;
    animation: lc-fade-up 0.7s ease-out both;
}
.lc-hero p {
    font-size: 1.05rem;
    margin: 0;
    opacity: 0.95;
    animation: lc-fade-up 0.7s ease-out 0.12s both;
}

/* Gentle cascading entrance for page content */
[data-testid="stVerticalBlock"] > div > .element-container {
    animation: lc-fade-up 0.45s ease-out both;
}

/* Buttons */
button[kind="primary"],
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(120deg, var(--lc-primary), var(--lc-primary-light)) !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    box-shadow: 0 4px 14px rgba(15, 155, 142, 0.35) !important;
}
button[kind="primary"]:hover,
div[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(15, 155, 142, 0.45) !important;
}
button[kind="primary"]:active,
div[data-testid="stFormSubmitButton"] button:active {
    transform: translateY(0) scale(0.98);
}

div[data-testid="stDownloadButton"] button,
div[data-testid="stLinkButton"] a {
    border-radius: 999px !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
div[data-testid="stDownloadButton"] button:hover,
div[data-testid="stLinkButton"] a:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.14);
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: #ffffff;
    border-radius: var(--lc-radius);
    padding: 0.9rem 1.1rem;
    border: 1px solid rgba(15, 155, 142, 0.14);
    box-shadow: 0 4px 16px rgba(15, 155, 142, 0.10);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    animation: lc-pop-in 0.5s ease-out both;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(15, 155, 142, 0.18);
}

/* Alerts (info / success / warning / error) */
div[data-testid="stAlert"] {
    border-radius: var(--lc-radius) !important;
    animation: lc-fade-up 0.5s ease-out both;
}

/* Expanders */
div[data-testid="stExpander"] {
    border-radius: var(--lc-radius) !important;
    overflow: hidden;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f2fbfa 0%, #f5f3ff 100%);
}
.lc-sidebar-accent {
    height: 6px;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--lc-primary), var(--lc-blue), var(--lc-purple), var(--lc-amber));
    margin-bottom: 1.1rem;
    animation: lc-fade-up 0.5s ease-out both;
}
.lc-sidebar-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.15rem 0;
}
.lc-sidebar-badge.teal { background: #ccfbf1; color: #0f766e; }
.lc-sidebar-badge.purple { background: #ede9fe; color: #6d28d9; }
.lc-sidebar-badge.rose { background: #ffe4e6; color: #be123c; }

/* How it works */
.lc-steps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.9rem;
    margin: 0.8rem 0 1.5rem 0;
}
.lc-step-card {
    background: linear-gradient(160deg, #eff6ff, #ffffff);
    border: 1px solid rgba(59, 130, 246, 0.18);
    border-radius: var(--lc-radius);
    padding: 1rem;
    text-align: center;
    box-shadow: 0 4px 14px rgba(59, 130, 246, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    animation: lc-fade-up 0.5s ease-out both;
}
.lc-step-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(59, 130, 246, 0.18);
}
.lc-step-badge {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--lc-blue), #60a5fa);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin: 0 auto 0.5rem auto;
    box-shadow: 0 4px 10px rgba(59, 130, 246, 0.35);
}
.lc-step-title { font-weight: 600; margin-bottom: 0.3rem; color: #1e3a5f; }
.lc-step-body { font-size: 0.85rem; color: #475569; }

/* Why it matters */
.lc-why-card {
    background: linear-gradient(120deg, var(--lc-purple) 0%, var(--lc-purple-light) 100%);
    color: white;
    border-radius: var(--lc-radius);
    padding: 1.3rem 1.5rem;
    margin: 0.8rem 0 1.5rem 0;
    box-shadow: 0 10px 26px rgba(124, 58, 237, 0.28);
    animation: lc-fade-up 0.5s ease-out both;
}
.lc-why-card h4 { margin: 0 0 0.4rem 0; font-family: 'Poppins', sans-serif; }
.lc-why-card p { margin: 0; opacity: 0.97; line-height: 1.55; }

/* Diet & nutrition */
.lc-diet-wrap { margin: 0.9rem 0 0.3rem 0; }
.lc-diet-framing {
    border-radius: 999px;
    padding: 0.45rem 1rem;
    display: inline-block;
    font-weight: 600;
    margin-bottom: 0.9rem;
    animation: lc-pop-in 0.4s ease-out both;
}
.lc-diet-framing.low { background: #dcfce7; color: #166534; }
.lc-diet-framing.intermediate { background: #fef9c3; color: #854d0e; }
.lc-diet-framing.high { background: #fee2e2; color: #991b1b; }
.lc-diet-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 0.6rem 0;
}
@media (max-width: 640px) {
    .lc-diet-grid { grid-template-columns: 1fr; }
}
.lc-diet-card {
    border-radius: var(--lc-radius);
    padding: 1rem 1.1rem;
    animation: lc-fade-up 0.5s ease-out both;
}
.lc-diet-favor { background: linear-gradient(160deg, #f0fdf4, #ffffff); border: 1px solid rgba(22, 163, 74, 0.2); }
.lc-diet-favor h5 { color: #166534; margin: 0 0 0.5rem 0; }
.lc-diet-limit { background: linear-gradient(160deg, #fef2f2, #ffffff); border: 1px solid rgba(225, 29, 72, 0.2); }
.lc-diet-limit h5 { color: #9f1239; margin: 0 0 0.5rem 0; }
.lc-diet-card ul { margin: 0; padding-left: 1.1rem; font-size: 0.87rem; color: #374151; line-height: 1.65; }
.lc-diet-note {
    background: #eff6ff;
    border-left: 4px solid var(--lc-blue);
    border-radius: 8px;
    padding: 0.7rem 0.9rem;
    font-size: 0.87rem;
    margin: 0.6rem 0;
    color: #1e3a5f;
}
.lc-diet-disclaimer {
    background: #fffbeb;
    border-left: 4px solid var(--lc-amber);
    border-radius: 8px;
    padding: 0.8rem 1rem;
    margin-top: 0.7rem;
    font-size: 0.85rem;
    color: #78350f;
}
.lc-diet-sources { font-size: 0.72rem; color: #9ca3af; margin-top: 0.5rem; }

/* FAQ */
.lc-faq-item {
    background: linear-gradient(160deg, #eef2ff, #ffffff);
    border-left: 4px solid var(--lc-indigo);
    border-radius: 0 var(--lc-radius) var(--lc-radius) 0;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.7rem;
    animation: lc-fade-up 0.5s ease-out both;
    transition: transform 0.15s ease;
}
.lc-faq-item:hover { transform: translateX(3px); }
.lc-faq-q { font-weight: 600; color: #3730a3; margin-bottom: 0.3rem; }
.lc-faq-a { font-size: 0.87rem; color: #4b5563; margin: 0; }

/* FIB-4 gauge */
.lc-gauge-wrap { margin: 1.1rem 0 0.3rem 0; }
.lc-gauge-track {
    position: relative;
    height: 14px;
    border-radius: 999px;
    display: flex;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.10);
    overflow: visible;
}
.lc-gauge-zone { height: 100%; }
.lc-zone-low { background: #86efac; border-radius: 999px 0 0 999px; }
.lc-zone-mid { background: #fde047; }
.lc-zone-high { background: #fca5a5; border-radius: 0 999px 999px 0; }
.lc-gauge-marker {
    position: absolute;
    top: -5px;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 3px solid white;
    transform: translateX(-50%);
    animation: lc-slide-in 1.1s cubic-bezier(0.22, 1, 0.36, 1) both;
}
.lc-gauge-scale {
    display: flex;
    justify-content: space-between;
    font-size: 0.75rem;
    color: #6b7280;
    margin-top: 4px;
}
</style>
"""


def render_hero(title: str, subtitle: str) -> str:
    """Return the animated gradient hero banner HTML for the page header."""
    return f"""
    <div class="lc-hero">
        <h1>🩺 {title}</h1>
        <p>{subtitle}</p>
    </div>
    """


_TIER_COLORS = {"low": "#16a34a", "intermediate": "#eab308", "high": "#dc2626"}


def render_gauge(score: float, tier: str, low_cutoff: float, high_cutoff: float, max_scale: float = 6.0) -> str:
    """Return an animated horizontal gauge showing where the score falls
    relative to the low/high risk cut-offs."""
    clamped = max(0.0, min(score, max_scale))
    pos_pct = round((clamped / max_scale) * 100, 1)
    low_pct = round((low_cutoff / max_scale) * 100, 1)
    high_pct = round((high_cutoff / max_scale) * 100, 1)
    marker_color = _TIER_COLORS.get(tier, "#0f9b8e")

    return f"""
    <div class="lc-gauge-wrap">
        <div class="lc-gauge-track">
            <div class="lc-gauge-zone lc-zone-low" style="width:{low_pct}%;"></div>
            <div class="lc-gauge-zone lc-zone-mid" style="width:{high_pct - low_pct}%;"></div>
            <div class="lc-gauge-zone lc-zone-high" style="width:{100 - high_pct}%;"></div>
            <div class="lc-gauge-marker"
                 style="--lc-target:{pos_pct}%; left:{pos_pct}%; background:{marker_color}; box-shadow: 0 0 0 4px {marker_color}33;">
            </div>
        </div>
        <div class="lc-gauge-scale">
            <span>0</span><span>{low_cutoff:g}</span><span>{high_cutoff:g}</span><span>{max_scale:g}+</span>
        </div>
    </div>
    """


def _bold_md_to_html(text: str) -> str:
    """Convert simple **bold** markdown to <strong> for text embedded
    inside a larger raw-HTML block, where Streamlit's markdown parser
    may not reliably process it."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)


def _bullet_md_to_html(md_list: str) -> str:
    """Convert a "- item\\n- item" markdown bullet list into an <ul>."""
    items = "".join(f"<li>{line[2:].strip()}</li>" for line in md_list.splitlines() if line.strip().startswith("- "))
    return f"<ul>{items}</ul>"


SIDEBAR_ACCENT = '<div class="lc-sidebar-accent"></div>'


def render_sidebar_badge(icon: str, text: str, color: str = "teal") -> str:
    return f'<span class="lc-sidebar-badge {color}">{icon} {text}</span>'


def render_how_it_works(steps: list) -> str:
    """steps: list of (title, body) tuples, numbered automatically."""
    cards = "".join(
        f'<div class="lc-step-card">'
        f'<div class="lc-step-badge">{i}</div>'
        f'<div class="lc-step-title">{title}</div>'
        f'<div class="lc-step-body">{body}</div>'
        f"</div>"
        for i, (title, body) in enumerate(steps, start=1)
    )
    return f'<div class="lc-steps-grid">{cards}</div>'


def render_why_matters(heading: str, body: str) -> str:
    return f"""
    <div class="lc-why-card">
        <h4>💜 {heading}</h4>
        <p>{body}</p>
    </div>
    """


def render_diet_section(
    *,
    framing_text: str,
    tier: str,
    favor_heading: str,
    favor_list_md: str,
    limit_heading: str,
    limit_list_md: str,
    plate_method: str,
    disclaimer_heading: str,
    disclaimer_body: str,
    sources_text: str,
    weight_note: str = "",
    diabetes_note: str = "",
) -> str:
    notes_html = ""
    if weight_note:
        notes_html += f'<div class="lc-diet-note">⚖️ {weight_note}</div>'
    if diabetes_note:
        notes_html += f'<div class="lc-diet-note">🩸 {diabetes_note}</div>'

    return f"""
    <div class="lc-diet-wrap">
        <span class="lc-diet-framing {tier}">{framing_text}</span>
        <div class="lc-diet-grid">
            <div class="lc-diet-card lc-diet-favor">
                <h5>✅ {favor_heading}</h5>
                {_bullet_md_to_html(favor_list_md)}
            </div>
            <div class="lc-diet-card lc-diet-limit">
                <h5>🚫 {limit_heading}</h5>
                {_bullet_md_to_html(limit_list_md)}
            </div>
        </div>
        <div class="lc-diet-note">🍽️ {_bold_md_to_html(plate_method)}</div>
        {notes_html}
        <div class="lc-diet-disclaimer"><strong>{disclaimer_heading}</strong><br>{disclaimer_body}</div>
        <div class="lc-diet-sources">{sources_text}</div>
    </div>
    """


def render_faq(items: list) -> str:
    """items: list of (question, answer) tuples."""
    return "".join(
        f'<div class="lc-faq-item"><div class="lc-faq-q">❓ {q}</div><p class="lc-faq-a">{a}</p></div>'
        for q, a in items
    )
