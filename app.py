import streamlit as st
import pandas as pd
import os

# Load dataset from the Downloads folder
file_path = os.path.expanduser("C:\\Users\\gearh\Downloads\\history.csv")  # Adjust path if necessary
df = pd.read_csv(file_path)

# Title
st.title("Team Search App")

# Search options
team_name = st.text_input("Search by Team Name:")
coach_name = st.text_input("Search by Coach Name:")
year = st.selectbox("Select Year:", ["All"] + sorted(df["Year"].astype(str).unique().tolist()))

# Filter based on input
filtered_df = df.copy()

if team_name:
    filtered_df = filtered_df[filtered_df["Team"].str.contains(team_name, case=False, na=False)]

if coach_name:
    filtered_df = filtered_df[filtered_df["Coach"].str.contains(coach_name, case=False, na=False)]

if year != "All":
    filtered_df = filtered_df[filtered_df["Year"].astype(str) == year]

# Display the filtered results
st.write(f"Showing {len(filtered_df)} results:")
st.dataframe(filtered_df)
