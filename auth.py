"""
Supabase-backed login/signup and per-user FIB-4 result history for LivrCheck.

Setup required before this works (see README.md "Login & history storage"):
    1. Create a free project at https://supabase.com.
    2. Run supabase_schema.sql (in this folder) in the Supabase SQL editor.
    3. Add SUPABASE_URL and SUPABASE_KEY to .streamlit/secrets.toml locally,
       and to the app's "Secrets" section on Streamlit Community Cloud.

The Supabase client is stored in st.session_state (per browser session), not
in a process-wide cache — a single Streamlit app process serves many
concurrent users, and caching an authenticated client globally would leak
one user's session to another.
"""

import streamlit as st
from supabase import create_client, Client


def get_client() -> Client:
    if "supabase_client" not in st.session_state:
        st.session_state.supabase_client = create_client(
            st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"]
        )
    return st.session_state.supabase_client


def sign_up(email: str, password: str):
    return get_client().auth.sign_up({"email": email, "password": password})


def sign_in(email: str, password: str):
    client = get_client()
    response = client.auth.sign_in_with_password({"email": email, "password": password})
    st.session_state.auth_user = response.user
    return response


def sign_out():
    client = get_client()
    try:
        client.auth.sign_out()
    except Exception:
        pass
    st.session_state.pop("auth_user", None)
    st.session_state.pop("supabase_client", None)


def current_user():
    return st.session_state.get("auth_user")


def save_result(user_id: str, *, age, ast, alt, platelets, score, tier) -> None:
    get_client().table("fib4_results").insert(
        {
            "user_id": user_id,
            "age": age,
            "ast": ast,
            "alt": alt,
            "platelets": platelets,
            "score": score,
            "tier": tier,
        }
    ).execute()


def get_history(user_id: str) -> list:
    response = (
        get_client()
        .table("fib4_results")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return response.data
