"""
Fetch odds from The Odds API and transform to app format.
https://the-odds-api.com/
"""
import os
import time
import requests

API_BASE = "https://api.the-odds-api.com/v4"
CACHE_TTL_SEC = 7200  # 12 hours (2 fetches per day = ~60/month, under 500 limit)
_cache = {"events": None, "fetched_at": 0}


def _transform_event(api_event: dict, sport_title: str) -> dict:
    """Convert API event format to our format."""
    outcomes = []
    for bookmaker in api_event.get("bookmakers", []):
        for market in bookmaker.get("markets", []):
            if market["key"] != "h2h":
                continue
            for outcome in market.get("outcomes", []):
                outcomes.append({
                    "book": bookmaker["title"],
                    "team": outcome["name"],
                    "odds": outcome["price"]
                })
    return {
        "id": api_event["id"],
        "sport": sport_title,
        "event": f"{api_event.get('away_team', '')} @ {api_event.get('home_team', '')}",
        "market": "Moneyline",
        "outcomes": outcomes
    }


def fetch_odds(api_key: str, sport: str = "upcoming", regions: str = "us") -> list[dict]:
    """
    Fetch odds from The Odds API.
    Returns list of events in our format, or empty list on error.
    """
    global _cache
    if _cache["events"] is not None and (time.time() - _cache["fetched_at"]) < CACHE_TTL_SEC:
        return _cache["events"]

    url = f"{API_BASE}/sports/{sport}/odds"
    params = {
        "apiKey": api_key,
        "regions": regions,
        "markets": "h2h",
        "oddsFormat": "decimal"
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        return []
    except Exception:
        return []

    # Sport title mapping (sport_key -> display name)
    sport_map = {
        "americanfootball_nfl": "NFL",
        "basketball_nba": "NBA",
        "baseball_mlb": "MLB",
        "icehockey_nhl": "NHL",
        "soccer_epl": "EPL",
        "soccer_uefa_european_championship": "UEFA Euro",
        "tennis_atp_french_open": "ATP French Open",
    }

    events = []
    for ev in data:
        sk = ev.get("sport_key", "")
        sport_title = sport_map.get(sk, sk.replace("_", " ").title())
        if len(ev.get("bookmakers", [])) >= 2:
            events.append(_transform_event(ev, sport_title))

    _cache["events"] = events
    _cache["fetched_at"] = time.time()
    return events


def clear_cache():
    """Clear cached events (e.g. after manual refresh)."""
    global _cache
    _cache = {"events": None, "fetched_at": 0}
