import streamlit as st
import pandas as pd

st.set_page_config(page_title="GW Opportunity Finder", layout="wide")

st.title("🎓 GW Opportunity Finder")
st.write("An open-source platform by students, for students — discover and share GW fellowships, grants, internships, and awards.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/opportunities.csv")

data = load_data()

# Filters
majors = st.multiselect("🎯 Filter by major", sorted(data["Major"].dropna().unique()))
eligibility = st.multiselect("👩‍🎓 Filter by eligibility", sorted(data["Eligibility"].dropna().unique()))
category = st.multiselect("📁 Filter by category", sorted(data["Category"].dropna().unique()))

filtered = data.copy()

if majors:
    filtered = filtered[filtered["Major"].isin(majors)]
if eligibility:
    filtered = filtered[filtered["Eligibility"].isin(eligibility)]
if category:
    filtered = filtered[filtered["Category"].isin(category)]

st.dataframe(filtered, use_container_width=True)

st.markdown("---")
st.write("💡 Want to add an opportunity? [Contribute here!](https://github.com/Lionnotlamb/gw-opportunity-finder)")
