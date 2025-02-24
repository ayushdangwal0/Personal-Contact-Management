import sqlite3
import pandas as pd
import streamlit as st

# Database Initialization
conn = sqlite3.connect("contacts.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT)''')
conn.commit()
conn.close()

# Function to Fetch Contacts
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    df = pd.read_sql_query("SELECT * FROM contacts", conn)
    conn.close()
    return df

# Function to Add Contact
def add_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

# Streamlit UI
st.title("📞 Contact Management System")

# Add Contact Form
st.subheader("Add New Contact")
with st.form("add_contact_form"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add Contact")
    if submitted:
        add_contact(name, phone, email)
        st.success(f"Contact {name} added successfully!")

# View Contacts Button
if st.button("View All Contacts"):
    contacts_df = view_contacts()
    st.subheader("All Contacts")
    st.dataframe(contacts_df)

