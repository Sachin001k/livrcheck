# LivrCheck

A free, bilingual (English + Hindi) web tool that calculates a **FIB-4 liver
fibrosis risk score** from a standard blood test (LFT + CBC) and tells the
user what to do next.

Built with Python + [Streamlit](https://streamlit.io).

> ⚠️ **Not a diagnosis.** LivrCheck is a screening tool based on the
> clinically validated FIB-4 formula (Sterling et al., *Hepatology* 2006).
> It does not replace medical advice. See the in-app disclaimer.

## What's in this folder

```
livrcheck/
├── app.py                          # Streamlit UI — the main app
├── fib4.py                         # Core FIB-4 + BMI calculation logic (no UI dependencies)
├── auth.py                         # Supabase login/signup + saved result history
├── translations.py                 # All English + Hindi text, in one place
├── test_fib4.py                    # Unit tests for the calculation logic
├── supabase_schema.sql             # Run once in Supabase to create the results table
├── requirements.txt                # Python dependencies
├── .streamlit/secrets.toml.example # Template for your Supabase credentials
└── .gitignore
```

The calculation logic (`fib4.py`) is deliberately separated from the UI
(`app.py`) so it can be unit tested independently — see `test_fib4.py`.
All 13 tests currently pass.

## Login & history storage (Supabase)

LivrCheck requires users to log in, and saves each calculated FIB-4 result
under their account so they can review it later. This is backed by
[Supabase](https://supabase.com) (free tier) — it provides both the
email/password auth and the database table for saved results.

1. Create a free account/project at [supabase.com](https://supabase.com).
2. In the Supabase dashboard, open **SQL Editor -> New query**, paste in the
   contents of [`supabase_schema.sql`](supabase_schema.sql), and run it. This
   creates the `fib4_results` table with Row Level Security so each user can
   only ever see their own saved results.
3. In **Settings -> API**, copy the **Project URL** and the **anon public**
   key.
4. Locally: copy `.streamlit/secrets.toml.example` to
   `.streamlit/secrets.toml` and paste in those two values. This file is
   already git-ignored and must never be committed.
5. On Streamlit Community Cloud: open your app -> **Settings -> Secrets**,
   and paste in the same two lines.
6. By default, Supabase requires users to confirm their email address
   before they can log in after signing up — that's expected behavior, not
   a bug.

## Running it locally (in VS Code)

1. Open this folder in VS Code.
2. Open a terminal (`` Ctrl+` `` / `` Cmd+` ``) and create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Complete the Supabase setup above (the app won't start without valid
   `SUPABASE_URL` / `SUPABASE_KEY` in `.streamlit/secrets.toml`).
4. Run the tests to confirm everything works:
   ```bash
   pip install pytest
   python -m pytest test_fib4.py -v
   ```
4. Launch the app:
   ```bash
   streamlit run app.py
   ```
   It will open automatically at `http://localhost:8501`.

## Pushing to GitHub

From this folder, in VS Code's terminal:

```bash
git init
git add .
git commit -m "Initial LivrCheck app"
gh repo create livrcheck --public --source=. --push
```

(If you don't have the `gh` CLI, create an empty repo named `livrcheck` on
github.com first, then run:)

```bash
git remote add origin git@github.com:<your-username>/livrcheck.git
git branch -M main
git push -u origin main
```

## Deploying for free on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with
   your GitHub account.
2. Click **New app**, select the `livrcheck` repo, branch `main`, and set
   the main file path to `app.py`.
3. Click **Deploy**. You'll get a permanent URL like
   `https://livrcheck.streamlit.app` (or a variant if that name is taken).
4. Once you have your real URL, update the `app_url` variable near the
   bottom of `app.py` (search for `livrcheck.streamlit.app`) so the
   WhatsApp share button points to the live link, then commit and push
   again — Streamlit Cloud auto-redeploys on every push to `main`.

## Before sharing this publicly

- [ ] Have a native Hindi speaker review all strings in `translations.py`
      under the `"hi"` dictionary. They're marked with a
      `NEEDS_NATIVE_REVIEW` note at the top of the file. This was drafted
      by Claude and has **not** been reviewed by a native speaker yet.
- [ ] Update the WhatsApp share URL in `app.py` once deployed (see above).
- [ ] Double check the FIB-4 cut-offs and citations in `fib4.py` and
      `translations.py` against the sources in the project write-up if
      anything changes.
- [ ] Complete the Supabase setup above (login won't work without it).
- [ ] Write and link a privacy policy — the app now stores accounts and
      per-user health results (FIB-4 scores), which is personal health data
      and carries privacy obligations (e.g. India's DPDP Act 2023) beyond
      what a fully anonymous calculator would.

## Sources

- Sterling RK, et al. *Hepatology*. 2006;43:1317 — FIB-4 formula
- Shalimar et al. *J Clin Exp Hepatol*. 2022;12(3):818-829 — NAFLD
  prevalence in India
- University of Washington Hepatitis C Online — FIB-4 clinical calculator
  reference
- Full citation list: see the LivrCheck project document (Athena
  Education, June 2026)

## License

Open source — feel free to adapt. No warranty; this is a screening aid,
not a medical device.
