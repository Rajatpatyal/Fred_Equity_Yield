# AI-Powered US Equity Market Analytics Platform

## Overview

The AI-Powered US Equity Market Analytics Platform is a Python-based financial intelligence solution that leverages Federal Reserve Economic Data (FRED) APIs to analyze equity market conditions, economic indicators, volatility, inflation, interest rates, and overall market sentiment.

The platform automatically retrieves market data, generates risk and opportunity scores, produces professional visualizations, and creates institutional-style PDF research reports suitable for investors, portfolio managers, researchers, and financial analysts.

---

## Features

### Market Intelligence Dashboard

* S&P 500 Analysis
* NASDAQ Analysis
* Dow Jones Analysis
* VIX Volatility Monitoring
* Inflation Tracking
* Federal Funds Rate Monitoring
* Unemployment Analysis
* Treasury Yield Monitoring

### Market Analytics

* Market Risk Score
* Opportunity Score
* Economic Health Score
* Market Regime Classification

  * Bullish
  * Neutral
  * Bearish

### Visualizations

* Market Snapshot Dashboard
* Economic Health Dashboard
* Risk vs Opportunity Analysis
* Market Regime Visualization
* Executive Dashboard

### Automated Reporting

* Executive Summary
* Market Commentary
* Risk Analysis
* Opportunity Analysis
* Portfolio Recommendations
* Scenario Analysis
* Professional PDF Report

---

## Architecture

```text
FRED API
    │
    ▼
fred_downloader.py
    │
    ▼
market_scoring.py
    │
    ▼
chart_generator.py
    │
    ▼
pdf_report_builder.py
    │
    ▼
US_Equity_Market_Report.pdf
```

---

## Project Structure

```text
Equity_Analytics/
│
├── fred_downloader.py
├── market_scoring.py
├── chart_generator.py
├── pdf_report_builder.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    │
    ├── market_snapshot.csv
    ├── market_scores.csv
    ├── market_commentary.txt
    │
    ├── market_snapshot.png
    ├── economic_health.png
    ├── risk_vs_opportunity.png
    ├── market_regime.png
    ├── dashboard.png
    │
    └── US_Equity_Market_Report.pdf
```

---

## Data Sources

The platform retrieves economic and market indicators directly from the Federal Reserve Economic Data (FRED) API.

### Indicators Used

| Series    | Description                      |
| --------- | -------------------------------- |
| SP500     | S&P 500 Index                    |
| NASDAQCOM | NASDAQ Composite                 |
| DJIA      | Dow Jones Industrial Average     |
| VIXCLS    | CBOE Volatility Index (VIX)      |
| FEDFUNDS  | Federal Funds Rate               |
| UNRATE    | Unemployment Rate                |
| CPIAUCSL  | Consumer Price Index (Inflation) |
| DGS10     | 10-Year Treasury Yield           |

---

## Market Scoring Model

### Economic Health Score

The Economic Health Score combines:

* Inflation Conditions
* Employment Conditions
* Interest Rate Environment

### Risk Score

The Risk Score evaluates:

* Market Volatility
* Economic Risk
* Monetary Policy Conditions

### Opportunity Score

The Opportunity Score identifies favorable market conditions by combining:

* Economic Strength
* Volatility Conditions
* Market Stability

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Fred_Equity_Yield.git

cd Fred_Equity_Yield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Set your FRED API Key:

```python
API_KEY = "YOUR_FRED_API_KEY"
```

Recommended:

```bash
export FRED_API_KEY=YOUR_FRED_API_KEY
```

Then access it in Python:

```python
import os

API_KEY = os.getenv("FRED_API_KEY")
```

---

## Running the Platform

```bash
python main.py
```

---

## Generated Outputs

### CSV Files

* market_snapshot.csv
* market_scores.csv

### Text Output

* market_commentary.txt

### Charts

* market_snapshot.png
* economic_health.png
* risk_vs_opportunity.png
* market_regime.png
* dashboard.png

### PDF Report

* US_Equity_Market_Report.pdf

---

## Example Output

### Market Snapshot

| Metric       | Example |
| ------------ | ------- |
| S&P 500      | 7609    |
| NASDAQ       | 27086   |
| Dow Jones    | 51307   |
| VIX          | 16      |
| Inflation    | 332     |
| Unemployment | 4.3     |

### Market Regime

```text
Bullish
```

### Opportunity Score

```text
7.8 / 10
```

---

## Use Cases

### Investment Research

* Market Condition Monitoring
* Economic Analysis
* Portfolio Research

### Asset Management

* Risk Assessment
* Opportunity Screening
* Portfolio Allocation

### Financial Education

* Economic Indicator Analysis
* Market Intelligence
* Quantitative Finance Projects

### Data Science Portfolio

* API Integration
* Financial Analytics
* Data Visualization
* Automated Reporting

---

## Future Enhancements

* Sector Rotation Analysis
* Stock Market Forecasting
* Machine Learning Market Prediction
* Sharpe Ratio Analysis
* Momentum Indicators
* Relative Strength Analysis
* ETF Analytics
* Portfolio Optimization
* Power BI Dashboard Integration
* Databricks Integration

---

## Technologies Used

* Python
* Pandas
* Requests
* Matplotlib
* ReportLab
* FRED API

---

## Disclaimer

This project is intended for educational, research, and portfolio demonstration purposes only. It does not constitute financial advice, investment recommendations, or trading guidance.

---

## Author

Rajat Patyal

MissionVision

Data • AI • Cloud • Financial Analytics
