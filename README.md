# trading-position-risk-analysis
Quantitative analysis of trading position profitability, break-even price, transaction costs, and risk-reward using Python.
# Quantitative Trading Position Profit & Risk Analysis

## 📌 Project Overview

This project develops a Python-based quantitative model to analyze the profitability and risk characteristics of a hypothetical NIFTY 50 trading position.

The model evaluates how entry price, exit price, transaction costs, stop-loss, and target levels affect the overall financial outcome of a position.

---

## 🎯 Objectives

- Calculate gross and net profit/loss for a trading position.
- Evaluate the impact of transaction costs on trading returns.
- Determine the break-even exit price.
- Analyze risk-reward characteristics at the stop-loss and target levels.
- Evaluate potential outcomes across multiple exit-price scenarios.
- Visualize the relationship between exit price and net profit/loss.

---

## 📊 Methodology

The analysis considers a hypothetical long position with the following assumptions:

| Parameter | Value |
|---|---:|
| Entry Price | ₹24,000 |
| Position Size | 50 units |
| Position Value | ₹12,00,000 |
| Stop-Loss | ₹23,700 |
| Target Price | ₹24,600 |
| Transaction Cost | 0.10% per side |

The model calculates:

1. Position value
2. Transaction costs
3. Gross profit/loss
4. Net profit/loss
5. ROI
6. Break-even price
7. Price-based risk-reward ratio
8. Net risk-reward ratio
9. Net P/L across different exit prices

---

## 📈 Key Results

| Metric | Result |
|---|---:|
| Break-Even Price | ₹24,048.05 |
| Net Risk at Stop-Loss | ₹17,385 |
| Net Reward at Target | ₹27,570 |
| Net Risk-Reward Ratio | 1 : 1.59 |
| Net Profit at Target | ₹27,570 |
| ROI at Target | 2.30% |

The analysis shows that transaction costs have a measurable impact on trading profitability. Although the price-based risk-reward ratio is 1:2, incorporating transaction costs reduces the effective net risk-reward ratio to approximately 1:1.59.

---

## 📉 Visualization

The following chart illustrates the relationship between exit price and net profit/loss while highlighting the break-even price, stop-loss, and target levels.

![Trading Position Net P/L](images/trading_position_pnl.png)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---
## ▶️ How to Run

git clone https://github.com/YOUR-USERNAME/trading-position-risk-analysis.git
cd trading-position-risk-analysis
pip install -r requirements.txt
python analysis.py
