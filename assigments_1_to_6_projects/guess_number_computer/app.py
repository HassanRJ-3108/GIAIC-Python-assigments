import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Guess the Number (Computer)", page_icon="🤖")

st.title("Guess the Number Game")
st.subheader("Computer tries to guess your number!")

# Initialize session state variables if they don't exist
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 100
if 'guess' not in st.session_state:
    st.session_state.guess = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to reset the game
def reset_game():
    st.session_state.game_started = False
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = None
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.messages = []

# Function to make a guess using binary search (most efficient)
def make_guess():
    st.session_state.attempts += 1
    # Use binary search algorithm for optimal guessing
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.messages.append(f"🤖 I guess: {st.session_state.guess}")

# Sidebar with instructions
with st.sidebar:
    st.header("Game Instructions")
    st.markdown("""
    1. Think of a number between 1 and 100
    2. The computer will try to guess it
    3. Tell the computer if its guess is too high, too low, or correct
    4. See how many attempts it takes!
    """)

# Start game section
if not st.session_state.game_started:
    st.markdown("""
    ### Think of a number between 1 and 100
    Don't tell me what it is! I'll try to guess it.
    """)
    
    # Secret number input for testing/demo purposes
    secret_number = st.number_input(
        "For testing: Enter your secret number",
        min_value=1,
        max_value=100,
        value=random.randint(1, 100),
        help="This is just for testing. In a real game, you would keep this number in your mind."
    )
    
    if st.button("Start Game"):
        st.session_state.game_started = True
        st.session_state.secret_number = secret_number
        make_guess()
        st.rerun()

# Game in progress
if st.session_state.game_started and not st.session_state.game_over:
    # Display game status
    st.markdown(f"### Round {st.session_state.attempts}")
    
    # Display message history
    for msg in st.session_state.messages:
        st.markdown(msg)
    
    # Display current guess and get feedback
    if st.session_state.guess is not None:
        st.markdown("### Is my guess correct?")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Too Low"):
                st.session_state.low = st.session_state.guess + 1
                st.session_state.messages.append("👤 Too low!")
                make_guess()
                st.rerun()
        with col2:
            if st.button("Correct!"):
                st.session_state.game_over = True
                st.session_state.messages.append(f"🎉 I got it in {st.session_state.attempts} attempts!")
                st.rerun()
        with col3:
            if st.button("Too High"):
                st.session_state.high = st.session_state.guess - 1
                st.session_state.messages.append("👤 Too high!")
                make_guess()
                st.rerun()
        
        # Auto-answer for demo mode
        if st.session_state.guess < st.session_state.secret_number:
            st.session_state.low = st.session_state.guess + 1
            st.session_state.messages.append("👤 Too low!")
            make_guess()
            st.rerun()
        elif st.session_state.guess > st.session_state.secret_number:
            st.session_state.high = st.session_state.guess - 1
            st.session_state.messages.append("👤 Too high!")
            make_guess()
            st.rerun()
        else:
            st.session_state.game_over = True
            st.session_state.messages.append(f"🎉 I got it in {st.session_state.attempts} attempts!")
            st.rerun()

# Game over state
if st.session_state.game_over:
    # Display message history
    for msg in st.session_state.messages:
        st.markdown(msg)
    
    # Display game stats
    st.success(f"Game completed! The number was {st.session_state.secret_number}")
    
    # Theoretical minimum attempts (log2 of range)
    import math
    min_attempts = math.ceil(math.log2(100))
    st.markdown(f"The theoretical minimum number of attempts needed was {min_attempts}.")
    
    # Play again button
    if st.button("Play Again"):
        reset_game()
        st.rerun()