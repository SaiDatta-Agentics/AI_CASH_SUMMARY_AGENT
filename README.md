# 💰 Daily Cash Summary AI Agent

An interactive Streamlit-based **AI Cash Flow Agent** powered by **Groq Llama 3.3 70B** that tracks money inflows and outflows, calculates running balances row-by-row, and generates executive financial summaries.

---

## 📸 Demo Screenshots

### Part 1: Account Setup & Live Digital Card Display
> *Users enter bank account details and immediately view a rendered profile card and structured JSON summary.*

![Part 1 - Account Setup](assets/part1_account_entry.png)

---

### Part 2: Interactive Daily Cash Dashboard & AI Analysis
> *Displays high-level KPIs, AI-generated daily insights via Groq, category expense distribution, and a real-time running balance ledger.*

![Part 2 - Daily Dashboard](assets/part2_dashboard.png)

---

## ✨ Key Features

- **Part 1: Manual Entry & Profile**
  - Modern form input for bank name, account number, opening balance, and credit limit.
  - Interactive credit/debit card UI card preview.
  - Structured data validation and JSON rendering.

- **Part 2: Daily Cash Dashboard Showcase**
  - **Key Metrics Overview**: Opening Balance, Money Received, Money Spent, and Closing Balance.
  - **Groq LLM Integration**: Generates natural language executive summaries and financial advice automatically using environment keys.
  - **Row-by-Row Running Balance**: Computes and displays updated total balance after every single transaction.
  - **Plotly Visualizations**: Donut chart detailing category-wise expense distribution.
  - **Top Outflows Table**: Highlights top 4 largest transactions for the day.

---

## 📁 Repository Structure

```text
daily_cash_agent/
│
├── assets/                    # Screenshots for GitHub README
│   ├── part1_account_entry.png
│   └── part2_dashboard.png
├── .env                       # API keys (Keep private!)
├── .gitignore                 # Files to exclude from git (e.g. .env)
├── requirements.txt           # Python dependency list
├── config.py                  # Page settings & global CSS styling
├── ai_agent.py                # Groq LLM integration logic
├── data_manager.py            # Transaction generator & running balance math
├── ui_components.py           # Styled card UI & Plotly chart renders
├── app.py                     # Main Streamlit application entry point
└── README.md                  # Project documentation