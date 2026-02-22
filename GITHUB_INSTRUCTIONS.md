# arb-local — GitHub & PR Setup Instructions

## Project location

`arb-local/` is in your workspace. Run commands from:

```
cd "/Users/michaelparker/Desktop/Monte Carlo Risk & Decision Engine for Trading Project/arb-local"
```

---

## 1. Create a new GitHub repo

1. Go to https://github.com/new  
2. Name it `arb-local` (or another name)  
3. Do **not** add a README, .gitignore, or license (content already exists locally)  
4. Create the repository  

---

## 2. Connect local repo and push

```bash
cd "/Users/michaelparker/Desktop/Monte Carlo Risk & Decision Engine for Trading Project/arb-local"

# Add your repo (replace with your actual repo URL)
git remote add origin https://github.com/michaelp1725/arb-local.git

# Push main (all 10 commits)
git push -u origin main
```

---

## 3. Open 10 PRs (one per commit)

Merge them in order (PR1 → PR2 → … → PR10).

### Option A — Create branches from each commit

```bash
cd arb-local

# PR 1
git checkout -b pr-1 db50f30
git push -u origin pr-1
# Open PR: base=main, compare=pr-1
# Merge, delete pr-1

# PR 2 (after merging PR 1 into main)
git checkout main
git pull origin main
git checkout -b pr-2 c14d3e0
git push -u origin pr-2
# Open PR: base=main, compare=pr-2
# Merge, delete pr-2

# PR 3
git checkout main
git pull origin main
git checkout -b pr-3 97f56a5
git push -u origin pr-3
# ... repeat
```

### Option B — Simpler: one PR per branch (cumulative)

Create 10 branches, each with one additional commit on top of `main`:

```bash
cd arb-local

# PR 1: Push branch with only commit 1
git checkout -b pr-1 db50f30
git push -u origin pr-1
# On GitHub: PR pr-1 → main, merge

# PR 2: Push branch with commits 1–2
git checkout main
git pull
git checkout -b pr-2 c14d3e0
git push -u origin pr-2
# PR pr-2 → main, merge

# PR 3: pr-3 at 97f56a5
git checkout main && git pull
git checkout -b pr-3 97f56a5
git push -u origin pr-3

# PR 4: pr-4 at 986b9e1
git checkout main && git pull
git checkout -b pr-4 986b9e1
git push -u origin pr-4

# PR 5: pr-5 at 11a70ff
git checkout main && git pull
git checkout -b pr-5 11a70ff
git push -u origin pr-5

# PR 6: pr-6 at b21d2c3
git checkout main && git pull
git checkout -b pr-6 b21d2c3
git push -u origin pr-6

# PR 7: pr-7 at bae6669
git checkout main && git pull
git checkout -b pr-7 bae6669
git push -u origin pr-7

# PR 8: pr-8 at 082924e
git checkout main && git pull
git checkout -b pr-8 082924e
git push -u origin pr-8

# PR 9: pr-9 at d37e789
git checkout main && git pull
git checkout -b pr-9 d37e789
git push -u origin pr-9

# PR 10: pr-10 at afa4209 (full project)
git checkout main && git pull
git checkout -b pr-10 afa4209
git push -u origin pr-10
```

You must merge PR 1, then PR 2, and so on. Later PRs depend on earlier ones.

### Option C — Single PR with 10 commits

```bash
git push -u origin main
```

Then open one PR with all 10 commits. If `main` is empty on GitHub, push `main` and create a PR from your local `main` into the remote default branch.

---

## 4. Run the app locally

```bash
cd arb-local
pip install -r requirements.txt
uvicorn main:app --reload
```

Open: http://127.0.0.1:8000/static/index.html

---

## Commit reference

| PR   | Commit   | Description                          |
|------|----------|--------------------------------------|
| PR1  | db50f30  | requirements.txt and .gitignore      |
| PR2  | c14d3e0  | FastAPI skeleton and static serve    |
| PR3  | 97f56a5  | Sample events data                   |
| PR4  | 986b9e1  | GET /events                          |
| PR5  | 11a70ff  | arbitrage.py and find_arbitrage      |
| PR6  | b21d2c3  | GET /arbitrage                       |
| PR7  | bae6669  | POST /calculate                      |
| PR8  | 082924e  | Table structure and CSS              |
| PR9  | d37e789  | Fetch, render, arb highlight         |
| PR10 | afa4209  | Calculate Stakes button              |
