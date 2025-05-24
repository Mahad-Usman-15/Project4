import streamlit as st
import random

# Title of the app
st.title("Number Guessing Game")

# Generate a random number between 1 and 100
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)

# Display instructions
st.write("Guess a number between 1 and 100.")

# Get user input
inputfromuser = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

# Check the user's guess
if st.button("Submit Guess"):
    if inputfromuser < 1 or inputfromuser > 100:
        st.error("Please enter a number within the range 1 to 100.")
    elif inputfromuser == st.session_state.number:
        st.success(f"Congratulations! You guessed the correct number: {st.session_state.number}")
        st.balloons()  # Celebrate!
    elif abs(inputfromuser - st.session_state.number) < 3:
        st.warning("You're very close! Try again.")
    else:
        st.error("Your guess is too high. Try again.")

# Optional: Display the correct number for debugging
# st.write(f"Debug: The correct number is {st.session_state.number}")