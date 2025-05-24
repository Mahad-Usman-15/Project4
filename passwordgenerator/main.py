import streamlit as st
import random

# Set page title with icon
st.set_page_config(page_title="Password Generator", page_icon="🔑")

# Title with icon
st.title("🔐 Strong Password Generator")

# Character sets (unchanged)
CAP = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
splitted = list(CAP)
small = "abcdefghijklmnopqrstuvwxyz"
splitted2 = list(small)
numbers = "12345678"
splitted3 = list(numbers)
special = "!@#$^&"
splitted4 = list(special)

# Input fields with icons
Uppercaseletters = st.number_input("🔠 Uppercase letters", value=0)
Lowercase = st.number_input("🔡 Lowercase letters", value=0)
Numbers = st.number_input("🔢 Numbers", value=0)
Special = st.number_input("⚠️ Special characters", value=0)

# Password generation (unchanged logic)
total = Uppercaseletters + Lowercase + Numbers + Special
if total >= 8:
    if Uppercaseletters and Lowercase and Numbers and Special:
        picked = random.sample(splitted, Uppercaseletters)
        picked2 = random.sample(splitted2, Lowercase)
        picked3 = random.sample(splitted3, Numbers)
        picked4 = random.sample(splitted4, Special)
        password = picked + picked2 + picked3 + picked4
        random.shuffle(password)
        password = ''.join(password)
        
        # Display password with success style
        st.success("### Your Generated Password")
        st.code(password, language="text")
    else:
        st.error("❌ Enter correct quantity")
else:
    st.error("❌ The password should be at least 8 characters")