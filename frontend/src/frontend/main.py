import pandas as pd
import requests
import streamlit as st

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="eClipseBoard", page_icon="🌒")

st.title("eClipseBoard")

response = requests.get(f"{BACKEND_URL}/eclipses")
response.raise_for_status()
df = pd.DataFrame(response.json())

st.write(f"Showing {len(df)} eclipses")
st.dataframe(df)