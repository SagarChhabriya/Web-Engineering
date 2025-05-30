import streamlit as st
import sqlite3
import random
import string
import os

# Connect to SQLite database (it will create the file if not already present)
db_path = os.path.join(os.getcwd(), 'url_shortener.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table for storing URLs (if it doesn't exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT NOT NULL,
        original_url TEXT NOT NULL
    )
''')
conn.commit()

# Function to generate a random short code (6 characters)
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to store the URL mapping (short code and original URL)
def store_url(short_code, original_url):
    cursor.execute('''
        INSERT INTO urls (short_code, original_url)
        VALUES (?, ?)
    ''', (short_code, original_url))
    conn.commit()

# Function to retrieve the original URL based on short code
def get_original_url(short_code):
    cursor.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = cursor.fetchone()
    return result[0] if result else None

# Streamlit UI for shortening URLs
st.title("URL Shortener")

# Input field for the original URL
original_url = st.text_input("Enter your long URL:")

if st.button("Shorten URL"):
    if original_url:
        # Generate a random short code for the URL
        short_code = generate_short_code()

        # Store the original URL and its corresponding short code in the database
        store_url(short_code, original_url)

        # Create the shortened URL (replace 'your-app-url' with your actual Streamlit Cloud app URL)
        short_url = f"https://tinyza.streamlit.app/?short_code={short_code}"

        # Display the shortened URL to the user
        st.success(f"Shortened URL: {short_url}")
    else:
        st.error("Please enter a valid URL.")

# Check if the user is accessing a shortened URL by entering the short code in the URL
# Example: If user accesses https://your-username-your-repo-name.streamlit.app/?short_code=abc123

# Get the short code from the query params
short_code_from_url = st.query_params.get("short_code", None)

if short_code_from_url:
    # Retrieve the original URL based on the short code
    original_url = get_original_url(short_code_from_url)

    if original_url:
        # Redirect to the original URL (simulate redirection by displaying it)
        st.write(f"Redirecting to {original_url}...")
        st.experimental_rerun()  # Use rerun to simulate the redirect
    else:
        st.error("Short URL not found.")
