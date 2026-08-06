import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def set_app_config():
    """App-wide page configuration and global CSS styling."""
    st.set_page_config(
        page_title="Daily Cash Summary AI Agent",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
        .metric-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border: 1px solid #e9ecef;
        }
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def init_session_state():
    """Initializes Streamlit session state keys."""
    if "account_details" not in st.session_state:
        st.session_state.account_details = None