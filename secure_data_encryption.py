import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac

# Check if the file exists, if not, create it
DATA_FILE = "stored_data.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump({}, file)

# Load data from JSON file
def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Generate a key (this should be stored securely in production)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# User login details (for simplicity, this is a demo)
users = {
    "admin": {"password": "admin123", "failed_attempts": 0, "last_failed_time": 0}
}

# Hashing with PBKDF2
def hash_passkey(passkey, salt):
    return pbkdf2_hmac('sha256', passkey.encode(), salt.encode(), 100000)

# Encrypt data
def encrypt_data(text, passkey):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey, salt):
    hashed_passkey = hash_passkey(passkey, salt)

    # Load stored data
    stored_data = load_data()
    for user_data in stored_data.values():
        if user_data["encrypted_text"] == encrypted_text and user_data["passkey"] == hashed_passkey.hex():
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# User authentication and login logic
def login(username, password):
    if username in users:
        user = users[username]
        
        # Lockout logic for failed attempts
        if user['failed_attempts'] >= 3 and time.time() - user['last_failed_time'] < 300:  # 5 minutes lockout
            st.error("❌ Too many failed login attempts. Please try again later.")
            return False
        
        # Check if the password matches
        if password == user['password']:
            users[username]['failed_attempts'] = 0  # Reset failed attempts
            return True
        else:
            users[username]['failed_attempts'] += 1
            users[username]['last_failed_time'] = time.time()
            st.error(f"❌ Incorrect password! Attempts remaining: {3 - users[username]['failed_attempts']}")
            return False
    else:
        st.error("❌ User not found!")
        return False

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    username = st.text_input("Enter your Username:")
    passkey = st.text_input("Enter Passkey:", type="password")
    user_data = st.text_area("Enter Data:")

    if st.button("Encrypt & Save"):
        if username and passkey and user_data:
            salt = username + "_salt"  # Simple salt based on username
            hashed_passkey = hash_passkey(passkey, salt)
            encrypted_text = encrypt_data(user_data, passkey)

            # Load existing data
            stored_data = load_data()
            stored_data[username] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey.hex()
            }

            # Save new data to file
            save_data(stored_data)
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    username = st.text_input("Enter your Username to retrieve data:")
    passkey = st.text_input("Enter Passkey:", type="password")
    encrypted_text = st.text_area("Enter Encrypted Data:")

    if st.button("Decrypt"):
        if username and passkey and encrypted_text:
            # Load stored data
            stored_data = load_data()

            if username in stored_data:
                decrypted_text = decrypt_data(encrypted_text, passkey, username + "_salt")

                if decrypted_text:
                    st.success(f"✅ Decrypted Data: {decrypted_text}")
                else:
                    st.error(f"❌ Incorrect passkey or data not found!")
            else:
                st.error(f"❌ No data found for {username}")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    username = st.text_input("Enter Username:")
    password = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("✅ Logged in successfully! Redirecting...")
            st.experimental_rerun()
        else:
            st.error("❌ Login failed. Please check your credentials.")
