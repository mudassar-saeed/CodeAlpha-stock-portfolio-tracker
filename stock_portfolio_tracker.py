# Task 2: Stock Portfolio Tracker

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 100,
    "MSFT": 300
}

print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Collect user input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not in list, try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = sum(stock_prices[symbol] * qty for symbol, qty in portfolio.items())

# Display portfolio and total value
print("\n💼 Your Portfolio:")
for symbol, qty in portfolio.items():
    print(f"{symbol}: {qty} shares x ${stock_prices[symbol]} = ${stock_prices[symbol]*qty}")

print(f"\n💰 Total Investment: ${total_investment}")

# Optionally save to a file
save_file = input("Do you want to save this portfolio to a file? (y/n): ").lower()
if save_file == "y":
    file_name = "portfolio.txt"
    with open(file_name, "w") as f:
        f.write("Your Portfolio:\n")
        for symbol, qty in portfolio.items():
            f.write(f"{symbol}: {qty} shares x ${stock_prices[symbol]} = ${stock_prices[symbol]*qty}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print(f"✅ Portfolio saved to '{file_name}'")
