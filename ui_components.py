import streamlit as st
import plotly.express as px
import pandas as pd

def render_bank_card(acc_details: dict):
    """Renders account display card."""
    st.markdown(
        f"""
        <div style="padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white;">
            <h3 style="margin:0; color: #f8f9fa;">{acc_details['bank']}</h3>
            <p style="margin: 5px 0 20px 0; opacity: 0.8;">{acc_details['type']}</p>
            <h2 style="margin: 0; font-family: monospace;">{acc_details['acc_num']}</h2>
            <br/>
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <small style="opacity: 0.7;">ACCOUNT HOLDER</small><br/>
                    <b>{acc_details['name']}</b>
                </div>
                <div>
                    <small style="opacity: 0.7;">OPENING BALANCE</small><br/>
                    <b>${acc_details['opening_bal']:,.2f}</b>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

def render_expense_chart(df_tx: pd.DataFrame):
    """Renders Plotly donut chart for expense breakdown."""
    df_expenses = df_tx[df_tx["Amount ($)"] < 0].copy()
    df_expenses["Amount ($)"] = df_expenses["Amount ($)"].abs()
    
    if not df_expenses.empty:
        fig = px.pie(
            df_expenses, 
            values="Amount ($)", 
            names="Category", 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=300)
        st.plotly_chart(fig, use_container_width=True)