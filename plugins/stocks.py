PLUGIN_NAME = "stocks"
PLUGIN_DESCRIPTION = "Get real stock data including current price, historical data, and analysis for any ticker symbol"
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "stocks",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock ticker symbol e.g. AAPL, TSLA, MSFT"
                },
                "period": {
                    "type": "string",
                    "description": "Time period: 1d, 5d, 1mo, 2mo, 3mo, 6mo, 1y, 2y, 5y",
                    "default": "1mo"
                },
                "info": {
                    "type": "string",
                    "description": "What to return: 'price' (current), 'history' (OHLCV data), 'summary' (full analysis)",
                    "default": "summary"
                }
            },
            "required": ["symbol"]
        }
    }
}


def run(symbol: str, period: str = "1mo", info: str = "summary") -> str:
    import yfinance as yf

    ticker = yf.Ticker(symbol)

    if info == "price":
        data = ticker.fast_info
        return f"{symbol}: ${data.last_price:.2f} USD (last close)"

    elif info == "history":
        hist = ticker.history(period=period)
        if hist.empty:
            return f"No data found for {symbol}"
        lines = [f"{symbol} historical data ({period}):"]
        lines.append(f"{'Date':<12} {'Open':>8} {'High':>8} {'Low':>8} {'Close':>8} {'Volume':>12}")
        lines.append("-" * 60)
        for date, row in hist.iterrows():
            lines.append(
                f"{str(date.date()):<12} "
                f"{row['Open']:>8.2f} "
                f"{row['High']:>8.2f} "
                f"{row['Low']:>8.2f} "
                f"{row['Close']:>8.2f} "
                f"{int(row['Volume']):>12,}"
            )
        return "\n".join(lines)

    else:  # summary
        hist = ticker.history(period=period)
        if hist.empty:
            return f"No data found for {symbol}"

        info_data = ticker.fast_info

        start_price = hist["Close"].iloc[0]
        end_price = hist["Close"].iloc[-1]
        change = end_price - start_price
        change_pct = (change / start_price) * 100
        high = hist["High"].max()
        low = hist["Low"].min()
        avg_volume = hist["Volume"].mean()
        volatility = hist["Close"].pct_change().std() * 100

        # Moving averages
        ma7 = hist["Close"].tail(7).mean() if len(hist) >= 7 else None
        ma30 = hist["Close"].tail(30).mean() if len(hist) >= 30 else None

        lines = [
            f"=== {symbol} Stock Analysis ({period}) ===",
            f"",
            f"PRICE",
            f"  Start:      ${start_price:.2f}",
            f"  End:        ${end_price:.2f}",
            f"  Change:     ${change:+.2f} ({change_pct:+.2f}%)",
            f"  Period High: ${high:.2f}",
            f"  Period Low:  ${low:.2f}",
            f"",
            f"AVERAGES",
        ]

        if ma7:
            lines.append(f"  MA7:   ${ma7:.2f}")
        if ma30:
            lines.append(f"  MA30:  ${ma30:.2f}")

        lines += [
            f"",
            f"VOLATILITY",
            f"  Daily volatility: {volatility:.2f}%",
            f"  Avg volume: {avg_volume:,.0f}",
            f"",
            f"DATA POINTS: {len(hist)} trading days",
        ]

        return "\n".join(lines)
