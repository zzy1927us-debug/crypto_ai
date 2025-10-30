import os
import requests
from config import DEEPC_API_KEY

DEEPC_BASE = "https://api.deepseek.com/v1"


def analyze_with_deepseek(symbol, exch, df):
    """
    Use DeepSeek API to provide trading advice based on RSI, MACD, signal, EMA20, Bollinger Bands.
    """
    prompt = f"""
请基于以下数据分析 {symbol} 在 {exch} 的市场趋势：
最近5日 RSI: {df['rsi'].tail(5).round(2).tolist()}
MACD: {df['macd'].tail(5).round(2).tolist()}
Signal: {df['signal'].tail(5).round(2).tolist()}
EMA20: {df['ema20'].tail(5).round(2).tolist()}
Bollinger High: {df['bb_high'].tail(5).round(2).tolist()}
Bollinger Low: {df['bb_low'].tail(5).round(2).tolist()}
请输出：
1. 当前趋势判断（上涨/下跌/震荡）
2. 关键支撑位与阻力位（如可能）
3. 建议（买入/卖出/观望）
4. 风险提示
"""
    headers = {
        "Authorization": f"Bearer {DEEPC_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一位专业的加密货币技术分析师。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 400
    }
    response = requests.post(f"{DEEPC_BASE}/chat/completions", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def summarize_market(all_advices):
    """
    Summarize the market trends and opportunities based on multiple advices.
    :param all_advices: list of tuples/lists [symbol, exchange, rsi, macd, signal, ema20, bb_high, bb_low, advice]
    :return: summary string
    """
    combined = "\n".join([f"{item[0]}-{item[1]}: {item[-1]}" for item in all_advices])
    prompt = f"""
以下是不同币种的技术分析摘要：
{combined}
请综合判断整体市场趋势、风险和机会，并用简洁中文给出总结段落。
"""
    headers = {
        "Authorization": f"Bearer {DEEPC_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一位专业的市场分析师。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }
    response = requests.post(f"{DEEPC_BASE}/chat/completions", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
