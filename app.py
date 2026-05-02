import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# 1. Connect using the Secret
@st.cache_resource # This keeps the connection alive
def get_engine():
    url = st.secrets["DB_URL"]
    return create_engine(url)

engine = get_engine()

# 2. Query function
@st.cache_data(ttl=600) # This saves data for 10 mins so it's lightning fast
def load_soccer_data(event_type):
    query = f"SELECT * FROM opta_events WHERE event_type = '{event_type}' LIMIT 5000"
    return pd.read_sql(query, engine)

# --- UI Layout ---
st.title("🏆 Pro Opta Analytics")

event = st.selectbox("Select Event", ["Pass", "Shot", "Tackle"])
df = load_soccer_data(event)

st.metric("Events Loaded", len(df))
st.dataframe(df.head(100)) # Show a preview
