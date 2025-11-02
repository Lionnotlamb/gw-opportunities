# app.py
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="GW Opportunities", layout="wide")
st.title("GW Opportunities Finder")
st.write("Browse fellowships, grants, competitions, and experiential learning programs at GW.")

# Confirm which file is being run
st.text(f"Running app.py from: {os.path.abspath(__file__)}")

# Sample opportunities data
data = [
    {
        "Title": "Planet Forward Experiential Learning Trips",
        "Organization": "Planet Forward",
        "Category": "Experiential Learning",
        "Eligibility": "Undergraduate and graduate students",
        "Deadline": "Varies",
        "Website": "https://planetforward.org/experiential-learning-trips/"
    },
    {
        "Title": "Seeds of the Future Fellowship",
        "Organization": "GW Food Safety and Security Policy Institute",
        "Category": "Research / Fellowship",
        "Eligibility": "Undergraduate and graduate students interested in food systems and sustainability",
        "Deadline": "Varies",
        "Website": "https://foodsafety.gwu.edu/seeds"
    },
    {
        "Title": "Knapp Fellowship for Entrepreneurial Service-Learning",
        "Organization": "The Honey W. Nashman Center",
        "Category": "Grant / Fellowship",
        "Eligibility": "Undergraduate and graduate students",
        "Deadline": "Typically February",
        "Website": "https://serve.gwu.edu/knapp-fellowship"
    },
    {
        "Title": "New Venture Competition (NVC)",
        "Organization": "GW Office of Innovation & Entrepreneurship",
        "Category": "Competition",
        "Eligibility": "All GW students",
        "Deadline": "Typically March",
        "Website": "https://entrepreneurship.gwu.edu/gw-new-venture-competition"
    },
    {
        "Title": "Pitch George Competition",
        "Organization": "GW Center for Entrepreneurial Excellence",
        "Category": "Competition",
        "Eligibility": "All GW students",
        "Deadline": "Typically November",
        "Website": "https://business.gwu.edu/pitch-george"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filter Opportunities")
category_filter = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

eligibility_filter = st.sidebar.text_input("Search by Eligibility:")

# Apply filters
filtered_df = df[df["Category"].isin(category_filter)]
if eligibility_filter:
    filtered_df = filtered_df[filtered_df["Eligibility"].str.contains(eligibility_filter, case=False)]

# Display filtered table
st.dataframe(filtered_df.reset_index(drop=True))

# Make website links clickable
for index, row in filtered_df.iterrows():
    st.markdown(f"[{row['Title']}]({row['Website']}) - {row['Organization']}")


