import random
from datetime import datetime, timedelta
import pandas as pd

def generate_mock_transactions(initial_balance: float):
    """Generates dummy transactions and computes the running balance for each row."""
    random.seed(42)  # For reproducible demo results
    categories_in = ["Client Payment", "Freelance Income", "Refund", "Investment Yield"]
    categories_out = ["Office Supplies", "AWS Cloud Services", "Dining Out", "Software Subscription", "Utilities", "Groceries"]

    raw_tx = []
    num_tx = random.randint(8, 12)
    
    # Generate random timestamp entries for today
    base_time = datetime.now().replace(hour=8, minute=0, second=0)
    for i in range(num_tx):
        tx_time = base_time + timedelta(minutes=random.randint(15, 50) * (i + 1))
        is_income = random.choices([True, False], weights=[0.35, 0.65])[0]
        
        if is_income:
            amount = round(random.uniform(150, 2500), 2)
            category = random.choice(categories_in)
            desc = f"Received: {category}"
        else:
            amount = -round(random.uniform(10, 450), 2)
            category = random.choice(categories_out)
            desc = f"Spent: {category}"

        raw_tx.append({
            "Time": tx_time.strftime("%H:%M"),
            "Description": desc,
            "Category": category,
            "Amount ($)": amount,
            "Type": "Income" if amount > 0 else "Expense"
        })

    df = pd.DataFrame(raw_tx)

    # Calculate Running Balance after every transaction row
    running_balances = []
    current_bal = initial_balance
    
    for amt in df["Amount ($)"]:
        current_bal += amt
        running_balances.append(round(current_bal, 2))
        
    df["Balance ($)"] = running_balances

    # Summary Statistics
    money_received = df[df["Amount ($)"] > 0]["Amount ($)"].sum()
    money_spent = abs(df[df["Amount ($)"] < 0]["Amount ($)"].sum())
    closing_balance = df["Balance ($)"].iloc[-1] if not df.empty else initial_balance

    return df, money_received, money_spent, closing_balance