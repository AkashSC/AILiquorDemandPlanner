import streamlit as st
from predict import predict_sales

st.set_page_config(page_title="Liquor Demand Planner", layout="centered")

st.title("🍷 Liquor Demand & Resource Planner")
st.markdown("Predict demand and plan inventory for liquor products.")

# Inputs
date = st.date_input("Select Date")
region = st.selectbox("Select Region", ["North", "South", "East", "West"])
product_type = st.selectbox("Select Product Type", ["Beer", "Wine", "Spirits"])

if st.button("Predict Demand"):
    prediction = predict_sales(date, region, product_type)
    st.success(f"📦 Predicted Sales: {prediction} units")

    # Resource planning logic
    inventory = round(prediction * 1.2)
    staff = max(1, round(prediction / 100))

    st.markdown(f"🛒 Recommended Inventory: **{inventory} units**")
    st.markdown(f"👥 Suggested Staff: **{staff} personnel**")
