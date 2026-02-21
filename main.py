from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from arbitrage import find_arbitrage

app = FastAPI()

# Sample odds (in memory)
events = [
    {
        "id": 1,
        "sport": "NBA",
        "event": "Lakers vs Celtics",
        "market": "Moneyline",
        "outcomes": [
            {"book": "DraftKings", "team": "Lakers", "odds": 2.10},
            {"book": "FanDuel", "team": "Celtics", "odds": 2.05},
            {"book": "BetMGM", "team": "Lakers", "odds": 2.00},
            {"book": "Caesars", "team": "Celtics", "odds": 2.15}
        ]
    },
    {
        "id": 2,
        "sport": "NFL",
        "event": "Chiefs vs Bills",
        "market": "Moneyline",
        "outcomes": [
            {"book": "DraftKings", "team": "Chiefs", "odds": 1.95},
            {"book": "FanDuel", "team": "Bills", "odds": 1.92},
            {"book": "BetMGM", "team": "Chiefs", "odds": 1.90},
            {"book": "Caesars", "team": "Bills", "odds": 2.00}
        ]
    }
]

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/events")
def get_events():
    """Return all sample events."""
    return events


@app.get("/arbitrage")
def get_arbitrage():
    """Return arbitrage opportunities for all events."""
    return find_arbitrage(events)


@app.post("/calculate")
def calculate_stakes(data: dict):
    """Calculate optimal stake split for two odds."""
    bankroll = float(data["bankroll"])
    odds1 = float(data["odds1"])
    odds2 = float(data["odds2"])

    inv1 = 1 / odds1
    inv2 = 1 / odds2
    total_inv = inv1 + inv2
    stake1 = bankroll * (inv1 / total_inv)
    stake2 = bankroll - stake1
    profit = (stake1 * odds1) - bankroll

    return {
        "stake1": round(stake1, 2),
        "stake2": round(stake2, 2),
        "profit": round(profit, 2)
    }
