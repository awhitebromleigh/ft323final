import streamlit as st
import pandas as pd
import datetime
import numpy as np

# --- App Configuration ---
st.set_page_config(page_title="UrBank Demo", page_icon="🏙️", layout="centered")

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

# --- Main UI Header ---
st.title("🏙️ UrBank")
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
    st.subheader("Recent Transactions")
    st.write("Automatic cashback from Transit, Groceries, and Subscriptions is instantly routed to your Smart Vault.")
    
    # Styled dataframe
    st.dataframe(
        transactions, 
        use_container_width=True,
        hide_index=True
    )
    
    st.button("💳 View Virtual Card Details", use_container_width=True)

# --- TAB 2: Earn More (APY) ---
with tab_wellness:
    st.header("Your Lifestyle, Your Rate")
    st.write("Complete daily urban habits to boost your base 1.5% APY up to 4.0%.")
    
    st.info("📱 Connected Devices: Apple Watch, MBTA Transit Card")
    
    # Interactive checkboxes
    st.subheader("Today's Progress")
    goal_steps = st.checkbox("Hit daily step target (10,000 steps) [+0.5%]")
    goal_transit = st.checkbox("Commute by public transit or bike [+0.5%]")
    goal_screen = st.checkbox("Stay under personal screen-time limit [+0.5%]")
    goal_cook = st.checkbox("Cook at home (No food delivery today) [+0.5%]")
    goal_sleep = st.checkbox("Consistent sleep schedule (8 hours) [+0.5%]")
    
    # Logic calculations
    goals_met = sum([goal_steps, goal_transit, goal_screen, goal_cook, goal_sleep])
    current_apy = st.session_state.base_apy + (goals_met * 0.5)
    city_score = int((goals_met / 5) * 100)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    col1.metric(label="Current APY", value=f"{current_apy:.2f}%", delta=f"+{goals_met * 0.5:.2f}% Boost")
    
    score_color = "normal" if city_score >= 60 else ("inverse" if city_score < 40 else "off")
    col2.metric(label="City Score", value=f"{city_score}/100", delta_color=score_color)
    
    st.progress(city_score / 100, text=f"City Score Progress: {city_score}%")
    
    if city_score == 100:
        st.success("🎉 Incredible! You've unlocked the maximum interest boost for the week!")

# --- TAB 3: Smart Savings Vault ---
with tab_vault:
    st.header("Smart Savings Vault")
    st.write("Money accumulated automatically from your daily habits.")
