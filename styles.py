"""
Visual polish for LivrCheck: a small CSS injection plus a couple of
HTML/CSS components (hero banner, FIB-4 gauge). Kept separate from app.py
so the calculation/auth logic stays easy to read.

The CSS below targets Streamlit's `data-testid` attributes, which have been
stable across recent Streamlit versions (this app requires streamlit>=1.36).
If a future Streamlit release renames these, the app still works — it just
loses the extra polish, since none of this affects functionality.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --lc-primary: #0f9b8e;
    --lc-primary-light: #38d9c9;
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
    background: var(--lc-bg-soft);
}

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
