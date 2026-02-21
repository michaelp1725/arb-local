from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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
