import os
import pandas as pd
from groq import Groq

def get_ai_summary(opening: float, received: float, spent: float, closing: float, df_tx: pd.DataFrame) -> str:
    """Uses Groq API to produce a cash flow analysis using GROQ_API_KEY from environment."""
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return "ℹ️ *Note: Add `GROQ_API_KEY=your_key` in `.env` to enable automated AI executive insights.*"

    try:
        client = Groq(api_key=api_key)
        top_expenses = df_tx[df_tx["Amount ($)"] < 0].sort_values("Amount ($)").head(3).to_dict('records')
        
        prompt = f"""
        You are a personal financial agent. Provide a concise, bulleted daily summary based on these numbers:
        - Opening Balance: ${opening:,.2f}
        - Total Money Received: ${received:,.2f}
        - Total Money Spent: ${spent:,.2f}
        - Closing Balance: ${closing:,.2f}
        - Top Outflows: {top_expenses}

        Keep it professional, brief (3 bullet points max), and offer 1 useful tip for cash flow management.
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=250,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ *Error running AI Agent:* {str(e)}"