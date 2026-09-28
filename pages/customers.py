import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customers", page_icon="👥", layout="wide")

st.title("👥 Customers")
st.caption("Manage customer profiles, activity, and loyalty insights.")

customers = pd.DataFrame([
	{"Name": "Ava Johnson", "Email": "ava.johnson@example.com", "Visits": 18, "Spent": 642.50, "Last visit": "Jun 14, 2024", "Status": "Active"},
	{"Name": "Liam Smith", "Email": "liam.smith@example.com", "Visits": 11, "Spent": 385.00, "Last visit": "Jun 12, 2024", "Status": "Active"},
	{"Name": "Sophia Brown", "Email": "sophia.brown@example.com", "Visits": 4, "Spent": 126.75, "Last visit": "May 28, 2024", "Status": "Inactive"},
	{"Name": "Noah Davis", "Email": "noah.davis@example.com", "Visits": 23, "Spent": 910.25, "Last visit": "Jun 15, 2024", "Status": "Active"},
])

with st.sidebar:
	st.header("Filters")
	search = st.text_input("Search customers", placeholder="Name or email")
	statuses = st.multiselect("Status", ["Active", "Inactive"], default=["Active", "Inactive"])

filtered = customers[customers["Status"].isin(statuses)]
if search:
	query = search.lower()
	filtered = filtered[filtered["Name"].str.lower().str.contains(query) | filtered["Email"].str.lower().str.contains(query)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total customers", len(customers))
col2.metric("Active customers", int((customers["Status"] == "Active").sum()))
col3.metric("Total spent", f"${customers['Spent'].sum():,.2f}")
col4.metric("Average spend", f"${customers['Spent'].mean():,.2f}")

st.subheader("Customer directory")
st.dataframe(
	filtered.style.format({"Spent": "${:,.2f}"}),
	use_container_width=True,
	hide_index=True,
)

with st.expander("➕ Add customer"):
	with st.form("add_customer"):
		name, email, phone = st.columns(3)
		new_name = name.text_input("Full name")
		new_email = email.text_input("Email")
		new_phone = phone.text_input("Phone")
		submitted = st.form_submit_button("Save customer", type="primary")
		if submitted:
			if new_name and new_email:
				st.success(f"{new_name} is ready to be added.")
			else:
				st.error("Full name and email are required.")
