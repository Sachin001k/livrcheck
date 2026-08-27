"""
LivrCheck — a free, bilingual FIB-4 liver fibrosis risk screening tool.

Run locally:
    streamlit run app.py

Deploy for free on Streamlit Community Cloud (see README.md for steps).
"""

import urllib.parse
from datetime import datetime

import streamlit as st

import auth
from fib4 import calculate_fib4, calculate_bmi, bmi_category, InvalidInputError, LOW_RISK_CUTOFF, HIGH_RISK_CUTOFF
from styles import CUSTOM_CSS, render_hero, render_gauge
from translations import t


# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="LivrCheck",
    page_icon="🩺",
    layout="centered",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "lang" not in st.session_state:
    st.session_state.lang = "en"


def _(key: str) -> str:
    """Shorthand translation lookup using the current session language."""
    return t(st.session_state.lang, key)


LANGUAGE_OPTIONS = {
    "en": "English",
    "hi": "हिन्दी",
    "mr": "मराठी",
    "bn": "বাংলা",
    "te": "తెలుగు",
    "ta": "தமிழ்",
    "gu": "ગુજરાતી",
    "ur": "اردو",
    "kn": "ಕನ್ನಡ",
    "or": "ଓଡ଼ିଆ",
    "ml": "മലയാളം",
    "pa": "ਪੰਜਾਬੀ",
}


# ---------------------------------------------------------------------------
# Sidebar — language toggle
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("### 🌐 Language")
    lang_choice = st.selectbox(
        label="Language",
        options=list(LANGUAGE_OPTIONS.keys()),
        format_func=lambda code: LANGUAGE_OPTIONS[code],
        index=list(LANGUAGE_OPTIONS.keys()).index(st.session_state.lang),
        label_visibility="collapsed",
    )
    st.session_state.lang = lang_choice

    st.markdown("---")
    st.caption(_("sidebar_tagline"))

    st.markdown("---")
    user = auth.current_user()
    if user:
        st.caption(f"{_('logged_in_as')} {user.email}")
        if st.button(_("logout_button"), use_container_width=True):
            auth.sign_out()
            st.rerun()
    else:
        with st.expander(f"🔐 {_('login_tab')} / {_('signup_tab')}"):
            tab_login, tab_signup = st.tabs([_("login_tab"), _("signup_tab")])

            with tab_login:
                with st.form("login_form"):
                    login_email = st.text_input(_("email_label"), key="login_email")
                    login_password = st.text_input(_("password_label"), type="password", key="login_password")
                    login_submitted = st.form_submit_button(
                        _("login_button"), type="primary", use_container_width=True
                    )
                if login_submitted:
                    if not login_email or not login_password:
                        st.error(_("auth_validation_error"))
                    else:
                        try:
                            auth.sign_in(login_email, login_password)
                        except Exception:
                            st.error(_("login_error"))
                        else:
                            st.rerun()

            with tab_signup:
                with st.form("signup_form"):
                    signup_email = st.text_input(_("email_label"), key="signup_email")
                    signup_password = st.text_input(
                        _("password_label"), type="password", help=_("password_help"), key="signup_password"
                    )
                    signup_submitted = st.form_submit_button(
                        _("signup_button"), type="primary", use_container_width=True
                    )
                if signup_submitted:
                    if not signup_email or not signup_password:
                        st.error(_("auth_validation_error"))
                    elif len(signup_password) < 6:
                        st.error(_("password_too_short"))
                    else:
                        try:
                            auth.sign_up(signup_email, signup_password)
                        except Exception as exc:
                            st.error(f"{_('signup_error')}: {exc}")
                        else:
                            st.success(_("signup_success"))


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.markdown(render_hero(_("app_title"), _("app_subtitle")), unsafe_allow_html=True)

st.markdown(f"#### {_('intro_heading')}")
st.markdown(_("intro_body"))

st.info(f"**{_('not_alcohol_heading')}**\n\n{_('not_alcohol_body')}")

st.markdown("---")


# ---------------------------------------------------------------------------
# History — past saved results for this user
# ---------------------------------------------------------------------------

current_user = auth.current_user()

if current_user:
    with st.expander(_("history_heading")):
        try:
            history = auth.get_history(current_user.id)
        except Exception:
            history = []

        if not history:
            st.caption(_("no_history_yet"))
        else:
            tier_labels = {"low": _("tier_low"), "intermediate": _("tier_intermediate"), "high": _("tier_high")}
            st.dataframe(
                [
                    {
                        _("result_card_generated"): row["created_at"][:10],
                        _("score_label"): row["score"],
                        _("results_heading"): tier_labels.get(row["tier"], row["tier"]),
                    }
                    for row in history
                ],
                use_container_width=True,
                hide_index=True,
            )

    st.markdown("---")


# ---------------------------------------------------------------------------
# Input form
# ---------------------------------------------------------------------------

st.markdown(f"### {_('form_heading')}")

with st.form("fib4_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(_("age_label"), min_value=1, max_value=120, value=None, step=1, placeholder="e.g. 45")
        ast = st.number_input(_("ast_label"), min_value=0.0, value=None, step=1.0, help=_("ast_help"), placeholder="e.g. 28")
    with col2:
        alt = st.number_input(_("alt_label"), min_value=0.0, value=None, step=1.0, help=_("alt_help"), placeholder="e.g. 32")
        platelets = st.number_input(
            _("platelets_label"), min_value=0.0, value=None, step=1.0, help=_("platelets_help"), placeholder="e.g. 250"
        )

    st.markdown(f"##### {_('context_heading')}")

    st.markdown(f"**{_('bmi_heading')}**")
    col3, col4 = st.columns(2)
    with col3:
        height = st.number_input(_("height_label"), min_value=0.0, value=None, step=1.0, placeholder="e.g. 170")
    with col4:
        weight = st.number_input(_("weight_label"), min_value=0.0, value=None, step=1.0, placeholder="e.g. 70")

    diabetes = st.radio(_("diabetes_label"), options=[_("yes"), _("no"), _("not_sure")], index=None, horizontal=True)
    family_history = st.radio(
        _("family_history_label"), options=[_("yes"), _("no"), _("not_sure")], index=None, horizontal=True
    )

    submitted = st.form_submit_button(_("calculate_button"), type="primary", use_container_width=True)


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

if submitted:
    if not age or not ast or not alt or not platelets:
        st.error(_("validation_error"))
    else:
        try:
            result = calculate_fib4(age=age, ast=ast, alt=alt, platelets=platelets)
        except InvalidInputError as exc:
            st.error(str(exc))
        else:
            if current_user:
                try:
                    auth.save_result(
                        current_user.id,
                        age=age,
                        ast=ast,
                        alt=alt,
                        platelets=platelets,
                        score=result.score,
                        tier=result.tier,
                    )
                except Exception:
                    st.warning(_("history_save_error"))

            st.markdown("---")
            st.markdown(f"## {_('results_heading')}")

            tier_display = {
                "low": (_("tier_low"), "success"),
                "intermediate": (_("tier_intermediate"), "warning"),
                "high": (_("tier_high"), "error"),
            }
            tier_label, tier_style = tier_display[result.tier]

            score_col, tier_col = st.columns(2)
            with score_col:
                st.metric(_("score_label"), f"{result.score}")
            with tier_col:
                st.metric(_("results_heading"), tier_label)

            st.markdown(
                render_gauge(result.score, result.tier, LOW_RISK_CUTOFF, HIGH_RISK_CUTOFF),
                unsafe_allow_html=True,
            )

            explanation_key = f"tier_{result.tier}_explanation"
            action_key = f"action_{result.tier}"

            if result.tier == "low":
                st.success(_(explanation_key))
            elif result.tier == "intermediate":
                st.warning(_(explanation_key))
            else:
                st.error(_(explanation_key))

            if result.age_out_of_validated_range:
                st.warning(_("age_warning"))

            st.markdown(f"#### {_('action_heading')}")
            st.markdown(_(action_key))

            # --- BMI context (optional) ---
            if height and weight:
                try:
                    bmi = calculate_bmi(height, weight)
                    category = bmi_category(bmi)
                    category_label = {
                        "underweight": _("bmi_underweight"),
                        "normal": _("bmi_normal"),
                        "overweight": _("bmi_overweight"),
                        "obese": _("bmi_obese"),
                    }[category]

                    st.markdown(f"#### {_('bmi_context_heading')}")
                    st.write(f"BMI: **{bmi}** ({category_label})")
                    if category in ("overweight", "obese"):
                        st.caption(_("bmi_note"))
                except InvalidInputError:
                    pass

            if diabetes == _("yes"):
                st.caption(_("diabetes_note"))

            if family_history == _("yes"):
                st.caption(_("family_history_note"))

            # --- Disclaimer (always shown, prominent) ---
            st.markdown("---")
            st.error(f"**{_('disclaimer_heading')}**\n\n{_('disclaimer_body')}")

            with st.expander(_("formula_heading")):
                st.markdown(_("formula_body"))
                st.latex(r"FIB\text{-}4 = \frac{Age \times AST}{Platelets \times \sqrt{ALT}}")

            # --- Downloadable result card ---
            st.markdown("---")
            st.markdown(f"### {_('print_button')}")

            generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
            card_html = f"""
            <html>
            <head><meta charset="utf-8"><title>{_('result_card_title')}</title></head>
            <body style="font-family: Arial, sans-serif; max-width: 500px; margin: auto; padding: 24px; border: 2px solid #333;">
                <h2 style="text-align:center;">🩺 {_('result_card_title')}</h2>
                <p style="text-align:center; color:#666;">{_('result_card_generated')}: {generated_at}</p>
                <hr>
                <p><strong>{_('score_label')}:</strong> {result.score}</p>
                <p><strong>{_('results_heading')}:</strong> {tier_label}</p>
                <p>{_(explanation_key)}</p>
                <h4>{_('action_heading')}</h4>
                <p>{_(action_key)}</p>
                <hr>
                <p style="font-size: 12px; color:#900;"><strong>{_('disclaimer_heading')}:</strong> {_('disclaimer_body')}</p>
            </body>
            </html>
            """
            st.download_button(
                label=_("print_button"),
                data=card_html,
                file_name="livrcheck_result.html",
                mime="text/html",
                use_container_width=True,
            )

            # --- WhatsApp share ---
            st.markdown(f"#### {_('share_heading')}")
            st.write(_("share_body"))
            app_url = "https://livrcheck.streamlit.app"  # update after deployment
            share_text = _("share_message_template").format(url=app_url)
            wa_link = "https://wa.me/?text=" + urllib.parse.quote(share_text)
            st.link_button(_("share_button_text"), wa_link, use_container_width=True)


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.markdown("---")
st.caption(_("footer_note"))
st.caption("Sources: Sterling RK, et al. Hepatology 2006;43:1317 · Shalimar et al. J Clin Exp Hepatol 2022 · echosens.com")
