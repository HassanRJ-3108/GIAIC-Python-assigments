import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Rock Paper Scissors", page_icon="✂️")

st.title("Rock Paper Scissors Game")

# Initialize session state variables
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = None
if 'result' not in st.session_state:
    st.session_state.result = None

# Define game choices and their relationships
CHOICES = ["rock", "paper", "scissors"]
RULES = {
    "rock": {"beats": "scissors", "emoji": "✊"},
    "paper": {"beats": "rock", "emoji": "✋"},
    "scissors": {"beats": "paper", "emoji": "✂️"}
}

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif RULES[user_choice]["beats"] == computer_choice:
        return "user"
    else:
        return "computer"

# Function to reset the game
def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0

# Function to make a move
def make_move(user_choice):
    # Set user's choice
    st.session_state.user_choice = user_choice
    
    # Get computer's random choice
    st.session_state.computer_choice = random.choice(CHOICES)
    
    # Determine winner
    winner = determine_winner(
        st.session_state.user_choice,
        st.session_state.computer_choice
    )
    
    # Update scores
    if winner == "user":
        st.session_state.user_score += 1
        st.session_state.result = "You win!"
    elif winner == "computer":
        st.session_state.computer_score += 1
        st.session_state.result = "Computer wins!"
    else:
        st.session_state.ties += 1
        st.session_state.result = "It's a tie!"

# Sidebar with game instructions
with st.sidebar:
    st.header("Game Instructions")
    st.markdown("""
    1. Choose rock, paper, or scissors
    2. The computer will make its choice
    3. Rock beats scissors, scissors beats paper, paper beats rock
    4. First to reach the winning score wins the game
    """)
    
    # Reset game button
    if st.button("Reset Game"):
        reset_game()
        st.rerun()

# Main game area
st.subheader("Make Your Choice")

# Create buttons for each choice
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✊ Rock", use_container_width=True):
        make_move("rock")
with col2:
    if st.button("✋ Paper", use_container_width=True):
        make_move("paper")
with col3:
    if st.button("✂️ Scissors", use_container_width=True):
        make_move("scissors")

# Display the game result
if st.session_state.user_choice is not None and st.session_state.computer_choice is not None:
    st.divider()
    
    # Create columns for user and computer choices
    user_col, vs_col, comp_col = st.columns([2, 1, 2])
    
    with user_col:
        st.markdown("### Your Choice")
        user_emoji = RULES[st.session_state.user_choice]["emoji"]
        st.markdown(f"<h1 style='text-align: center;'>{user_emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>{st.session_state.user_choice.capitalize()}</p>", unsafe_allow_html=True)
    
    with vs_col:
        st.markdown("<h2 style='text-align: center;'>VS</h2>", unsafe_allow_html=True)
    
    with comp_col:
        st.markdown("### Computer's Choice")
        comp_emoji = RULES[st.session_state.computer_choice]["emoji"]
        st.markdown(f"<h1 style='text-align: center;'>{comp_emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>{st.session_state.computer_choice.capitalize()}</p>", unsafe_allow_html=True)
    
    # Display result with appropriate styling
    if "win" in st.session_state.result:
        if "You" in st.session_state.result:
            st.success(f"### {st.session_state.result}")
        else:
            st.error(f"### {st.session_state.result}")
    else:
        st.info(f"### {st.session_state.result}")

# Display scoreboard
st.divider()
st.subheader("Scoreboard")

score_cols = st.columns(3)
with score_cols[0]:
    st.metric("You", st.session_state.user_score)
with score_cols[1]:
    st.metric("Ties", st.session_state.ties)
with score_cols[2]:
    st.metric("Computer", st.session_state.computer_score)