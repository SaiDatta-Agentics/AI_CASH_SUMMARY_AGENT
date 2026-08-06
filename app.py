from datetime import datetime
import streamlit as st

# Import local modular scripts
from config import set_app_config, init_session_state
from data_manager import generate_mock_transactions
from ai_agent import get_ai_summary
from ui_components import render_bank_card, render_expense_chart

# Initialize setup
set_app_config()
init_session_state()

# -----------------------------------------------------------------------------
# NAVIGATION SIDEBAR
# -----------------------------------------------------------------------------
st.sidebar.title("💳 Cash Flow Agent")
page = st.sidebar.radio("Navigation", ["Part 1: Account Entry & Profile", "Part 2: Daily Report Demo Showcase"])

# -----------------------------------------------------------------------------
# PART 1: ACCOUNT ENTRY & PROFILE
# -----------------------------------------------------------------------------
if page == "Part 1: Account Entry & Profile":
    st.title("⚙️ Account Setup & Profile")
    st.caption("Enter your account details manually to configure the agent.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("📝 Manual Entry Form")
        with st.form("account_form"):
            acc_name = st.text_input("Account Holder Name", value="Alex Morgan")
            bank_name = st.selectbox("Bank Name", ["Chase Bank", "Bank of America", "Wells Fargo", "Capital One", "Revolut"])
            acc_num = st.text_input("Account Number (Last 4 Digits)", value="8842", max_chars=4)
            acc_type = st.radio("Account Type", ["Checking Account", "Savings Account", "Credit Card"])
            opening_bal = st.number_input("Opening Balance ($)", value=5420.50, step=100.0)
            credit_limit = st.number_input("Credit Limit ($)", value=10000.0, step=500.0)
            
            if st.form_submit_button("Save & Link Account", use_container_width=True):
                st.session_state.account_details = {
                    "name": acc_name,
                    "bank": bank_name,
                    "acc_num": f"•••• {acc_num}",
                    "type": acc_type,
                    "opening_bal": opening_bal,
                    "credit_limit": credit_limit,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.success("Account profile saved!")

    with col2:
        st.subheader("📋 Saved Account Display")
        if st.session_state.account_details:
            acc = st.session_state.account_details
            render_bank_card(acc)
            st.markdown("<br/>", unsafe_allow_html=True)
            st.json(acc)
        else:
            st.info("Submit the form on the left to see your details displayed here.")

# -----------------------------------------------------------------------------
# PART 2: DEMO SHOWCASE
# -----------------------------------------------------------------------------
elif page == "Part 2: Daily Report Demo Showcase":
    st.title("📊 Daily Cash Summary Agent")
    
    if st.session_state.account_details:
        acc = st.session_state.account_details
        initial_bal = acc["opening_bal"]
        acc_label = f"{acc['bank']} ({acc['acc_num']})"
    else:
        initial_bal = 5000.00
        acc_label = "Demo Checking Account (•••• 1234)"

    st.caption(f"Account: **{acc_label}** | Date: **{datetime.now().strftime('%B %d, %Y')}**")
    
    # Generate dataset with running balances
    df_tx, money_in, money_out, closing_bal = generate_mock_transactions(initial_bal)

    # 1. Summary Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Opening Balance", f"${initial_bal:,.2f}")
    m2.metric("Money Received", f"${money_in:,.2f}", delta=f"+${money_in:,.2f}")
    m3.metric("Money Spent", f"${money_out:,.2f}", delta=f"-${money_out:,.2f}", delta_color="inverse")
    m4.metric("Closing Balance", f"${closing_bal:,.2f}", delta=f"${closing_bal - initial_bal:,.2f}")

    st.markdown("---")

    # 2. AI Executive Insights
    st.subheader("🤖 AI Agent Summary")
    with st.spinner("AI Agent is analyzing cash flows..."):
        ai_summary = get_ai_summary(
            initial_bal,
            money_in,
            money_out,
            closing_bal,
            df_tx
        )
    st.info(ai_summary)

    st.markdown("---")

    # 3. Expense Charts & Top Outflows
    col_left, col_right = st.columns([3, 2], gap="medium")
    with col_left:
        st.subheader("📈 Expenses Breakdown")
        render_expense_chart(df_tx)

    with col_right:
        st.subheader("🔥 Largest Outflows")
        top_expenses_df = (
            df_tx[df_tx["Amount ($)"] < 0]
            .copy()
            .assign(Amount=lambda x: x["Amount ($)"].abs())
            .sort_values(by="Amount", ascending=False)
            .head(4)[["Time", "Description", "Amount"]]
        )
        st.dataframe(top_expenses_df.style.format({"Amount": "${:,.2f}"}), use_container_width=True, hide_index=True)

    # 4. Detailed Ledger with Balance Column
    st.markdown("### 📝 Full Daily Ledger (with Running Balance)")
    st.dataframe(
        df_tx.style.format({
            "Amount ($)": "${:,.2f}",
            "Balance ($)": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )