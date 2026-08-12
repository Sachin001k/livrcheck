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
├── app.py            # Streamlit UI — the main app
├── fib4.py           # Core FIB-4 + BMI calculation logic (no UI dependencies)
├── translations.py   # All English + Hindi text, in one place
├── test_fib4.py       # Unit tests for the calculation logic
├── requirements.txt  # Python dependencies
└── .gitignore
```

The calculation logic (`fib4.py`) is deliberately separated from the UI
(`app.py`) so it can be unit tested independently — see `test_fib4.py`.
All 13 tests currently pass.

## Running it locally (in VS Code)

1. Open this folder in VS Code.
2. Open a terminal (`` Ctrl+` `` / `` Cmd+` ``) and create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the tests to confirm everything works:
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
