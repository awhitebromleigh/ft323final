import streamlit as st
import pandas as pd
import datetime

# --- App Configuration ---
st.set_page_config(page_title="UrbanBank Demo", page_icon="🏙️", layout="centered")

# --- Initial State Management ---
if 'checking_balance' not in st.session_state:
    st.session_state.checking_balance = 2450.00
if 'vault_balance' not in st.session_state:
    st.session_state.vault_balance = 530.75
if 'base_apy' not in st.session_state:
    st.session_state.base_apy = 1.5

# --- Mock Data ---
# Simulating a user's recent transactions for "City Rewards" and "Pantry Mode"
transactions = pd.DataFrame({
    'Date': [datetime.date.today() - datetime.timedelta(days=i) for i in range(5)],
    'Merchant': ['Subway (MBTA)', 'Whole Foods', 'Uber Eats', 'Spotify', 'Sweetgreen'],
    'Category': ['Transit', 'Groceries', 'Food Delivery', 'Subscription', 'Dining'],
    'Amount': [2.40, 65.20, 32.50, 10.99, 15.00],
    'Cashback_Earned': [0.05, 0.65, 0.00, 0.11, 0.00]
})

# --- Main UI ---
st.title("🏙️ UrbanBank")
st.caption('"Live Well, Spend Smart, Save Automatically"')

# Create navigation tabs to simulate mobile app screens
tab_home, tab_wellness, tab_vault, tab_pantry = st.tabs([
    "🏠 Home", "🏃 Earn More (APY)", "🏦 Smart Vault", "🛒 Pantry Mode"
])

# --- TAB 1: Home / Dashboard ---
with tab_home:
    st.header("Account Overview")
    
    col1, col2 = st.columns(2)
    col1.metric("Checking Balance", f"${st.session_state.checking_balance:,.2f}")
    col2.metric("Smart Vault Balance", f"${st.session_state.vault_balance:,.2f}")
    
    st.divider()
    st.subheader("Recent Transactions")
    st.dataframe(
        transactions[['Date', 'Merchant', 'Amount', 'Cashback_Earned']], 
        use_container_width=True,
        hide_index=True
    )
    st.info("💡 Automatic cashback from Transit, Groceries, and Subscriptions is instantly routed to your Smart Vault.")

# --- TAB 2: Earn More (Floating APY & City Score) ---
with tab_wellness:
    st.header("Your Lifestyle, Your Rate")
    st
