import streamlit as st
import random
import time
import math

# Set page configuration
st.set_page_config(page_title="Guess the Number (Computer)", page_icon="🎮")

st.title("Guess the Number Game")
st.subheader("Computer tries to guess your number!")

# Initialize session state variables
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'min_range' not in st.session_state:
    st.session_state.min_range = 1
if 'max_range' not in st.session_state:
    st.session_state.max_range = 100
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'current_guess' not in st.session_state:
    st.session_state.current_guess = None
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'user_number' not in st.session_state:
    st.session_state.user_number = None
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# Function to reset the game
def reset_game():
    st.session_state.game_started = False
    st.session_state.min_range = 1
    st.session_state.max_range = 100
    st.session_state.attempts = 0
    st.session_state.current_guess = None
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.user_number = None
    st.session_state.start_time = None

# Function to make a computer guess
def computer_guess():
    # Binary search approach
    return (st.session_state.min_range + st.session_state.max_range) // 2

# Sidebar with game instructions
with st.sidebar:
    st.header("Game Instructions")
    st.markdown("""
    1. Think of a number between 1 and 100
    2. The computer will try to guess it
    3. Tell the computer if its guess is too high, too low, or correct
    4. See how many attempts it takes!
    """)
    
    # Display current game settings
    st.divider()
    st.write(f"Range: {st.session_state.min_range} to {st.session_state.max_range}")
    
    # Option to set a custom number (for testing)
    custom_number = st.number_input(
        "Set your number (optional):",
        min_value=1,
        max_value=100,
        value=None,
        help="You can set your number here or just keep it in your mind"
    )
    
    if custom_number and not st.session_state.game_started:
        st.session_state.user_number = custom_number

# Main game area
if not st.session_state.game_started:
    st.markdown("### Think of a number between 1 and 100")
    
    if st.button("Start Game"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()
        st.session_state.current_guess = computer_guess()
        st.session_state.attempts += 1
        st.session_state.guesses.append(st.session_state.current_guess)
        st.rerun()

# Game in progress
elif st.session_state.game_started and not st.session_state.game_over:
    # Display current guess
    st.markdown(f"### 🤖 I guess: {st.session_state.current_guess}")
    
    # User feedback buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👤 Too low!"):
            st.session_state.min_range = st.session_state.current_guess + 1
            st.session_state.current_guess = computer_guess()
            st.session_state.attempts += 1
            st.session_state.guesses.append(st.session_state.current_guess)
            
            # Check if range is invalid (user might be cheating)
            if st.session_state.min_range > st.session_state.max_range:
                st.session_state.game_over = True
                st.session_state.error = "Invalid range! Are you changing your number?"
            st.rerun()
    
    with col2:
        if st.button("👤 Too high!"):
            st.session_state.max_range = st.session_state.current_guess - 1
            st.session_state.current_guess = computer_guess()
            st.session_state.attempts += 1
            st.session_state.guesses.append(st.session_state.current_guess)
            
            # Check if range is invalid (user might be cheating)
            if st.session_state.min_range > st.session_state.max_range:
                st.session_state.game_over = True
                st.session_state.error = "Invalid range! Are you changing your number?"
            st.rerun()
    
    with col3:
        if st.button("🎯 Correct!"):
            st.session_state.game_over = True
            st.rerun()
    
    # Display previous guesses
    if st.session_state.guesses:
        st.markdown("### Previous Guesses")
        for i, guess in enumerate(st.session_state.guesses[:-1]):  # All except current
            if guess < st.session_state.current_guess:
                st.markdown(f"Guess #{i+1}: **{guess}** was too low")
            elif guess > st.session_state.current_guess:
                st.markdown(f"Guess #{i+1}: **{guess}** was too high")

# Game over state
if st.session_state.game_over:
    if 'error' in st.session_state:
        st.error(st.session_state.error)
    else:
        st.balloons()
        st.success(f"🎉 I got it in {st.session_state.attempts} attempts!")
        
        # Calculate theoretical minimum
        if st.session_state.user_number:
            actual_number = st.session_state.user_number
        else:
            actual_number = st.session_state.current_guess
            
        theoretical_min = math.ceil(math.log2(100))
        
        st.markdown(f"Game completed! The number was {actual_number}")
        st.markdown(f"The theoretical minimum number of attempts needed was {theoretical_min}.")
        
        # Display time taken
        if st.session_state.start_time:
            time_taken = time.time() - st.session_state.start_time
            st.markdown(f"Time taken: {time_taken:.2f} seconds")
    
    # Play again button
    if st.button("Play Again"):
        reset_game()
        st.rerun()
