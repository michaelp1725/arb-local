def find_arbitrage(events):
    """
    Find 2-way arbitrage opportunities.
    Returns list of events with profit % and best odds per team.
    """
    results = []
    for event in events:
        outcomes = event["outcomes"]
        teams = list(set(o["team"] for o in outcomes))
        if len(teams) != 2:
            continue

        t1, t2 = teams
        best1 = max((o for o in outcomes if o["team"] == t1), key=lambda x: x["odds"])
        best2 = max((o for o in outcomes if o["team"] == t2), key=lambda x: x["odds"])

        o1, o2 = best1["odds"], best2["odds"]
        implied = (1 / o1) + (1 / o2)

        if implied < 1:
            profit_percent = ((1 / implied) - 1) * 100
            results.append({
                "event_id": event["id"],
                "profit_percent": round(profit_percent, 2),
                "best_odds": {
                    "team1": {"book": best1["book"], "odds": o1, "team": t1},
                    "team2": {"book": best2["book"], "odds": o2, "team": t2}
                }
            })
    return results
