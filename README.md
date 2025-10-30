# Crypto AI Report  

该项目是自动化生成加密货币市场分析报告的工具。此版本经过优化迭代，具备以下特点：  

- 环境配置：支持通过 `.env` 配置需要监控的币种 (`SYMBOLS`) 和交易所 (`EXCHANGES`)，以及报告输出路径 (`REPORT_PATH`)。  
- 稳健的数据获取：在拉取 Binance / OKX 行情时加入重试逻辑，提高网络请求稳定性。  
- 额外的技术指标：在原有 RSI 和 MACD 基础上，新增 20 日指数移动平均 (EMA20) 及布林带 (Bollinger Bands) 指标，提供更丰富的技术视觉。  
- 优化的 DeepSeek 提示词：生成更结构化的买卖建议，包含趋势判断、支撑阶戳、建议与风险提示。  
- 自动生成 PDF 报告：包含每个币种的指标、建议以及总体市场总结。  

## 安装方法  

```bash
git clone <your_path>
cd crypto_ai
pip install -r requirements.txt
cp .env.example .env
# 在 .env 中填写你的 DEEPC_API_KEY 以及必要的 SYMBOLS、EXCHANGES
python main.py
```

生成的报告将保存在你配置的 `REPORT_PATH` 目录下，文件名为 `crypto_report_YYYY-MM-DD.pdf`。  

## 文件说明  

- `config.py`：加载环境变量，定义符号、交易所、报告路径和历史天数等配置。  
- `data_fetch.py`：从 Binance / OKX 拉取历史行情，并加入重试机制。  
- `indicators.py`：计算 RSI、MACD、Signal、EMA20、布林带等指标。  
- `deepseek_api.py`：调用 DeepSeek API，根据指标生成交易建议，并汇总市场观点。  
- `report_generator.py`：使用 reportlab 自动生成图文 PDF 报告。  
- `main.py`：主入口，串联数据获取、指标计算、AI 分析和报告生成。
