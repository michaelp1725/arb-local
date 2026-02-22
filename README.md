# arb-local

A minimal arbitrage finder for sports betting. Compares odds across bookmakers, highlights arbitrage opportunities, and calculates optimal stake splits.

## Features

- **Live odds** from [The Odds API](https://the-odds-api.com/)
- **2-way arbitrage detection** — rows with ⭐ are guaranteed-profit opportunities
- **Stake calculator** — optimal bet split and guaranteed profit
- **12-hour cache** to stay within free API limits (500 calls/month)

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/michaelp1725/arb-local.git
   cd arb-local
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or: `pip3 install -r requirements.txt`

3. **Get an API key** (optional but recommended)
   - Sign up at [the-odds-api.com](https://the-odds-api.com/)
   - Copy `.env.example` to `.env` and add your key:
   ```bash
   ODDS_API_KEY=your_api_key_here
   ```
   Without a key, the app uses sample data.

## Run

```bash
python3 -m uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/static/index.html** in your browser.

If port 8000 is in use:
```bash
python3 -m uvicorn main:app --reload --port 8001
```
Then open **http://127.0.0.1:8001/static/index.html**

## Project structure

```
arb-local/
├── main.py           # FastAPI app, API endpoints
├── arbitrage.py      # Arbitrage detection logic
├── odds_api.py       # The Odds API integration
├── requirements.txt
└── static/
    └── index.html    # Frontend
```

## Tech stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn
- **Frontend:** Vanilla HTML/JS, Fetch API
- **Odds:** [The Odds API](https://the-odds-api.com/)
