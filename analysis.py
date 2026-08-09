import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# QUANTITATIVE TRADING POSITION PROFIT & RISK ANALYSIS
# ============================================================

# ------------------------------------------------------------
# 1. Trading Position Parameters
# ------------------------------------------------------------

entry_price = 24000
position_size = 50

stop_loss = 23700
target_price = 24600

transaction_cost_rate = 0.001  # 0.10% per side


# ------------------------------------------------------------
# 2. Position Value
# ------------------------------------------------------------

position_value = entry_price * position_size

print("Position Value: ₹", position_value)


# ------------------------------------------------------------
# 3. Transaction Costs
# ------------------------------------------------------------

entry_cost = (
    entry_price
    * position_size
    * transaction_cost_rate
)

exit_cost_target = (
    target_price
    * position_size
    * transaction_cost_rate
)

total_transaction_cost = (
    entry_cost + exit_cost_target
)

print("Entry Transaction Cost: ₹", entry_cost)
print("Exit Transaction Cost: ₹", exit_cost_target)
print(
    "Total Transaction Cost: ₹",
    total_transaction_cost
)


# ------------------------------------------------------------
# 4. Gross Profit at Target
# ------------------------------------------------------------

gross_profit = (
    target_price - entry_price
) * position_size

print("Gross Profit at Target: ₹", gross_profit)


# ------------------------------------------------------------
# 5. Net Profit at Target
# ------------------------------------------------------------

net_profit = (
    gross_profit - total_transaction_cost
)

print("Net Profit at Target: ₹", net_profit)


# ------------------------------------------------------------
# 6. Loss at Stop-Loss
# ------------------------------------------------------------

gross_loss = (
    entry_price - stop_loss
) * position_size

print("Gross Loss at Stop-Loss: ₹", gross_loss)


# ------------------------------------------------------------
# 7. Price-Based Risk-Reward Ratio
# ------------------------------------------------------------

potential_reward = target_price - entry_price

potential_risk = entry_price - stop_loss

risk_reward_ratio = (
    potential_reward / potential_risk
)

print(
    "Price-Based Risk-Reward Ratio: 1 :",
    round(risk_reward_ratio, 2)
)


# ------------------------------------------------------------
# 8. Return on Investment
# ------------------------------------------------------------

roi = (
    net_profit / position_value
) * 100

print(
    "ROI at Target:",
    round(roi, 2),
    "%"
)


# ------------------------------------------------------------
# 9. Break-Even Price
# ------------------------------------------------------------

break_even_price = (
    entry_price
    * (1 + transaction_cost_rate)
    / (1 - transaction_cost_rate)
)

print(
    "Break-Even Exit Price: ₹",
    round(break_even_price, 2)
)


# ------------------------------------------------------------
# 10. Exit Price Scenario Analysis
# ------------------------------------------------------------

exit_prices = np.array([
    23500,
    23700,
    24000,
    24200,
    24400,
    24600,
    24800
])


gross_pnl = (
    exit_prices - entry_price
) * position_size


total_costs = (
    entry_price
    * position_size
    * transaction_cost_rate
    +
    exit_prices
    * position_size
    * transaction_cost_rate
)


net_pnl = gross_pnl - total_costs


results = pd.DataFrame({
    "Exit Price": exit_prices,
    "Gross P/L": gross_pnl,
    "Transaction Cost": total_costs,
    "Net P/L": net_pnl
})

print("\nExit Price Scenario Analysis")
print(results.to_string(index=False))


# ------------------------------------------------------------
# 11. Net Risk-Reward Analysis
# ------------------------------------------------------------

stop_loss_exit_cost = (
    stop_loss
    * position_size
    * transaction_cost_rate
)

target_exit_cost = (
    target_price
    * position_size
    * transaction_cost_rate
)


net_risk = (
    (entry_price - stop_loss)
    * position_size
    + entry_cost
    + stop_loss_exit_cost
)


net_reward = (
    (target_price - entry_price)
    * position_size
    - entry_cost
    - target_exit_cost
)


net_risk_reward_ratio = (
    net_reward / net_risk
)

print(
    "\nNet Risk at Stop-Loss: ₹",
    round(net_risk, 2)
)

print(
    "Net Reward at Target: ₹",
    round(net_reward, 2)
)

print(
    "Net Risk-Reward Ratio: 1 :",
    round(net_risk_reward_ratio, 2)
)


# ------------------------------------------------------------
# 12. Visualization
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    exit_prices,
    net_pnl,
    marker="o",
    label="Net P/L"
)

plt.axhline(
    0,
    linestyle="--",
    label="Zero P/L"
)

plt.axvline(
    break_even_price,
    linestyle="--",
    label="Break-even Price"
)

plt.axvline(
    stop_loss,
    linestyle=":",
    label="Stop-loss"
)

plt.axvline(
    target_price,
    linestyle=":",
    label="Target Price"
)

plt.title(
    "Trading Position: Net P/L vs Exit Price"
)

plt.xlabel("Exit Price (₹)")

plt.ylabel("Net Profit / Loss (₹)")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 13. Final Project Summary
# ------------------------------------------------------------

print("\n========== TRADING POSITION ANALYSIS ==========")

print(
    f"Entry Price: ₹{entry_price:,.2f}"
)

print(
    f"Position Size: {position_size} units"
)

print(
    f"Position Value: ₹{position_value:,.2f}"
)

print(
    f"\nBreak-Even Price: ₹{break_even_price:,.2f}"
)

print(
    f"\nNet Risk at Stop-Loss: ₹{net_risk:,.2f}"
)

print(
    f"Net Reward at Target: ₹{net_reward:,.2f}"
)

print(
    f"Net Risk-Reward Ratio: "
    f"1 : {net_risk_reward_ratio:.2f}"
)

print(
    f"\nNet Profit at Target: ₹{net_profit:,.2f}"
)

print(
    f"ROI at Target: {roi:.2f}%"
)

print(
    "\n==============================================="
)
