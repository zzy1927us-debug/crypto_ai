import os
from config import SYMBOLS, EXCHANGES, REPORT_PATH, DAYS_HISTORY
from data_fetch import fetch_history
from indicators import compute_indicators
from deepseek_api import analyze_with_deepseek, summarize_market
from report_generator import create_pdf_report

# Ensure the report directory exists
os.makedirs(REPORT_PATH, exist_ok=True)

results = []
# Loop through each exchange and symbol
for exch in EXCHANGES:
    for symbol in SYMBOLS:
        df = fetch_history(symbol, exch, days=DAYS_HISTORY)
        df = compute_indicators(df)
        advice = analyze_with_deepseek(symbol, exch, df)
        # Extract latest indicator values
        rsi = round(df["rsi"].iloc[-1], 2)
        macd = round(df["macd"].iloc[-1], 2)
        signal = round(df["signal"].iloc[-1], 2)
        ema = round(df["ema"].iloc[-1], 2) if "ema" in df.columns else None
        bb_high = round(df["bb_high"].iloc[-1], 2) if "bb_high" in df.columns else None
        bb_low = round(df["bb_low"].iloc[-1], 2) if "bb_low" in df.columns else None
        results.append([symbol, exch, rsi, macd, signal, ema, bb_high, bb_low, advice])

# Generate market summary
summary = summarize_market(results)
# Generate PDF report
report_path = create_pdf_report(results, summary, REPORT_PATH)
print(f"✅ 报告生成成功: {report_path}")
