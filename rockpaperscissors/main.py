import streamlit as st
import random

st.title("Rock, Paper, Scissors")
st.text("Whoever first scores 3 points will win the game")
# Initialize session state only if not already set
if "userscore" not in st.session_state:
    st.session_state.userscore = 0
if "computerscore" not in st.session_state:
    st.session_state.computerscore = 0

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Select your choice", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"Computer chooses: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        st.session_state.userscore += 1
        st.success("You win this round!")
    else:
        st.session_state.computerscore += 1
        st.error("Computer wins this round!")

    # Show current scores
    st.write(f"Your Score: {st.session_state.userscore}")
    st.write(f"Computer Score: {st.session_state.computerscore}")

    # Check for end of game
    if st.session_state.userscore == 3:
        st.balloons()
        st.success("🎉 You won the game!")
        st.session_state.userscore = 0
        st.session_state.computerscore = 0
    elif st.session_state.computerscore == 3:
        st.error("💻 Computer won the game!")
        st.session_state.userscore = 0
        st.session_state.computerscore = 0
