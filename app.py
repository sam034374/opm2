import streamlit as st
import pandas as pd
import sqlite3

# Set up page config
st.set_page_config(page_title="Opta Event Explorer", layout="wide")

# Connect to your uploaded database
def get_connection():
    return sqlite3.connect('opta_events.db')

st.title("⚽ Opta Event Dashboard")

# 1. Sidebar Filters
st.sidebar.header("Filters")
event_types = ["Pass", "Shot", "Tackle", "Foul"] # Adjust based on your actual data
selected_type = st.sidebar.selectbox("Select Event Type", event_types)

# 2. Query Data based on filter
conn = get_connection()
query = f"SELECT * FROM event_table WHERE event_type = '{selected_type}' LIMIT 1000"
df = pd.read_sql(query, conn)

# 3. Display Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("Events Loaded", len(df))
with col2:
    st.metric("Total in DB", "587,767")

# 4. Show Data Table
st.subheader(f"Recent {selected_type} Events")
st.dataframe(df)
