import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# --- App Configuration ---
st.set_page_config(page_title="UrbanBank Demo", page_icon="🏙️", layout="centered")

# --- Initial State Management ---
if 'checking_balance' not in st.session_state:
    st.session_state.checking_balance = 2450.00
if 'vault_balance' not in st.session_state:
    st.session_state.vault_balance = 530.75
if 'base_apy' not in st.session_state:
    st.session_state.base_apy = 1.50

# --- Mock Data ---
transactions = pd.DataFrame({
    'Date': [datetime.date.today() - datetime.timedelta(days=i) for i in range(5)],
    'Merchant': ['MBTA Transit', 'Whole Foods', 'Uber Eats', 'Spotify', 'Sweetgreen'],
    'Category': ['Transit', 'Groceries', 'Food Delivery', 'Subscription', 'Dining'],
    'Amount': [2.40, 65.20, 32.50, 10.99, 15.00],
    'Cashback': ['+$0.05', '+$0.65', '-', '+$0.11', '-']
})

# Mock data for Pie Chart based on typical paycheck distribution
expense_data = pd.DataFrame({
    "Category": ["Housing", "Transportation", "Food & Beverage", "Savings", "Utilities", "Personal/Misc", "Debt & Medical"],
    "Allocation (%)": [30, 15, 15, 15, 10, 10, 5]
})

# Mock data for Vault Growth over time
vault_history = pd.DataFrame({
    "Day": [f"Day {i}" for i in range(1, 15)],
    "Balance": [200, 215, 230, 245, 260, 310, 325, 340, 355, 390, 410, 425, 480, 530.75]
})

# --- Main UI Header ---
st.title("🏙️ UrbanBank")
st.caption('"Live Well, Spend Smart, Save Automatically"')

# --- Tabs ---
tab_home, tab_wellness, tab_vault, tab_pantry = st.tabs([
    "🏠 Home", "📈 Earn More (APY)", "🏦 Smart Vault", "🛒 Pantry Mode"
])

# --- TAB 1: Home ---
with tab_home:
    st.header("Account Overview")
    
    col1, col2 = st.columns(2)
    col1.metric("Checking Balance", f"${st.session_state.checking_balance:,.2f}")
    col2.metric("Smart Vault Balance", f"${st.session_state.vault_balance:,.2f}")
    
    st.divider()
    
    # Interactive Expense Pie Chart
    st.subheader("Where is your paycheck going?")
    fig = px.pie(
        expense_data, 
        values='Allocation (%)', 
        names='Category', 
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.Tealgrn
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.subheader("Recent Transactions")
    st.write("Automatic cashback from Transit, Groceries, and Subscriptions is instantly routed to your Smart Vault.")
    
    st.dataframe(
        transactions, 
        use_container_width=
