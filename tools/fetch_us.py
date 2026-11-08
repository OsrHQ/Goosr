"""Fetch daily closes and dividends for the US paper test (SPY, SPUS) from Yahoo and write data/us.json.
Runs in GitHub Actions after the US close; uses only the Python standard library."""
import json, time, urllib.request, os, sys

TICKERS = ["SPY", "SPUS"]
START = 1780272000  # 2026-06-01 00:00 UTC: a little history before the test starts on 2026-12-01
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "us.json")

def get(ticker):
    last = None
    for host in ("query1", "query2"):
        for attempt in range(4):
            url = (f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}"
                   f"?period1={START}&period2={int(time.time()) + 86400}&interval=1d&events=div%2Csplit")
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (paper-test price fetch)"})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    res = json.load(r)["chart"]["result"][0]
                q = res["indicators"]["quote"][0]
                rows = [[t, c] for t, c in zip(res["timestamp"], q["close"]) if c is not None]
                divs = {str(int(d["date"])): d["amount"] for d in (res.get("events", {}).get("dividends", {}) or {}).values()}
                if len(rows) < 20:
                    raise ValueError("too few rows")
                return {"close": rows, "div": divs, "tz": res["meta"].get("exchangeTimezoneName")}
            except Exception as e:  # rate limits and hiccups: wait and retry
                last = e
                time.sleep(20 * (attempt + 1))
    raise SystemExit(f"{ticker}: {last}")

data = {"updated": int(time.time()), "source": "Yahoo Finance daily chart (close, dividends)", "tickers": {}}
for t in TICKERS:
    data["tickers"][t] = get(t)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(data, f, separators=(",", ":"))
print("wrote", OUT, {t: len(v["close"]) for t, v in data["tickers"].items()})
